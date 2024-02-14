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


ItemOrdenVentaFormSet = forms.inlineformset_factory(
    parent_model=OrdenVenta,
    model=ItemOrdenVenta,
    form=ItemOrdenVentaForm,
    extra=50,  # Puedes ajustar esto según tus necesidades
    can_delete=False,
)


class MassItemOrdenVentaForm(forms.Form):
    items_data = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 40}))
