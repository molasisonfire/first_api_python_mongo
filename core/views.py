from django.shortcuts import render
from django.http import JsonResponse
import requests
import pymongo

from pymongo import MongoClient


# Create your views here.
def test_view(request):
    data = {
        'name' : 'john',
        'age' : 23
    }
    return JsonResponse(data)

def test_call(request):
    r = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')
    json_object = r.json()
    #cluster = MongoClient('mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb');
    #db = cluster["db"];
    #collection = db["Transacoes"];
    #collection.insert_one(json_object);
    return JsonResponse(json_object)
