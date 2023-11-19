from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["title","slug","author","publish","status"]
    list_filter=["status","publish","author"]#filterできる変数#このままだとstatusは表示名では検索できない。dbには二文字短縮形でいれているから
    search_fields=["status","title"]#auhroで検索試合場合は？？？？
    raw_id_fields=["author"]
    prepopulated_fields={"slug":("title",)}