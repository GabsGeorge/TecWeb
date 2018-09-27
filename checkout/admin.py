from django.contrib import admin
from checkout.models import Pedido, ItemDoPedido, CartItem

#Item do Pedido begin
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart_key","produto","quantidade","preco_p", "total_p"]
    search_fields = ["pedido","produto"]
    filter_horizontal = []
    ordering = ["cart_key"]
    list_filter = []
#Item do pedido end

#Item do Pedido begin
class ItemdosPedidosAdmin(admin.ModelAdmin):
    list_display = ["pedido","produto","quantidade","preco_p"]
    search_fields = ["pedido","produto"]
    filter_horizontal = []
    ordering = ["pedido"]
    list_filter = []
#Item do pedido end

#Pedido begin
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["user","status","opcoes_de_pagamento","modificado","criado"]
    search_fields = ["user"]
    filter_horizontal = []
    ordering = ["user"]
    list_filter = []
#Pedido end

admin.site.register(Pedido,PedidoAdmin)
admin.site.register(ItemDoPedido,ItemdosPedidosAdmin)
admin.site.register(CartItem, CartItemAdmin)
# Register your models here.
