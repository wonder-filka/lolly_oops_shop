from django.urls import path

from .views import test_veiw, ProductDetailView

urlpatterns = [
    path('', test_veiw, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
