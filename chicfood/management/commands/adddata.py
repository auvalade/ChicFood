from model_mommy import mommy
import random
import string
import decimal
from elasticsearch.client import IndicesClient
from elasticsearch.helpers import bulk
from django.core.management.base import BaseCommand
from django.conf import settings
from chicfood.models import Food

class Command(BaseCommand):
    help = "Fills the database with dummy Food data and updates the ES index."
    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int)

    def handle(self, *args, **options):
        print ('Started ... ')
        self.reset_all_food()
        print ('|-- Database Emptied ')
        self.make_some_food(options)
        print ('|-- New random Food Added')
        self.recreate_index()
        self.push_db_to_index()
        print ('|-- ElasticSearch index updated ')
        print('... and done !')

    def reset_all_food(self):
        Food.objects.all().delete()

    def make_some_food(self, options):
        self.food_array = []
        for _ in range(options.get('count')[0]):
            myfood = mommy.prepare(
                Food,
                name=''.join([random.choice(string.ascii_lowercase) for n in range(20)]),
                short_desc=''.join([random.choice(string.ascii_letters) for n in range(256)]),
                quantity=random.randint(0, 999),
                healthy_level=random.randint(0, 10),
                taste_level=random.randint(0, 10),
                price = decimal.Decimal(random.randrange(9999))/100,
            )
            self.food_array.append(myfood)
        Food.objects.bulk_create(self.food_array)


    def recreate_index(self):
        indices_client = IndicesClient(client=settings.ES_CLIENT)
        index_name = Food._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name, body={"analysis": { "filter": { "trigrams_filter": {  "type":     "ngram", "min_gram": 3, "max_gram": 3 } }, "analyzer": { "trigrams": { "type": "custom", "tokenizer": "standard", "filter":   [ "lowercase", "trigrams_filter" ]}}}})
        
        indices_client.put_mapping(
            doc_type=Food._meta.es_type_name,
            body=Food._meta.es_mapping,
            index=index_name
        )

    def push_db_to_index(self):
        data = [
            self.convert_for_bulk(f, 'create') for f in Food.objects.all()
        ]
        bulk(client=settings.ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, django_object, action=None):
        data = django_object.es_repr()
        metadata = {
            '_op_type': action,
            "_index": django_object._meta.es_index_name,
            "_type": django_object._meta.es_type_name,
        }
        data.update(**metadata)
        return data


