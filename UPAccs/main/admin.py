from django.contrib import admin
from .models import Client, OrderStatus, Order, Review, JewelryType, Material, Jewelry, OrderComposition, Specialization, Master, Production, MaterialUsage, User

# Register your models here.
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('jewelry_id' , 'name', 'type_id', 'material_id', 'weight', 'price')
    search_fields = ('name', 'price')
    list_filter = ['price']
    list_per_page = 1
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'password', 'first_name', 'last_name', 'role', 'registration_date')
    search_fields = ('username', 'role')
    list_per_page = 1
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_code', 'first_name', 'last_name', 'address', 'phone', 'email')
    search_fields = ('client_code', 'first_name', 'last_name', 'address', 'phone', 'email')
    list_filter = ['first_name']
    list_per_page = 1
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('status_code', 'name')
    search_fields = ('status_code', 'name')
    list_filter = ['name']
    list_per_page = 1
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date', 'status_code', 'client_code')
    search_fields = ('order_date', 'status_code', 'clien_code')
    list_per_page = 1
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'order_id', 'text', 'rating', 'review_date')
    search_fields = ('review_date', 'rating', 'text')
    list_per_page = 1
class JewelryTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'name')
    search_fields = ('name', 'type_id')
    list_per_page = 1
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_id', 'name', 'unit_cost')
    search_fields = ('name', 'unit_cost')
    list_per_page = 1
class OrderCompositionAdmin(admin.ModelAdmin):
    list_display = ('order_composition_id', 'order_id', 'jewelry_id', 'quantity')
    search_fields = ('quantity', 'order_id')
    list_per_page = 1
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('specialization_id', 'name')
    search_fields = ('name', 'specialization_id')
    list_per_page = 1
class MasterAdmin(admin.ModelAdmin):
    list_display = ('master_id', 'first_name', 'specialization_id', 'work_experience', 'salary')
    search_fields = ('name', 'price')
    list_per_page = 1
class MaterialUsageAdmin(admin.ModelAdmin):
    list_display = ('material_usage_id', 'production_id', 'material_id', 'quantity_used')
    search_fields = ('quantity_used', 'material_id')
    list_per_page = 1
class ProductionAdmin(admin.ModelAdmin):
    list_display = ('production_id', 'master_id', 'jewelry_id', 'start_date', 'end_date')
    search_fields = ('start_date', 'master_id')
    list_per_page = 1

admin.site.register(Client, ClientAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(JewelryType, JewelryTypeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(OrderComposition, OrderCompositionAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Production, ProductionAdmin)
admin.site.register(MaterialUsage, MaterialUsageAdmin)
admin.site.register(User, UserAdmin)

