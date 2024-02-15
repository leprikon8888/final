from django.db import models


class ServiceBlock(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блока сервисов')
    description = models.TextField(verbose_name='Описание блока сервисов')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


# Create your models here.
class Service(models.Model):
    service_block = models.ForeignKey(ServiceBlock, on_delete=models.CASCADE, related_name='services',
                                      verbose_name='Блок сервисов')
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=800, unique=True)
    icon = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('position',)


class PortfolioBlock(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блока сервисов')
    description = models.TextField(verbose_name='Описание блока сервисов')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Portfolio(models.Model):
    portfolio_block = models.ForeignKey(PortfolioBlock, on_delete=models.CASCADE, related_name='services',
                                      verbose_name='Блок сервисов')
    name = models.CharField(max_length=60, unique=True)
    short_description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=800)
    is_visible = models.BooleanField(default=True)
    date = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    category_service = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='portfolio', blank=True)



class AboutBlock(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блока ')
    description = models.TextField(verbose_name='Описание блока ')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class AboutUnit(models.Model):
    about_block = models.ForeignKey(AboutBlock, on_delete=models.CASCADE, related_name='services',
                                      verbose_name='Блок сервисов')
    name = models.CharField(max_length=50, unique=True)
    date = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=800, unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='about', blank=True)


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    job_title = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    instagram = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='team/', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Team'
        ordering = ('position',)


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='client/', blank=True)

    def __str__(self):
        return f'{self.name}'


class Shapka(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField(default=1, unique=True)
    is_visible = models.BooleanField(default=True)


class BrandName(models.Model):
    name = models.CharField(max_length=100, verbose_name="ім'я бренду")
    is_visible = models.BooleanField(default=True)


class BrandFace(models.Model):
    h1 = models.CharField(max_length=60, unique=True)
    h2 = models.CharField(max_length=60, unique=True)
    button_name = models.CharField(max_length=60, unique=True)
    photo = models.ImageField(upload_to='face/', blank=True)

