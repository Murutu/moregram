from django.test import TestCase
from .models import Location



# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.place = Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.place.delete_location('Nairobi')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

