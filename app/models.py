from django.db import models
from django.conf import settings
from django.utils import timezone


# テーブルを作成 投稿者が削除されたら記事も削除される
class Post(models.Moldel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")

    def __str__(self):
        return self.title
