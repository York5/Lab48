from django.db import models

STATUS_CHOICES = (('Electronics', 'Electronic goods'), ('Books', 'Books'), ('Automotive', 'Automotive'),
                  ('Fashion', 'Fashion goods'), ('Sports', 'Sports and Outdoors'), ('Toys', 'Toys and games'),
                  ('Other', 'Other'))


class Good(models.Model):
    title = models.TextField(max_length=100, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    category = models.CharField(max_length=40, null=False, blank=False, verbose_name='Status',
                                default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    stock = models.IntegerField(verbose_name='Stock')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.title