from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add_cart', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete_itemcart/<id>/<item_id>/<slug>', views.delete_itemcart, name='delete_itemcart'),
    path('history/', views.history, name='history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)