from django.db import models


class Books(models.Model):
    title = models.CharField('Название', max_length=50)
    name_author = models.CharField('Имя автора', max_length=50)
    date = models.DateField('Дата выхода')
    count_page = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
# Create your models here.
