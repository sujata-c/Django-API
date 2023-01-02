#from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
#re_path('', TemplateView.as_view(template_name='api_app/base.html'), name='home'),

re_path(r'^api/store$', views.ItemList.as_view(), name='items'),
re_path(r'^api/store/(?P<pk>100|[1-9]?[0-9]+)$', views.ItemModify.as_view(), name='item'),
re_path(r'^api/categories$', views.CategoryList.as_view(), name='categories'),
re_path(r'^api/category/(?P<pk>100|[1-9]?[0-9]+)$', views.CategoryModify.as_view(), name='category'),

# built-in class based views calling
path('suppliers/', views.SupplierList.as_view(), name='suppliers_list'),
path('suppliers/<int:pk>/detail', views.SupplierDetail.as_view(), name='supplier_detail'),
path('suppliers/create/', views.SupplierCreate.as_view(), name='supplier_create'),
path('suppliers/<int:pk>/update/', views.SupplierUpdate.as_view(), name='supplier_update'),
path('suppliers/<int:pk>/delete/', views.SupplierDelete.as_view(), name='supplier_delete'),
]