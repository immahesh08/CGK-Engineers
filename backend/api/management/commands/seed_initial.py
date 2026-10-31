from django.core.management.base import BaseCommand
from api.models import Category, Product, Service, CompanyInformation

class Command(BaseCommand):
    help = "Create initial CGK sample content"

    def handle(self, *args, **kwargs):
        cats = ["Air Conditioners","VRF Systems","Chillers","Lighting","Street Lighting","High Mast Lighting","Solar Lighting"]
        for name in cats: Category.objects.get_or_create(name=name, defaults={"slug": name.lower().replace(" ","-")})
        services = ["HVAC Installation","AC Installation","VRF Installation","Chiller Installation","HVAC Maintenance","AC Repair","Ducting Work","Lighting Installation"]
        for title in services: Service.objects.get_or_create(title=title, defaults={"slug": title.lower().replace(" ","-"), "short_description": "Professional engineering and support service."})
        company = CompanyInformation.objects.first()
        if not company: CompanyInformation.objects.create()
        self.stdout.write(self.style.SUCCESS("Initial CGK content created."))
