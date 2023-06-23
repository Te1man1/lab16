from django.urls import path
from myapp import views
from django.contrib import admin

from myapp.views import user_profile_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipment/create/', views.equipment_create, name='equipment_create'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/<int:pk>/update/', views.equipment_update, name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),

    path('equipment_category/create/', views.equipment_category_create, name='equipment_category_create'),
    path('equipment_category/', views.equipment_category_list, name='equipment_category_list'),
    path('equipment_category/<int:pk>/update/', views.equipment_category_update, name='equipment_category_update'),
    path('equipment_category/<int:pk>/delete/', views.equipment_category_delete, name='equipment_category_delete'),

    path('responsible_person/create/', views.responsible_person_create, name='responsible_person_create'),
    path('responsible_person/', views.responsible_person_list, name='responsible_person_list'),
    path('responsible_person/<int:pk>/update/', views.responsible_person_update, name='responsible_person_update'),

    path('equipment_log/create/', views.equipment_log_create, name='equipment_log_create'),
    path('equipment_log/', views.equipment_log_list, name='equipment_log_list'),
    path('equipment_log/<int:pk>/update/', views.equipment_log_update, name='equipment_log_update'),
    path('equipment_log/<int:pk>/delete/', views.equipment_log_delete, name='equipment_log_delete'),

    path('user_profile/create/', views.user_profile_create, name='user_profile_create'),
    path('user_profile/', views.user_profile_list, name='user_profile_list'),
    path('user_profile/update/<int:pk>/', user_profile_update, name='user_profile_update'),
]