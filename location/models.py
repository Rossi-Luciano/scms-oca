from django.db import models
from django.utils.translation import gettext as _
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable

from core.models import CommonControlField
from usefulmodels.models import City, Country, State

from . import choices
from .forms import LocationForm


class Location(CommonControlField):
    region = models.CharField(_("Region"), choices=choices.regions, max_length=255, null=True, blank=True)

    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.CASCADE,
                             null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_("State"), on_delete=models.CASCADE,
                              null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.CASCADE,
                                null=True, blank=True)

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __unicode__(self):
        return u'%s: %s | %s: %s | %s: %s | %s: %s' % (_('Country'), self.country, _('Region'), self.region, _('State'),  self.state, _('City'), self.city, )

    def __str__(self):
        return u'%s: %s | %s: %s | %s: %s | %s: %s' % (_('Country'), self.country, _('Region'), self.region, _('State'),  self.state, _('City'), self.city, )

    @classmethod
    def get_or_create(cls, location_country, location_region, location_state,
                      location_city, user):

        # check if exists the location
        if cls.objects.filter(country__name=location_country, region=location_region, state__name=location_state, city__name=location_city).exists():
            return cls.objects.get(
                country__name=location_country, region=location_region, state__name=location_state, city__name=location_city)
        else:
            location = location()
            location.region = location_region
            location.country = location_country
            location.state = location_state
            location.city = location_city
            location.creator = user
            location.save()

        return location


    base_form_class = LocationForm
