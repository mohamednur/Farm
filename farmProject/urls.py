from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from farm import views as farm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farm.urls')),
    path('addProduce/', farm_views.addProduce, name="addProduce"),
    path('Admin_Dash/', farm_views.admin_dash, name="admin_dash"),
    path('Admin_Dash/Add_employee/', farm_views.Add_employee, name='Add_employee'),
    path('Admin_Dash/users/',
         farm_views.UserListView.as_view(), name='user_list'),
    path('Admin_Dash/user/<int:pk>',
         farm_views.UserDetailView.as_view(), name='user_detail'),
    path('Admin_Dash/user_update/<int:pk>',
         farm_views.UserUpdateView.as_view(), name='user_update'),
    path('Admin_Dash/user_delete/<int:pk>',
         farm_views.UserDeleteview.as_view(), name='user_delete'),
    path('Admin_Dash/crops/',
         farm_views.CropListView.as_view(), name='crops_list'),
    path('Admin_Dash/crop/<int:pk>',
         farm_views.CropsDetailView.as_view(), name='crop_detail'),
    path('Admin_Dash/crop_update/<int:pk>',
         farm_views.CropUpdateView.as_view(), name='crop_update'),
    path('Admin_Dash/crop_delete/<int:pk>',
         farm_views.CropDeleteView.as_view(), name='crop_delete'),

    path('Admin_Dash/Add_crop/', farm_views.Add_crops, name="Add_crops"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('success/', farm_views.success, name='success'),

]
