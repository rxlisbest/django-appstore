from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from store.models import appspic
from store.models import appClass
from store.models import apps
from store.models import size 
from django.db import connection 

def dictfetchall(cursor):
	desc = cursor.description
	return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

def index(request):
	return HttpResponse("Hello,world.")

def appclass(request):
	acp = dict()
	
	cursor = connection.cursor()
	sql = "SELECT *,store_appclass.id as c_id FROM store_appclass LEFT JOIN store_appspic ON store_appspic.id=store_appclass.p_id LEFT JOIN store_size ON store_size.id=store_appspic.s_id"
	cursor.execute(sql)
	classes = dictfetchall(cursor)
	return render(request, 'index.html', {'classes':classes})

def app(request, c_id):
	acp = dict()
	
	cursor = connection.cursor()
	sql = "SELECT * FROM store_apps LEFT JOIN store_appspic ON store_appspic.id=store_apps.p_id LEFT JOIN store_size ON store_size.id=store_appspic.s_id WHERE c_id = %s" % c_id
	cursor.execute(sql)
	apps = dictfetchall(cursor)
	return render(request, 'app.html', {'apps':apps})

