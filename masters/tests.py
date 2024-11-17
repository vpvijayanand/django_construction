# masters/tests.py
from django.test import TestCase
from .models import EmployeeType, VendorType

class EmployeeTypeTestCase(TestCase):
    def setUp(self):
        self.employee_type = EmployeeType.objects.create(name="Full-time")

    def test_employee_type_str(self):
        self.assertEqual(str(self.employee_type), "Full-time")

class VendorTypeTestCase(TestCase):
    def setUp(self):
        self.vendor_type = VendorType.objects.create(name="Supplier")

    def test_vendor_type_str(self):
        self.assertEqual(str(self.vendor_type), "Supplier")
