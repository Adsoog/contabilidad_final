from django.urls import path
from .views import (
    ListaOrdenesVenta,
    DetalleOrdenVenta,
    ListaItemsOrdenVenta,
    DetalleItemOrdenVenta,
    OrdenVentaCRUDView,
    create_item_ordenventa,
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
        "crear-item-ordenventa/<int:ordenventa_id>/",
        create_item_ordenventa,
        name="crear-item-ordenventa",
    ),
    # path(
    #     "ordenventa/<int:pk>/", OrdenVentaDetailView.as_view(), name="ordenventa-detail"
    # ),
]
