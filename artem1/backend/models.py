from django.db import models


class Status(models.Model):
    status = models.CharField("Статус", max_length=150)

    def __str__(self):
        return self.status


class Order(models.Model):
    """Заказ"""
    telephone = models.CharField("Номер телефона", max_length=15, default='')
    name = models.CharField("ФИ клиента", max_length=70, default='')
    number = models.CharField("Код Заказа", max_length=150)
    brand = models.CharField("Бренд", max_length=300)
    articul = models.CharField("Артикул", max_length=150)
    term = models.DateField("Дата заказа", max_length=150)
    term_wanted = models.DateField("Ожидается на складе")
    amount_wanted = models.IntegerField("Было заказано")
    amount_actual = models.IntegerField("Количество")
    cost = models.FloatField("Цена за штуку")
    pre_cost = models.FloatField("Предоплата", default='24')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField("Описание")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


