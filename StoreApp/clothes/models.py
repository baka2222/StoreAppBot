from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40,
                            verbose_name='Название категории')
    
    def __str__(self):
        return f'{self.name}'
    


class Clothes(models.Model):
    img = models.ImageField(verbose_name='название картинки')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='clothes',
                                 verbose_name='Название одежды')