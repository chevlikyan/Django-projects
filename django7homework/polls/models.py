from django.db import models

# Create your models here.
STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Category(models.Model):
    """Category model"""

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class News(TimeStampedModel):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='categories')
    additional_category = models.ManyToManyField(Category,
                                                 blank=True,
                                                 related_name='additional_categories')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='news')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
