from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","is_active","created_at")
    search_fields = ("name","description")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","brand","is_featured","is_active","created_at")
    search_fields = ("name","brand","short_description")
    list_filter = ("category","brand","is_featured","is_active")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product","alt_text","created_at")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title","is_featured","is_active","created_at")
    search_fields = ("title","short_description")
    list_filter = ("is_featured","is_active")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","category","client_name","location","completion_date","is_featured")
    search_fields = ("title","client_name","location")
    list_filter = ("category","is_featured")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(ProjectImage)
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title","category","project","created_at")
    search_fields = ("title","category","description")
    list_filter = ("category",)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name","phone","product","service","status","created_at")
    search_fields = ("name","company_name","phone","email","requirement")
    list_filter = ("status","created_at")
    list_editable = ("status",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name","email","subject","is_read","created_at")
    search_fields = ("name","email","subject","message")
    list_filter = ("is_read","created_at")
    list_editable = ("is_read",)

@admin.register(CompanyInformation)
class CompanyInformationAdmin(admin.ModelAdmin):
    list_display = ("company_name","phone","email","city","established_year","updated_at")
    search_fields = ("company_name","phone","email","city")
