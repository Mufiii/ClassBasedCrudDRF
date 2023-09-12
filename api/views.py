from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .serializers import FootballSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import *
import io
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class FootballApi(View):
  def get(self,request,*args,**kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    print(stream)
    pythondata = JSONParser().parse(stream)
    print(pythondata)
    id = pythondata.get('id', None)
    print(id)
    if id is not None :
        stu = Football.objects.get(id=id)
        serializer = FootballSerializer(stu)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='appliction/json')
    
    stu = Football.objects.all()
    serializer = FootballSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='appliction/json')
  
  
  def post(self,request,*args,**kwargs):
    if request.method == 'POST':
      json_data = request.body
      stream = io.BytesIO(json_data)
      pythondata = JSONParser().parse(stream)
      serializer = FootballSerializer(data = pythondata)
      if serializer.is_valid():
          Football.objects.create(
            name = serializer.validated_data.get('name'),
            roll = serializer.validated_data.get('roll'),
            city = serializer.validated_data.get('city')
          )
          res = { 'msg': 'Data is Created'}
          json_data = JSONRenderer().render(res)
    else :
        json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data , content_type='application/json')
  
  def update(self,request,*args,**kwargs):
    if request.method == 'PUT':
      json_data = request.body
      print(json_data)
      stream = io.BytesIO(json_data)
      pythondata = JSONParser().parse(stream)
      id = pythondata.get('id')
      print(id)
      stu = Football.objects.get(id=id)
      print(stu)
      serializer = FootballSerializer(stu, data=pythondata)
      print(serializer)
      if serializer.is_valid():
          serializer.save()
          res = {'msg': 'data is Updated'}
          json_data = JSONRenderer().render(res)
          print(json_data)
          print(serializer.data)
          return HttpResponse(json_data, content_type='application/json')
    print(serializer.errors)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data , content_type='application/json')
  
  def delete(self,request,*args,**kwargs):
    if request.method == 'DELETE':
      json_data = request.body
      stream = io.BytesIO(json_data)
      pythondata = JSONParser().parse(stream)
      id = pythondata.get('id')
      stu = Football.objects.get(id=id)
      stu.delete()
      res = {'msg': 'Data Deleted '}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
   