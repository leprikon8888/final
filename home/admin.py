# from django.contrib import admin
# from django.utils.safestring import mark_safe
#
# from .models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, \
#     Portfolio, PortfolioBlock
#
#
# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('photo_src_tag', 'name',  'date', 'is_visible', 'description', 'position',
#                     'date', 'client', 'category_service')
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ('name', 'date', 'is_visible', 'description', 'position', 'date', 'client',
#                      'category_service')
#
#     def photo_src_tag(self, obj):
#         if obj.photo:
#             return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")
#
#         photo_src_tag.short_description = 'Portfolio photo'
#
#
# @admin.register(PortfolioBlock)
# class PortfolioBlockAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# @admin.register(BrandName)
# class BrandNameAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'position', 'is_visible')
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ('name', 'position', 'is_visible')
#     list_filter = ('is_visible',)
#
#
# @admin.register(ServiceBlock)
# class ServiceBlockAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'is_visible', 'description',)
#     list_editable = ('name', 'is_visible', 'description',)
#
#
# @admin.register(AboutBlock)
# class AboutBlockAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'is_visible', 'description',)
#     list_editable = ('name', 'is_visible', 'description',)
#
#
# @admin.register(AboutUnit)
# class AboutUnitAdmin(admin.ModelAdmin):
#     list_display = ('photo_src_tag', 'name', 'date', 'is_visible', 'description', 'position', )
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ('name', 'date', 'is_visible', 'description', 'position')
#
#     def photo_src_tag(self, obj):
#         if obj.photo:
#             return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")
#
#         self.photo_src_tag.short_description = 'Aboutbnit photo'
#
#
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('photo_src_tag', 'name', 'job_title', 'is_visible', 'position', 'instagram', 'facebook', 'linkedin')
#     list_editable = ('name', 'job_title', 'is_visible', 'position', 'instagram', 'facebook', 'linkedin')
#
#     def photo_src_tag(self, obj):
#         if obj.photo:
#             return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")
#
#         self.photo_src_tag.short_description = 'Team photo'
#
#
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('photo_src_tag', 'name', 'is_visible', 'position')
#     list_editable = ('name', 'is_visible', 'position')
#
#     def photo_src_tag(self, obj):
#         if obj.photo:
#             return mark_safe(f"<img src='{obj.photo.url}' width=50")
#
#         self.photo_src_tag.short_description = 'Client photo'
#
#
# @admin.register(Shapka)
# class ShapkaAdmin(admin.ModelAdmin):
#     list_display = ('name', 'position', 'is_visible', )
#     prepopulated_fields = {'slug': ('name',)}
#     list_editable = ('is_visible', 'position')
#
#
# @admin.register(BrandFace)
# class BrandFaceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'h1', 'h2', 'button_name')
#     list_editable = ('h1', 'h2', 'button_name')


from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, Portfolio, PortfolioBlock


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'date', 'is_visible', 'description', 'position', 'client', 'category_service')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name', 'date', 'is_visible', 'description', 'position', 'client', 'category_service')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Portfolio photo'


@admin.register(PortfolioBlock)
class PortfolioBlockAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BrandName)
class BrandNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'is_visible')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name', 'position', 'is_visible')
    list_filter = ('is_visible',)


@admin.register(ServiceBlock)
class ServiceBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'description',)
    list_editable = ('name', 'is_visible', 'description',)


@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'description',)
    list_editable = ('name', 'is_visible', 'description',)


@admin.register(AboutUnit)
class AboutUnitAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'date', 'is_visible', 'description', 'position', )
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('name', 'date', 'is_visible', 'description', 'position')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Aboutunit photo'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'job_title', 'is_visible', 'position', 'instagram', 'facebook', 'linkedin')
    list_editable = ('name', 'job_title', 'is_visible', 'position', 'instagram', 'facebook', 'linkedin')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Team photo'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'is_visible', 'position')
    list_editable = ('name', 'is_visible', 'position')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Client photo'


@admin.register(Shapka)
class ShapkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_visible', )
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_visible', 'position')


@admin.register(BrandFace)
class BrandFaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'h1', 'h2', 'button_name')
    list_editable = ('h1', 'h2', 'button_name')
