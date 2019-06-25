from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserprofileForm, CropsForm, AddProduceForm, AddFertilizerForm, FinancialRecordsForms, FarmMachineryForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Crops, Fertilizer, Produce, FinancialRecords, FarmMachinery

decorators = [staff_member_required, login_required]


def index(request):
    if request.user.is_staff:
        return redirect('admin_dash')
    else:
        return redirect('addProduce')
    return render(request)


@login_required
@staff_member_required
def home(request):
    return render(request, 'farm/admin_dash.html')


@login_required
@staff_member_required
def admin_dash(request):
    return render(request, 'farm/admin_dash.html')


@login_required
@staff_member_required
def Add_employee(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserprofileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('user_list')
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserprofileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'farm/Add_employee.html', context)


class UserListView(ListView):
    paginate_by = 10
    model = User
    context_object_name = 'user_list'
    template_name = ('auth/user_list.html')


class UserDetailView(DeleteView):
    model = User
    context_object_name = 'user_detail'
    template_name = ('auth/user_detail.html')


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name',
              'email', 'is_active', 'is_staff']

    success_url = reverse_lazy('user_list')


class UserDeleteview(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')


class CropCreateView(CreateView):
    model = Crops
    form_class = CropsForm
    template_name = ('farm/Add_crop.html')
    # fields = '__all__'

    success_url = reverse_lazy('crops_list')


class CropListView(ListView):
    paginate_by = 8
    model = Crops
    context_object_name = 'crop_list'
    template_name = ('farm/crops_list.html')


class CropUpdateView(UpdateView):
    model = Crops
    fields = '__all__'

    success_url = reverse_lazy('crops_list')


class CropDeleteView(DeleteView):
    model = Crops
    success_url = reverse_lazy('crops_list')


class CropsDetailView(DeleteView):
    model = Crops
    context_object_name = 'crop_detail'
    template_name = ('farm/crops_detail.html')


class FertilizerCreate(CreateView):
    model = Fertilizer
    form_class = AddFertilizerForm
    template_name = ('farm/fertilizer_form.html')
    success_url = reverse_lazy('crops_list')


class FertilizerView(ListView):
    model = Fertilizer
    context_object_name = 'fertilizer_list'
    template_name = ('farm/fertilizer_list.html')


class FertilizerDeleteView(DeleteView):
    model = Fertilizer
    form_class = AddFertilizerForm

    success_url = reverse_lazy('fertilizer_list')


class FertlizerUpdateView(UpdateView):
    model = Fertilizer
    form_class = AddFertilizerForm
    template_name = ('farm/fertilizer_form.html')

    success_url = reverse_lazy('fertilizer_list')


class FinancialRecordsCreate(CreateView):
    model = FinancialRecords
    form_class = FinancialRecordsForms
    template_name = ('farm/financialRecord_form.html')
    success_url = reverse_lazy('financialRecords_list')


class FinancialRecordsView(ListView):
    model = FinancialRecords
    context_object_name = 'financialRecords_list'
    template_name = ('farm/financialRecords_list.html')


class FinancialRecordsDeleteView(DeleteView):
    model = FinancialRecords
    form_class = FinancialRecordsForms

    success_url = reverse_lazy('financialRecords_list')


class FinancialRecordsUpdateView(UpdateView):
    model = FinancialRecords
    form_class = FinancialRecordsForms
    template_name = ('farm/fertilizer_form.html')
    success_url = reverse_lazy('financialRecords_list')


@method_decorator(decorators, name='dispatch')
class FarmMachineryCreateView(CreateView):
    model = FarmMachinery
    form_class = FarmMachineryForm
    template_name = ('farm/farmMachinery-form.html')
    success_url = reverse_lazy('farm-machinery-list')


class FarmMachineryView(ListView):
    model = FarmMachinery
    context_object_name = 'farm-machinery-list'
    template_name = ('farm/farm-machinery-list.html')


class FarmMachineryDetailView(DetailView):
    model = FarmMachinery
    context_object_name = 'farm-machinery-detail'
    template_name = ('farm/farm-machinery-details.html')


class FarmMachineryDeleteView(DeleteView):
    model = FarmMachinery
    form_class = FarmMachineryForm

    success_url = reverse_lazy('farm-machinery-list')


class FarmMachineryUpdateView(UpdateView):
    model = FarmMachinery
    form_class = FarmMachineryForm
    template_name = ('farm/farmmachinery-form.html')
    success_url = reverse_lazy('farm-machinery-list')


@method_decorator(login_required, name='dispatch')
class AddProduce(CreateView):
    model = Produce
    fields = '__all__'
    success_url = reverse_lazy('addProduce')
