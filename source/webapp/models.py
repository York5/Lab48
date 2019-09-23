from django.db import models
OTHER = 'other'
CATEGORY_CHOICES = [(OTHER, 'Other'), ('electronics', 'Electronic goods', ), ('books', 'Books'), ('automotive', 'Automotive'),
                    ('fashion', 'Fashion goods'), ('sports', 'Sports and Outdoors'), ('toys', 'Toys and games')]


class Good(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    category = models.CharField(max_length=40, null=False, blank=False, verbose_name='Category',
                                default=OTHER, choices=CATEGORY_CHOICES)
    stock = models.IntegerField(verbose_name='Left in Stock', default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name