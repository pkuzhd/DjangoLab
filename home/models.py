from django.db import models

class Teacher(models.Model):

    class Meta:
        verbose_name="教师"
        verbose_name_plural="教师"

    name = models.CharField(max_length=200, verbose_name="姓名")
    uid = models.CharField(max_length=10, verbose_name="工作证号")
    perm = models.IntegerField(default=0, verbose_name="权限") # web permissions

    def __str__(self):
        return "{name}({uid})".format(name=self.name, uid=self.uid)
