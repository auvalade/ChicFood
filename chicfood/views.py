from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.conf import settings
 
from .models import Food
from .forms import LoginForm, AddFoodForm

def index(request):
    response = {}
    all_food = Food.objects.all()
    response['all_food'] = all_food
    return render(request, 'index.html', response)

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def loginpage(request):
    response = {}
    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user) 
            else: 
                error = True
    else:
        form = LoginForm()

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse(index))
    
    response['error'] = error
    response['form'] = form
    return render(request, 'login.html', response)

def addfood(request):
    response = {}
    error = False

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(loginpage))

    if request.method == "POST":
        form = AddFoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            short_desc = form.cleaned_data["short_desc"]
            healthy_level = form.cleaned_data["healthy_level"]
            taste_level = form.cleaned_data["taste_level"]
            quantity = form.cleaned_data["quantity"]
            price = form.cleaned_data["price"]
            Food.objects.create(name=name, short_desc=short_desc, healthy_level=healthy_level, taste_level=taste_level, quantity=quantity, price=price)   
            return HttpResponseRedirect(reverse(index))
        else:
            error = True
    else:
        form = AddFoodForm()

    response['error'] = error 
    response['form'] = form
    return render(request, 'add.html', response)

def searchpage(request):
    response = {}
    all_food = []
    total_results= 0
    client = settings.ES_CLIENT
    query = request.GET.get('q','')

    if query:
    #    body = {"query": {"match": {'name':query}}}
        body = {"query":{ "bool": {  "should": [
                { "match": { "name": query }},
                { "match": { "short_desc": query }}
            ]}}}
    else: 
        body = {"query":{'match_all': {}}}
    search_result = client.search(index='chicfood', doc_type='food', body=body)
    
    for hit in search_result['hits']['hits']:
        current_food = Food.objects.get(pk=hit['_id'])
        all_food.append(current_food)

    if search_result['hits']['total']:
        total_results = search_result['hits']['total']

    response['total_results'] = total_results
    response['all_food'] = all_food
    return render(request, 'search.html', response)
