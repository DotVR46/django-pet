from django.contrib import admin
from news.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'tag_list', 'get_image']
    list_editable = ('category',)
    search_fields = ('title', 'category__title')
    readonly_fields = ('get_image',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
