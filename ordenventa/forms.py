from django import forms
from .models import OrdenVenta, ItemOrdenVenta


class OrdenVentaForm(forms.ModelForm):
    class Meta:
        model = OrdenVenta
        fields = ["codigosap", "proyecto", "direccion_proyecto", "observacion", "fecha"]


class ItemOrdenVentaForm(forms.ModelForm):
    class Meta:
        model = ItemOrdenVenta
        fields = ["nro_articulo", "cantidad", "precio_bruto", "total_bruto"]
