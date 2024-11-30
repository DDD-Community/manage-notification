from django.db import models
from tinymce.models import HTMLField

class EmailTemplate(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="이메일 KEY ID")
    title = models.CharField(max_length=200, verbose_name="이메일 제목")
    body = HTMLField(verbose_name="이메일 본문")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    class Meta:
        verbose_name = "이메일 템플릿"
        verbose_name_plural = "이메일 템플릿"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title