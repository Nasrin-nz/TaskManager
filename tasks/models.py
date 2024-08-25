from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Mission(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'ایجاد شده'),
        ('IN_PROGRESS', 'در حال انجام'),
        ('COMPLETED', 'تمام شده'),
        ('CANCELED', 'کنسل شده'),
    ]
    name = models.CharField(max_length=500, verbose_name="نام")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='CREATED', verbose_name="وضعیت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ماموریت"
        verbose_name_plural = "ماموریت‌ها"


class Project(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'ایجاد شده'),
        ('IN_PROGRESS', 'در حال انجام'),
        ('COMPLETED', 'تمام شده'),
        ('CANCELED', 'کنسل شده'),
        ('COMPLETED_WITHOUT_RESULT', 'تمام شده بدون نتیجه'),
    ]
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, verbose_name="ماموریت")
    name = models.CharField(max_length=500, verbose_name="نام")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"


class Task(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'ایجاد شده'),
        ('IN_PROGRESS', 'در حال انجام'),
        ('COMPLETED', 'تمام شده'),
        ('CANCELED', 'کنسل شده'),
        ('WAITING', 'منتظر'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="پروژه")
    referring_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر ارجاع دهنده", related_name='referring_tasks')
    registration_time = jmodels.jDateTimeField(verbose_name="زمان ثبت")
    responsible_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر مسئول کار", related_name='responsible_tasks')
    deadline = jmodels.jDateTimeField(verbose_name="ددلاین")
    task_title = models.CharField(max_length=500, verbose_name="عنوان وظیفه")
    description = models.TextField(verbose_name="توضیحات")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="وضعیت")


    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = "وظیفه"
        verbose_name_plural = "وظایف"


class Action(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="وظیفه")
    registering_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر ثبت کننده")
    registration_time = jmodels.jDateTimeField(verbose_name="زمان ثبت")
    action_description = models.TextField(verbose_name="شرح اقدام")
    attachment = models.FileField(upload_to='documents/', verbose_name="پیوست")


    def __str__(self):
        return f"{self.task} - {self.registering_user.username}"

    class Meta:
        verbose_name = "اقدام"
        verbose_name_plural = "اقدامات"


class Referral(models.Model):
    referring_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر ارجاع دهنده", related_name='referrals_made')
    receiving_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر ارجاع گیرنده", related_name='referrals_received')
    registration_time = jmodels.jDateTimeField(verbose_name="زمان ثبت")
    referral_description = models.TextField(verbose_name="توضیح ارجاع")


    def __str__(self):
        return  f"{self.referring_user.username} to {self.receiving_user.username}"

    class Meta:
        verbose_name = "ارجاع"
        verbose_name_plural = "ارجاعات"
