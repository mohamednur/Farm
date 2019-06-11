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
    path('Admin_Dash/Add_crop/', farm_views.Add_crops, name="Add_crops"),
    path('accounts/', include('django.contrib.auth.urls')),

]
