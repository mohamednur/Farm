from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls.static import static
from farm import views as farm_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/login', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('farm.urls')),
    path('addProduce/', farm_views.AddProduce.as_view(), name="addProduce"),
    path('Admin_Dash/', farm_views.admin_dash, name="admin_dash"),
    path('Admin_Dash/Add_employee/', farm_views.Add_employee, name='Add_employee'),
    path('Admin_Dash/users/', staff_member_required(
         farm_views.UserListView.as_view()), name='user_list'),
    path('Admin_Dash/user/<int:pk>', staff_member_required(
         farm_views.UserDetailView.as_view()), name='user_detail'),
    path('Admin_Dash/user_update/<int:pk>', staff_member_required(
         farm_views.UserUpdateView.as_view()), name='user_update'),
    path('Admin_Dash/user_delete/<int:pk>', staff_member_required(
         farm_views.UserDeleteview.as_view()), name='user_delete'),
    path('Admin_Dash/crops/', staff_member_required(
         farm_views.CropListView.as_view()), name='crops_list'),
    path('Admin_Dash/fertilizer/',
         farm_views.FertilizerView.as_view(), name='fertilizer_list'),
    path('Admin_Dash/fertilizer_delete/<int:pk>', staff_member_required(
         farm_views.FertilizerDeleteView.as_view()), name='fertilizer_delete'),
    path('Admin_Dash/fertilizer_update/<int:pk>', staff_member_required(
         farm_views.FertlizerUpdateView.as_view()), name='fertilizer_update'),
    path('Admin_Dash/crop/<int:pk>',
         farm_views.CropsDetailView.as_view(), name='crop_detail'),
    path('Admin_Dash/crop_update/<int:pk>', staff_member_required(
         farm_views.CropUpdateView.as_view()), name='crop_update'),
    path('Admin_Dash/crop_delete/<int:pk>', staff_member_required(
         farm_views.CropDeleteView.as_view()), name='crop_delete'),
    path('Admin_Dash/Add_crop/',
         farm_views.CropCreateView.as_view(), name="Add_crops"),
    path('Admin_Dash/Addfinance/',
         farm_views.FinancialRecordsCreate.as_view(), name="Add_finance_records"),
    path('Admin_Dash/finance_delete/<int:pk>', staff_member_required(
         farm_views.FinancialRecordsDeleteView.as_view()), name='financialRecords_delete'),
    path('Admin_Dash/finance_list/', staff_member_required(
         farm_views.FinancialRecordsView.as_view()), name='financialRecords_list'),
    path('Admin_Dash/Add-farm-machinery/', staff_member_required(
         farm_views.FarmMachineryCreateView.as_view()), name="Add-farm-machinery"),
    path('Admin_Dash/farm-machinery-list/', staff_member_required(
         farm_views.FarmMachineryView.as_view()), name='farm-machinery-list'),
    path('Admin_Dash/farm-machinery-details/<int:pk>', staff_member_required(
        farm_views.FarmMachineryDetailView.as_view()), name='farm-machinery-details'),
    path('Admin_Dash/farm-machinery-update/<int:pk>', staff_member_required(
         farm_views.FarmMachineryUpdateView.as_view()), name='farm-machinery-update'),
    path('Admin_Dash/farm-machinery-delete/<int:pk>', staff_member_required(
         farm_views.FarmMachineryDeleteView.as_view()), name='farm-machinery-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Admin_Dash/add_fertilizer/',
         farm_views.FertilizerCreate.as_view(), name='add_fertilizer'),
]
