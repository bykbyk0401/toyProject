from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True

class Post(BaseModel):

    post_id = models.AutoField(primary_key=True)
    writer = models.CharField(verbose_name="작성자", max_length=30)
    content = models.TextField(verbose_name="내용")
    date = models.CharField(verbose_name="날짜", max_length=20, default='')
 

class Comment(BaseModel):
    writer = models.CharField(verbose_name="작성자", max_length=30)
    content = models.CharField(verbose_name="내용", max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, blank=False)