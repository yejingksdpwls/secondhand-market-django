from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__" # ['title', 'content']
        exclude = ("author","like_user", "see_count")