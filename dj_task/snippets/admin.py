from django.contrib import admin
from snippets.models import Snippet,Task#Product,Task
# Register your models here.

#admin.site.register(Product)
admin.site.register(Task)
admin.site.register(Snippet)