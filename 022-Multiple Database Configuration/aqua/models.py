from django.db import models
from django.utils.translation import gettext_lazy as _

class Aqua(models.Model):
    title = models.CharField(_("title"), max_length=50)
    content = models.CharField(_("content"), max_length=50)
    app_name = models.CharField(_("app name"), max_length=50)

    def __str__(self):
        return self.title