from django.contrib import admin
from .models import Product, Order
from django.http import HttpRequest
from django.db.models import QuerySet
from .admin_mixins import ExportAsCSVMixin


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description="Archive products")
def mark_arcived(modeladmin: admin.ModelAdmin, HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unarchive products")
def mark_unarcived(modeladmin: admin.ModelAdmin, HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Product)
class ProductAdimin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_arcived,
        mark_unarcived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description_short", "prise", 'discount', "archived"
    list_display_links = "pk", "name"
    ordering = "pk", "name"
    search_fields = "name", "description" 
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("prise", "discount"),
            "classes": ("collapse",),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse"),
            "description": "Extra options. Field 'archived' if for soft delete"
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode","created_at", "user_verbose"
    
    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")
    
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username