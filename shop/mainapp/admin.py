from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm
from .models import *
from PIL import Image


#help text
class PendalAdminForm(ModelForm):

    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'rashirenie {}x{}'.format(
            *self.MIN_RESOLUTION
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min.width, min.height = self.MIN_RESOLUTION
        return image


class PendalAdmin(admin.ModelAdmin):

    form = PendalAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Pendal'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class EarRingsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='EarRings'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class OtherProductsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PendalCategoryChoiceField(Category.objects.filter(slug='OtherProducts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(EarRings, EarRingsAdmin)
admin.site.register(Pendals, PendalAdmin)
admin.site.register(OtherProducts, OtherProductsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)

