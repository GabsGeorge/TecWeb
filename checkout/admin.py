from django.contrib import admin
from checkout.models import Pedido, ItemDoPedido, CartItem



admin.site.register([Pedido, ItemDoPedido, CartItem])

# Register your models here.
