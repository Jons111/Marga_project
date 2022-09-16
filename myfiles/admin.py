from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)

class AdminPro(admin.ModelAdmin):
    list_display = ['id','nomi','tur','manzil','rasm','vaqt']

admin.site.register(Project,AdminPro)


class AdminM(admin.ModelAdmin):
    list_display = ['id','ism','fam','mail','matn','vaqt']

admin.site.register(Messagelar,AdminM)