from django.contrib import admin
from .models import Puppy, PuppyImage

class PuppyImageInline(admin.TabularInline):
    model = Puppy.additional_images.through  # Many-to-many relation
    extra = 1  # Number of empty forms to display for additional images (optional)

class PuppyAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'description')
    search_fields = ('name', 'breed')
    list_filter = ('breed',)
    inlines = [PuppyImageInline]  # Adding the PuppyImageInline to display additional images

admin.site.register(Puppy, PuppyAdmin)
admin.site.register(PuppyImage)
