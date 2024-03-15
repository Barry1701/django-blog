from django.contrib import admin
from .models import About
form django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields - ('content',)