from enum import unique
from django.db import models

class Wilayah(models.Model):
    nama = models.CharField(max_length=50)

    class Meta:
        db_table = 'wilayah'
        verbose_name = 'Wilayah'
        verbose_name_plural = 'Wilayah'

    def __str__(self):
        return '{}'.format(self.nama)

    def save(self, *args, **kwargs):
        self.nama = self.nama.upper()

        return super(Wilayah, self).save()


class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    nia = models.CharField(max_length=20)
    wilayah = models.ForeignKey(
        Wilayah,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'anggota'
        verbose_name = 'jemaat'
        verbose_name_plural = 'jemaat'

    def __str__(self):
        return '{}'.format(self.nama)

    def save(self, *args, **kwargs):
        self.nama = self.nama.upper()
        self.nia = self.nia.upper()
        return super(Anggota, self).save()


class Pengusul(models.Model):
    anggota = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Anggota',
        related_name='pengusul'
    )
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    penatua_1 = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Usulan Penatua Pertama',
        related_name='penatua_alasan_1'
    )
    penatua_alasan_1 = models.TextField(blank=True, null=True)
    penatua_mobile_1 = models.CharField(max_length=20, blank=True, null=True)

    penatua_2 = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Usulan Penatua Kedua',
        blank=True,
        null=True,
        related_name='penatua_alasan_2'
    )
    penatua_alasan_2 = models.TextField(blank=True, null=True)
    penatua_mobile_2 = models.CharField(max_length=20, blank=True, null=True)

    penatua_3 = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Usulan Penatua Ketiga',
        blank=True,
        null=True,
        related_name='penatua_alasan_3'
    )
    penatua_alasan_3 = models.TextField(blank=True, null=True)
    penatua_mobile_3 = models.CharField(max_length=20, blank=True, null=True)

    penatua_4 = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Usulan Penatua Keempat',
        blank=True,
        null=True,
        related_name='penatua_alasan_4'
    )
    penatua_alasan_4 = models.TextField(blank=True, null=True)
    penatua_mobile_4 = models.CharField(max_length=20, blank=True, null=True)

    penatua_5 = models.ForeignKey(
        Anggota,
        on_delete=models.CASCADE,
        verbose_name='Usulan Penatua Kelima',
        blank=True,
        null=True,
        related_name='penatua_alasan_5'
    )
    penatua_alasan_5 = models.TextField(blank=True, null=True)
    penatua_mobile_5 = models.CharField(max_length=20, blank=True, null=True)

    konfirmasi = models.BooleanField(default=False)

    class Meta:
        db_table = 'pengusul'
        verbose_name = 'pengusul'
        verbose_name_plural = 'pengusul'

    def __str__(self):
        return '{}'.format(self.anggota)

