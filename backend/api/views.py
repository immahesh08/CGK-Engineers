from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import *
from .serializers import *

class PublicModelViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

class CategoryViewSet(PublicModelViewSet):
    queryset = Category.objects.filter(is_active=True).order_by("name")
    serializer_class = CategorySerializer

class ProductViewSet(PublicModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related("category").prefetch_related("gallery").order_by("-is_featured","-created_at")
    serializer_class = ProductSerializer
    lookup_field = "slug"
    search_fields = ["name","brand","short_description"]
    filterset_fields = ["category","brand","is_featured"]
    ordering_fields = ["name","created_at"]

class ServiceViewSet(PublicModelViewSet):
    queryset = Service.objects.filter(is_active=True).order_by("-is_featured","title")
    serializer_class = ServiceSerializer
    lookup_field = "slug"
    search_fields = ["title","short_description"]

class ProjectViewSet(PublicModelViewSet):
    queryset = Project.objects.all().prefetch_related("gallery").order_by("-is_featured","-completion_date")
    serializer_class = ProjectSerializer
    lookup_field = "slug"
    filterset_fields = ["category"]
    search_fields = ["title","client_name","location"]

class GalleryViewSet(PublicModelViewSet):
    queryset = Gallery.objects.all().order_by("-created_at")
    serializer_class = GallerySerializer
    filterset_fields = ["category"]

class CompanyView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CompanyInformationSerializer
    def get_object(self):
        return CompanyInformation.objects.order_by("-updated_at").first()

class EnquiryCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EnquirySerializer
    queryset = Enquiry.objects.all()

class ContactCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()
