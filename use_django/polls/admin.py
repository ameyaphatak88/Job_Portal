
from django.contrib import admin

from .models import Person

class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'city']

admin.site.register(Person, QuestionAdmin)
