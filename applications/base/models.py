from django.db import models

from model_utils.models import TimeStampedModel

# Create your models here.
class Client(TimeStampedModel):

    OPTIONS = (
        (1, 'active'),
        (2, 'off'),
    )

    cli_id = models.AutoField("Key", primary_key=True)
    cli_name = models.CharField("name client", max_length=100)
    cli_mail = models.CharField("mail client", max_length=100)
    cli_fono1 = models.CharField("phone one client", max_length=100)
    cli_fono2 = models.CharField("phone two client", max_length=100)
    cli_status = models.IntegerField("status client", choices=OPTIONS, default=0)
    cli_image = models.TextField("image client", null=True, blank=True)
    cli_color1 = models.CharField("color one client", max_length=25)
    cli_color2 = models.CharField("color two client", max_length=25)
    cli_nombre_bd = models.CharField('name data base', max_length=100)
    cli_link = models.CharField("Link base", max_length=255, default='')

    def __int__(self):
        return self.cli_id

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)

    class Meta:
        db_table = 'base_client'
        ordering = ['cli_id']