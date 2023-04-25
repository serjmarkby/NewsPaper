from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment, Subscription

# Register your models here.

# admin.site.register(Author)
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(PostCategory)
# admin.site.register(Comment)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("pk", "authorUser", "rating")
    list_filter = ("rating", )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "type", "date_create", "display_category", "title", "text", "rating")
    list_filter = ("author", "rating")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "category")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "authorUser", "text", "date_create", "rating")
    list_filter = ("authorUser", "post", "rating")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "category")
    list_filter = ("category", )




