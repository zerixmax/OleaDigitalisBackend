from django.db import models

class Maslina(models.Model):
    naziv = models.CharField(max_length=100)
    qr_kod = models.CharField(max_length=100, unique=True)
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    datum_unosa = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naziv} ({self.qr_kod})"
