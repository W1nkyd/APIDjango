from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class JewelrySerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    jewelry_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    type_id = serializers.PrimaryKeyRelatedField(queryset=JewelryType.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Jewelry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.type_id = validated_data.get("type_id", instance.type_id)
        instance.material_id = validated_data.get("material_id", instance.material_id)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance

class ClientSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    client_code = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance

class MaterialSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    material_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    unit_cost = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Material.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.unit_cost = validated_data.get("unit_cost", instance.unit_cost)
        instance.save()
        return instance

class OrderStatusSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status_code = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return OrderStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class OrderSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_id = serializers.IntegerField(read_only=True)
    order_date = serializers.DateField()
    status_code = serializers.PrimaryKeyRelatedField(queryset=OrderStatus.objects.all())
    client_code = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get("order_date", instance.order_date)
        instance.status_code = validated_data.get("status_code", instance.status_code)
        instance.client_code = validated_data.get("client_code", instance.client_code)
        instance.save()
        return instance

class ReviewSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    review_id = serializers.IntegerField(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    text = serializers.CharField()
    rating = serializers.IntegerField()
    review_date = serializers.DateField()

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_id = validated_data.get("order_id", instance.order_id)
        instance.text = validated_data.get("text", instance.text)
        instance.rating = validated_data.get("rating", instance.rating)
        instance.review_date = validated_data.get("review_date", instance.review_date)
        instance.save()
        return instance

class JewelryTypeSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return JewelryType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class OrderCompositionSerializer(serializers.Serializer):
    order_composition_id = serializers.IntegerField(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    jewelry_id = serializers.PrimaryKeyRelatedField(queryset=Jewelry.objects.all())
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return OrderComposition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_id = validated_data.get("order_id", instance.order_id)
        instance.jewelry_id = validated_data.get("jewelry_id", instance.jewelry_id)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.save()
        return instance

class SpecializationSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    specialization_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Specialization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class MasterSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    master_id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    specialization_id = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all())
    work_experience = serializers.IntegerField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Master.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.specialization_id = validated_data.get("specialization_id", instance.specialization_id)
        instance.work_experience = validated_data.get("work_experience", instance.work_experience)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.save()
        return instance

class ProductionSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    production_id = serializers.IntegerField(read_only=True)
    master_id = serializers.PrimaryKeyRelatedField(queryset=Master.objects.all())
    jewelry_id = serializers.PrimaryKeyRelatedField(queryset=Jewelry.objects.all())
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Production.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.master_id = validated_data.get("master_id", instance.master_id)
        instance.jewelry_id = validated_data.get("jewelry_id", instance.jewelry_id)
        instance.save()
        return instance

class MaterialUsageSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    material_usage_id = serializers.IntegerField(read_only=True)
    production_id = serializers.PrimaryKeyRelatedField(queryset=Production.objects.all())
    material_id = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())
    quantity_used = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return MaterialUsage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.production_id = validated_data.get("production_id", instance.production_id)
        instance.material_id = validated_data.get("material_id", instance.material_id)
        instance.quantity_used = validated_data.get("quantity_used", instance.quantity_used)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    role = serializers.CharField(max_length=50)
    registration_date = serializers.DateField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.role = validated_data.get("role", instance.role)
        instance.registration_date = validated_data.get("registration_date", instance.registration_date)
        instance.save()
        return instance
