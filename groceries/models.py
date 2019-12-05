from django.db import models
from home.models import Teacher

class Items(models.Model):

    class Meta:
        verbose_name="设备"
        verbose_name_plural="设备"

    name = models.CharField(max_length=200, verbose_name="设备名称")
    serial = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    position = models.CharField(max_length=20, verbose_name="位置")
    status = models.IntegerField(default=0, verbose_name="状态")
    note = models.CharField(max_length=200, verbose_name="备注")
    owner = models.ForeignKey(Teacher, on_delete = models.CASCADE, verbose_name="所有者")

    def __unicode__(self):
        return "(__unicode__)"+self.name

    def __str__(self):
        return "(__str__){name}({owner})".format(name=self.name, owner=self.owner)

class History(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    date = models.DateTimeField('Borrow Date')
    tel = models.CharField(max_length=20)
    note = models.CharField(max_length=200)
    back = models.DateTimeField('Return Date', blank=True, null=True)
