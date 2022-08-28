from django.contrib import admin
from trans.models import MyModel
from parler.admin import TranslatableAdmin
# Register your models here.
admin.site.register(MyModel, TranslatableAdmin)