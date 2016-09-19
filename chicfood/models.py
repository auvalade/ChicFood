from django.db import models
from django.conf import settings
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)


class Food(models.Model):
    name = models.CharField(max_length=20)
    short_desc = models.CharField(max_length=256)
    healthy_level = models.IntegerField()  
    taste_level = models.IntegerField()  
    quantity = models.IntegerField()  
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return str(name) 

    class Meta:
        es_index_name = 'chicfood'
        es_type_name = 'food'
        es_mapping = {
            'properties': {
                'name': {'type': 'string', "analyzer": "trigrams"},
                'short_desc': {'type': 'string', "analyzer": "trigrams"},
            }
        }

    def es_repr(self):
        """
        Serializes the model instance into a dictionary
        """
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            config = self._meta.es_mapping['properties'][field_name]
            data[field_name] = getattr(self, field_name)
        return data


    def save(self, *args, **kwargs):
        """
        Overrides the save() function to update the ES index on save and create.
        """
        is_new = self.pk
        es_client = settings.ES_CLIENT
        super(Food, self).save(*args, **kwargs)
        payload = self.es_repr()
        del payload['_id']
        if is_new is not None:
            es_client.update(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body= payload
            )
        else:
            es_client.create(
                index=self._meta.es_index_name,
                doc_type=self._meta.es_type_name,
                id=self.pk,
                refresh=True,
                body= payload
            )

    def delete(self, *args, **kwargs):
        """
        Overrides the delete() function to update the ES index on delete.
        """
        prev_pk = self.pk
        es_client = settings.ES_CLIENT
        super(Food, self).delete(*args, **kwargs)
        es_client.delete(
            index=self._meta.es_index_name,
            doc_type=self._meta.es_type_name,
            id=prev_pk,
            refresh=True,
        )
