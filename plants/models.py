from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Plant(models.Model):
    name = models.CharField(max_length=100, verbose_name="植物名称")
    scientific_name = models.CharField(max_length=100, verbose_name="学名")
    description = models.TextField(verbose_name="描述")
    care_instructions = models.TextField(verbose_name="养护说明")
    light_requirements = models.CharField(max_length=50, verbose_name="光照需求")
    water_frequency = models.CharField(max_length=50, verbose_name="浇水频率")
    difficulty_level = models.CharField(max_length=20, verbose_name="难度等级")
    created_at = models.DateTimeField('创建时间', default=timezone.now)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    image = models.ImageField('植物图片', upload_to='plants/', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "植物"
        verbose_name_plural = "植物"

class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='植物')
    nickname = models.CharField('昵称', max_length=100, blank=True)
    acquired_date = models.DateField('获得日期')
    last_watered = models.DateField('最后浇水日期', null=True, blank=True)
    notes = models.TextField('个人笔记', blank=True)
    created_at = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        verbose_name = '用户植物'
        verbose_name_plural = '用户植物'

    def __str__(self):
        return f"{self.user.username}的{self.plant.name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='植物')
    content = models.TextField('评论内容')
    created_at = models.DateTimeField('创建时间', default=timezone.now)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return f"{self.user.username}对{self.plant.name}的评论" 