from django.urls import path
from .views import (
    ListaOrdenesVenta,
    DetalleOrdenVenta,
    ListaItemsOrdenVenta,
    DetalleItemOrdenVenta,
    OrdenVentaCRUDView,
    agregar_item_orden_venta,
)

urlpatterns = [
    path("ordenesventa/", ListaOrdenesVenta.as_view(), name="lista_ordenesventa"),
    path(
        "ordenesventa/<int:pk>/", DetalleOrdenVenta.as_view(), name="detalle_ordenventa"
    ),
    path(
        "itemsordenesventa/",
        ListaItemsOrdenVenta.as_view(),
        name="lista_itemsordenesventa",
    ),
    path(
        "itemsordenesventa/<int:pk>/",
        DetalleItemOrdenVenta.as_view(),
        name="detalle_itemordenventa",
    ),
    path("", OrdenVentaCRUDView.as_view(), name="ordenventa-crud"),
    path(
        "agregar_item_orden_venta/<int:ordenventa_id>/",
        agregar_item_orden_venta,
        name="agregar_item_orden_venta",
    ),
    # path(
    #     "ordenventa/<int:pk>/", OrdenVentaDetailView.as_view(), name="ordenventa-detail"
    # ),
]
