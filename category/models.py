from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
            help_text='one word for title alias')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_category'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', args=(self.slug,))
