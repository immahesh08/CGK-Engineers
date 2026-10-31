from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = Category; fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta: model = ProductImage; fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    gallery = ProductImageSerializer(many=True, read_only=True)
    class Meta: model = Product; fields = "__all__"; read_only_fields = ["created_at","updated_at"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta: model = Service; fields = "__all__"

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta: model = ProjectImage; fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    gallery = ProjectImageSerializer(many=True, read_only=True)
    class Meta: model = Project; fields = "__all__"

class GallerySerializer(serializers.ModelSerializer):
    class Meta: model = Gallery; fields = "__all__"

class EnquirySerializer(serializers.ModelSerializer):
    class Meta: model = Enquiry; fields = "__all__"; read_only_fields = ["status","created_at","updated_at"]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta: model = ContactMessage; fields = "__all__"; read_only_fields = ["is_read","created_at","updated_at"]

class CompanyInformationSerializer(serializers.ModelSerializer):
    class Meta: model = CompanyInformation; fields = "__all__"
