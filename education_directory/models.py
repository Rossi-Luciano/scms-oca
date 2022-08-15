import os
from django.db import models
from django.utils.translation import gettext as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from core.models import CommonControlField
from .forms import EducationDirectoryForm, EducationDirectoryFileForm

from location.models import Location
from institution.models import Institution


class EducationDirectory(CommonControlField):
    class Meta:
        verbose_name_plural = _('Education Directory')

    title = models.CharField(_("Title"), max_length=255, null=False, blank=False)
    link = models.URLField(_("Link"), null=False, blank=False)
    description = models.TextField(_("Description"), max_length=255,
                                   null=True, blank=True)
    start_date = models.DateField(_("Start Date"), max_length=255,
                                  null=True, blank=True)
    end_date = models.DateField(_("End Date"), max_length=255,
                                  null=True, blank=True)
    start_time = models.TimeField(_("Start Time"), max_length=255,
                                  null=True, blank=True)
    end_time = models.TimeField(_("End Time"), max_length=255,
                                  null=True, blank=True)

    locations = models.ManyToManyField(Location, blank=True)
    institutions = models.ManyToManyField(Institution, blank=True)

    is_online = models.BooleanField(default=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        FieldPanel('description'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
        FieldPanel('locations'),
        FieldPanel('institutions'),
        FieldPanel('is_online'),
    ]
    base_form_class = EducationDirectoryForm

class EducationDirectoryFile(CommonControlField):
    class Meta:
        verbose_name_plural = _('Education Directory Upload')

    attachment = models.ForeignKey(
        'wagtaildocs.Document',
        verbose_name=_("Attachement"),
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    is_valid = models.BooleanField(_("Is valid?"), default=False, blank=True,
                                   null=True)
    line_count = models.IntegerField(_("Number of lines"), default=0,
                                     blank=True, null=True)

    def filename(self):
        return os.path.basename(self.attachment.name)

    panels = [
        DocumentChooserPanel('attachment')
    ]
    base_form_class = EducationDirectoryFileForm
