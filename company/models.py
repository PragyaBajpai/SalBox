from django.db import models
from django.db.models.base import Model

# Create your models here.
class Company(models.Model):
    """Model definition for Company."""

    # TODO: Define fields here
    name = models.CharField(blank=False,null=False, max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        """Unicode representation of Company."""
        return '{}'.format(self.name ) # TODO

class Employee(models.Model):
    """Model definition for Employee."""

    CompanyInfo = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    name = models.CharField(blank=False,null=False, max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of Employee."""
        return '{}'.format(self.name )
