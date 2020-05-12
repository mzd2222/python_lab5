from django.db import models


# Create your models here.

class Dictionaries(models.Model):
    spell = models.CharField(max_length=200, primary_key=True)    # 拼写
    tp = models.CharField(max_length=200, default='#')        # 词类型
    chinese = models.TextField()  # 中文翻译
