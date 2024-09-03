
from django.db import models
from django.core.paginator import *

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    registration_date = models.DateField()

    class Meta:
        verbose_name = 'Пользователь'


class Client(models.Model):
    client_code = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Клиент'
class OrderStatus(models.Model):
    status_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус заказа'
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    status_code = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    client_code = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказы'
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField()

    class Meta:
        verbose_name = 'Отзывы'
class JewelryType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип украшений'
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Материалы'
class Jewelry(models.Model):
    jewelry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type_id = models.ForeignKey(JewelryType, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Украшения'
class OrderComposition(models.Model):
    order_composition_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    jewelry_id = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Состав заказа'
class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Специализация'
class Master(models.Model):
    master_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    work_experience = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Мастер'
class Production(models.Model):
    production_id = models.AutoField(primary_key=True)
    master_id = models.ForeignKey('Master', on_delete=models.CASCADE, null=True)
    jewelry_id = models.ForeignKey('Jewelry', on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Продукция'
class MaterialUsage(models.Model):
    material_usage_id = models.AutoField(primary_key=True)
    production_id = models.ForeignKey(Production, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Используемые материалы'