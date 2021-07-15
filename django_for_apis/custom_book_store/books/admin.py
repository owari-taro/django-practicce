from django.contrib import admin
from django.db.models.fields.related import create_many_to_many_intermediary_model
from .models import Book, Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ["title", "author", "is_special"]


admin.site.register(Book, BookAdmin)
# admin.site.register(Comment)
