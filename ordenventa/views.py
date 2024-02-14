from rest_framework import generics
from .models import OrdenVenta, ItemOrdenVenta
from .serializers import OrdenVentaSerializer, ItemOrdenVentaSerializer
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from .forms import ItemOrdenVentaForm, OrdenVentaForm, MassItemOrdenVentaForm


class OrdenVentaCRUDView(View):
    template_name = "ordenventa_crud.html"

    def get(self, request, *args, **kwargs):
        # Obtén la acción de la URL (edit o delete)
        action = request.GET.get("action", None)

        # Lógica para editar
        if action == "edit":
            orden_venta_id = request.GET.get("edit", None)
            if orden_venta_id:
                orden_venta = get_object_or_404(OrdenVenta, pk=orden_venta_id)
                form = OrdenVentaForm(instance=orden_venta)
            else:
                form = OrdenVentaForm()

        # Lógica para eliminar
        elif action == "delete":
            orden_venta_id = request.GET.get("delete", None)
            if orden_venta_id:
                orden_venta = get_object_or_404(OrdenVenta, pk=orden_venta_id)
                orden_venta.delete()
                return HttpResponseRedirect(reverse_lazy("ordenventa-crud"))

        # Lógica por defecto para mostrar la lista y el formulario de creación
        else:
            form = OrdenVentaForm()

        ordenes_venta = OrdenVenta.objects.all()
        return render(
            request, self.template_name, {"ordenes_venta": ordenes_venta, "form": form}
        )

    def post(self, request, *args, **kwargs):
        form = OrdenVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("ordenventa-crud"))
        else:
            ordenes_venta = OrdenVenta.objects.all()
            return render(
                request,
                self.template_name,
                {"ordenes_venta": ordenes_venta, "form": form},
            )


def create_item_ordenventa(request, ordenventa_id):
    ordenventa = get_object_or_404(OrdenVenta, pk=ordenventa_id)

    if request.method == "POST":
        form = MassItemOrdenVentaForm(request.POST)
        if form.is_valid():
            items_data = form.cleaned_data["items_data"].split("\n")

            items_to_create = []
            for data in items_data:
                item_data = data.split("\t")
                if len(item_data) == 4:
                    nro_articulo, cantidad, precio_bruto, total_bruto = item_data
                    item = ItemOrdenVenta(
                        nro_articulo=nro_articulo,
                        cantidad=cantidad,
                        precio_bruto=precio_bruto,
                        total_bruto=total_bruto,
                        ordenventa=ordenventa,
                    )
                    items_to_create.append(item)

            # Usar bulk_create para insertar los ítems de manera eficiente
            ItemOrdenVenta.objects.bulk_create(items_to_create)

            return redirect("ordenventa-crud")  # O redirige a donde desees
    else:
        form = MassItemOrdenVentaForm()

    return render(
        request, "crear_item_ordenventa.html", {"form": form, "ordenventa": ordenventa}
    )


# Vistas para OrdenVenta
class ListaOrdenesVenta(generics.ListCreateAPIView):
    queryset = OrdenVenta.objects.all()
    serializer_class = OrdenVentaSerializer


class DetalleOrdenVenta(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdenVenta.objects.all()
    serializer_class = OrdenVentaSerializer


# Vistas para ItemOrdenVenta
class ListaItemsOrdenVenta(generics.ListCreateAPIView):
    queryset = ItemOrdenVenta.objects.all()
    serializer_class = ItemOrdenVentaSerializer


class DetalleItemOrdenVenta(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOrdenVenta.objects.all()
    serializer_class = ItemOrdenVentaSerializer
