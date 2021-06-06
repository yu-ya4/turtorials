from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from manager.managers import PersonManager

class Person(AbstractBaseUser):

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    objects = PersonManager()

    identifier = models.CharField(max_length=64, unique=True, blank=False)
    name = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    sex = models.IntegerField(editable=False)
    address_from = models.IntegerField()
    current_address = models.IntegerField()
    email = models.EmailField()

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "identifier"


class Manager(models.Model):

    DEP_ACCOUNTING = 0  # 経理
    DEP_SALES = 5  # 営業
    DEP_PRODUCTION = 10  # 製造
    DEP_DEVELOPMENT = 15  # 開発
    DEP_HR = 20  # 人事
    DEP_FIN = 25  # 財務
    DEP_AFFAIRS = 30  # 総務
    DEP_PLANNING = 35  # 企画
    DEP_BUSINESS = 40  # 業務
    DEP_DISTR = 45  # 流通
    DEP_IS = 50  # 情報システム

    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    department = models.IntegerField()
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):

    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)
    manager = models.ForeignKey("Manager", on_delete=models.SET_NULL, null=True)
