from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment

# Register your models here.

# admin.site.register(Author)
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(PostCategory)
# admin.site.register(Comment)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("pk", "authorUser", "rating")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "type", "date_create", "title", "text", "rating")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "category")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "authorUser", "text", "date_create", "rating")




