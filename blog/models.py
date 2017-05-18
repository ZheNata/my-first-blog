from django.db import models
from django.utils import timezone

#наш объект - класс Записи в блоге
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#метод публикации поста в блоге
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#после вызова этого метода получаем текст (строку) с загом записи
    def __str__(self):
        return self.title
