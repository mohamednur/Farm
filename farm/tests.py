from django.test import TestCase
from farm.models import Produce, Fertilizer, Crops, FarmMachinery, FinancialRecords


class FertilizerTestCase(TestCase):

    def setUp(self):
        Fertilizer.objects.create(fname="Fertilizer1",)
        Fertilizer.objects.create(fname="Fertilizer2")

    def test_fertilzer_name(self):
        Fertilizer1 = Fertilizer.objects.get(fname="Fertilizer1")
        Fertilizer2 = Fertilizer.objects.get(fname="Fertilizer2")

# Create your tests here.
