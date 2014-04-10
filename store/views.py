from django.http import HttpResponse
from django.shortcuts import render
from store.models import appClass

def index(request):
	return HttpResponse("Hello,world.")

def appclass(request):
	acp = dict()
	acp[1] = "/templates/appstore/images/mail.png"
	acp[2] = "/templates/appstore/images/settings.png"
	acp[3] = "/templates/appstore/images/phone.png"
	acp[4] = "/templates/appstore/images/gallery.png"
	acp[5] = "/templates/appstore/images/music.png"
	acp[6] = "/templates/appstore/images/firefox.png"
	acp[7] = "/templates/appstore/images/yahoo.png"
	acp[8] = "/templates/appstore/images/gmail.png"
	acp[9] = "/templates/appstore/images/facebook.png"
	acp[10] = "/templates/appstore/images/winamp.png"
	acp[11] = "/templates/appstore/images/tasks.png"
	acp[12] = "/templates/appstore/images/deviantart.png"
	acp[13] = "/templates/appstore/images/dribbble.png"
	appclasses = appClass.objects.order_by('id')[:5]
	return render(request, 'index.html', {'appclasses':appclasses,'acp':acp})
