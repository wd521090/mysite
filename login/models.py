# Create your models here.

from django.db import models


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)  # name:必填，最长不超过128个字符，唯一
    password = models.CharField(max_length=256)  # password:必填，最长不超过256个字符
    email = models.EmailField(unique=True)  # email:使用Django内置的邮箱类型，唯一
    sex = models.CharField(max_length=32, choices=gender, default="男")  # sex:性别，使用一个choice，只能选择男或女；默认为男
    c_time = models.DateTimeField(auto_now_add=True)

    # 帮助人性化显示对象信息
    def __str__(self):
        return self.name

    # 定义用户按创建时间的反序排列
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
