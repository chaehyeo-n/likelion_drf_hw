from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=50)     # 가수 설명
    debut = models.DateField()       # 데뷔일자

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
    release = models.DateField()     # 출시일
    content = models.TextField(max_length=200)     # 노래 설명