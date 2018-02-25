# encoding:utf-8
from django.db import models
from django.utils import timezone

class RegisterTable(models.Model):
    # 姓名
    name = models.CharField(default='', max_length=45)
    # 性别
    sex = models.CharField(default='', max_length=4)
    # 民族
    nation = models.CharField(default='', max_length=45)
    # 电话
    phone = models.CharField(default='', max_length=11)
    # email
    email = models.CharField(default='', max_length=45)
    # qq
    qq = models.CharField(default='', max_length=13)
    # 爱好
    hobby = models.CharField(default='', max_length=45)
    # 宿舍地址
    address = models.CharField(default='', max_length=45)
    # 学生组织
    organization = models.CharField(default='', max_length=45)
    # 技术倾向
    tech = models.CharField(default='', max_length=45)
    # 部门
    apartment = models.CharField(default='', max_length=20)
    # 是否服从分配
    agree_to_allocation = models.IntegerField(default=0)
    # 期待
    await = models.TextField(default='')
    # 大学的计划
    plan = models.TextField(default='')
    # 自我评价
    assess = models.TextField(default='')
    # 发送时间
    time = models.DateTimeField( null=False,default=timezone.now )

    class Meta:
        ordering = ['-time',]
