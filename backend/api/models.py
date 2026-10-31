from django.db import models
from django.utils.text import slugify

class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(TimeStamped):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self): return self.name

class Product(TimeStamped):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    name = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    features = models.JSONField(default=list, blank=True)
    specifications = models.JSONField(default=dict, blank=True)
    applications = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self): return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="products/gallery/")
    alt_text = models.CharField(max_length=180, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Service(TimeStamped):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    features = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title

class Project(TimeStamped):
    CATEGORY_CHOICES = [(x, x) for x in ["HVAC","VRF","Chiller","AC Installation","Electrical","Lighting"]]
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    client_name = models.CharField(max_length=180, blank=True)
    location = models.CharField(max_length=180, blank=True)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    completion_date = models.DateField(blank=True, null=True)
    featured_image = models.ImageField(upload_to="projects/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=180, blank=True)

class Gallery(TimeStamped):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="gallery/")
    category = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name="gallery_items")

class Enquiry(TimeStamped):
    STATUS_CHOICES = [(x, x) for x in ["New","Contacted","In Progress","Quoted","Closed"]]
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=180, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=180, blank=True)
    requirement = models.TextField(blank=True)
    preferred_contact_method = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="New")

class ContactMessage(TimeStamped):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

class CompanyInformation(TimeStamped):
    company_name = models.CharField(max_length=180, default="CGK Engineers & Consultants")
    tagline = models.CharField(max_length=300, default="Complete HVAC & Electrical Solutions for Modern Spaces")
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="company/", blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    whatsapp = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=250, default="Tatibandh, Raipur, Chhattisgarh - 492001, India")
    city = models.CharField(max_length=100, default="Raipur")
    state = models.CharField(max_length=100, default="Chhattisgarh")
    pincode = models.CharField(max_length=10, default="492001")
    google_maps_url = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    established_year = models.PositiveIntegerField(default=2012)
    employees = models.PositiveIntegerField(default=0)
    business_hours = models.CharField(max_length=200, blank=True)
    def __str__(self): return self.company_name
