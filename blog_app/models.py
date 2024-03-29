from django.db                  import models
from django.db.models.query     import QuerySet
from django.utils               import timezone
from django.contrib.auth.models import User
from django.urls                import reverse

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset() \
                      .filter(status = Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT     = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    title   = models.CharField(max_length = 200)
    slug    = models.SlugField(max_length = 250,
                               unique_for_date = 'publish')
    author  = models.ForeignKey(User,
                                on_delete    = models.CASCADE,
                                related_name = 'blog_posts')
    body    = models.TextField()
    publish = models.DateTimeField(default      = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now     = True)
    status  = models.CharField(max_length = 2,
                               choices    = Status.choices,
                               default    = Status.DRAFT)
    objects   = models.Manager() # менеджер, применяемый по умолчанию
    published = PublishedManager() # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_app:post_detail',
                       args = [self.publish.year,
                               self.publish.month,
                               self.publish.day,
                               self.slug])
