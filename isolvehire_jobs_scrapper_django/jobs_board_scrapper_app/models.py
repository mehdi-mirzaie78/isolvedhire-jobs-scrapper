from django.db import models
from django.utils.translation import gettext_lazy as _


from model_utils.models import TimeStampedModel, SoftDeletableModel
# Create your models here.

class Job(TimeStampedModel):
    url = models.URLField(verbose_name=_("URL"), unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    location = models.CharField(verbose_name=_("Location"), max_length=255, blank=True, null=True)
    pay = models.CharField(verbose_name=_("Pay"), max_length=255, blank=True, null=True)
    pay_type = models.CharField(verbose_name=_("Pay Type"), max_length=255, blank=True, null=True)
    employment_type = models.CharField(
        verbose_name=_("Employment Type"), max_length=255, blank=True, null=True)
    job_benefits = models.CharField(
        verbose_name=_("Job Benefits"), max_length=255, blank=True, null=True)
    job_description = models.TextField(verbose_name=_("Job Description"), blank=True, null=True)

    class Meta:
        ordering = ('-modified', '-pay')
    def __str__(self) -> str:
        return f"{self.title} #{(self.url.split('/')[-1]).split('.html')[0]}"