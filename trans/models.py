from distutils.text_file import TextFile
from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

class MyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200,null=True,blank=True),
        content = models.TextField(max_length=400,null=True,blank=True),
        editor = RichTextField('Advance content',null=True,blank=True)
    )

    def __unicode__(self):
        return self.title
# Create your models here.
