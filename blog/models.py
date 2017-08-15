from django.db import models
from category.models import Category

from django.core.urlresolvers import reverse

# Create your models here.

class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                related_name="posts")
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, 
            null=True,
            help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=500, 
        default='Nothing', blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT', default='Nothing')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def det_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
