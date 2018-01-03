from django.contrib import admin

from CQATest.models import *
admin.site.register([Catagory,Tag,Question])
# admin.site.register(Question)
# admin.site.register(Catagory)
# admin.site.register(Tag)