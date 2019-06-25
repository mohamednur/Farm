from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.IntegerField()

    def __str__(self):
        return self.mobile_no


class Crops(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s ' % (self.name)


class Fertilizer(models.Model):
    fname = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    used_for_crop = models.ForeignKey(Crops, on_delete=models.CASCADE)


class Produce(models.Model):
    from_crop = models.ForeignKey(Crops, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_submitted = models.DateField()

    def __str__(self):
        return '%s %d %s' % (self.from_crop, self.quantity, self.submitted_by)


class Seed(models.Model):
    seed_name = models.CharField(max_length=30)


class FinancialRecords(models.Model):
    receipt_no = models.CharField(max_length=30, unique=True)
    Amount = models.FloatField()
    date_of_payment = models.DateTimeField()


class FarmMachinery(models.Model):
    MACHINERY_TYPE = (
        ('TR', 'Tractors'),
        ('CO', 'Combines'),
        ('PL', 'Planters'),
        ('MO', 'Mowers'),
        ('SP', 'Sprayers'),
        ('PO', 'Plows'),
    )

    MACHINERY_STATUS = (
        ('AV', 'Available'),
        ('IM', 'In Maintenance')

    )

    machinery_type = models.CharField(max_length=2, choices=MACHINERY_TYPE)
    name = models.CharField(max_length=60)
    identification_no = models.CharField(max_length=20)
    status = models.CharField(max_length=2, choices=MACHINERY_STATUS)
    last_serviced = models.DateField()
    date_of_purchase = models.DateField()

    def machinery_type_verbose(self):
        return dict(FarmMachinery.MACHINERY_TYPE)[self.machinery_type]

    def machinery_status_verbose(self):
        return dict(FarmMachinery.MACHINERY_STATUS)[self.status]
