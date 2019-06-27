from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserprofileForm, CropsForm, AddProduceForm, AddFertilizerForm, FinancialRecordsForms, FarmMachineryForm, ProduceForm, ProduceSoldForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Crops, Fertilizer, Produce, FinancialRecords, FarmMachinery, ProduceSold
from django.views.generic import View
from django.utils import timezone
from .render import Render
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
decorators = [staff_member_required, login_required]


@login_required
@staff_member_required
def home(request):
    return render(request, 'farm/admin_dash.html')


def help(request):
    return render(request, 'help.html')


@login_required
@staff_member_required
def online_help(request):
    return render(request, 'farm/online-help.html')


@login_required
@staff_member_required
def admin_dash(request):
    return render(request, 'farm/admin_dash.html')


def index(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password' '')

        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.is_staff:
                return redirect('admin_dash')
            elif request.user.is_staff is False:
                return redirect('addProduce')
            else:
                return redirect('login')
        else:
            form = AuthenticationForm()
            msg = messages.error(
                request, "Invalid Credentials Please Enter valid credentials", fail_silently=True)
            return render(request, 'registration/login.html', {'msg': msg, 'form': form})
    return render(request, 'registration/login.html')


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


class FinancialRecordsDetailView(DetailView):
    model = FinancialRecords
    context_object_name = 'financialRecords_detail'
    template_name = ('farm/financialRecords_detail.html')


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
    form_class = ProduceForm
    success_url = reverse_lazy('addProduce')


class ProduceList(ListView):
    model = Produce
    context_object_name = 'ProduceList'
    template_name = 'farm/produce-list.html'


class ProduceUpdateView(UpdateView):
    model = Produce
    form_class = ProduceForm
    template_name = ('farm/produce_form.html')
    success_url = reverse_lazy('produce-list')


class ProduceDeleteView(DeleteView):
    model = Produce
    form_class = ProduceForm

    success_url = reverse_lazy('produce-list')


class ProduceDetailView(DetailView):
    model = Produce
    context_object_name = 'produce-detail'
    template_name = ('farm/produce-details.html')


class ProduceSoldView(CreateView):
    model = ProduceSold
    form_class = ProduceSoldForm

    template_name = ('farm/produceSold_form.html')
    success_url = reverse_lazy('produce-list')


class ProduceSoldUpdateView(UpdateView):
    model = ProduceSold
    form_class = ProduceSoldForm
    template_name = ('farm/produceSold_form.html')
    success_url = reverse_lazy('produce-sold-list')


class ProduceSoldList(ListView):
    model = ProduceSold
    context_object_name = 'ProduceSoldList'
    template_name = 'farm/produce-sold-list.html'


class ProduceSoldDeleteView(DeleteView):
    model = ProduceSold
    form_class = ProduceSoldForm

    success_url = reverse_lazy('produce-sold-list')


class ProduceSoldDetailView(DetailView):
    model = ProduceSold
    context_object_name = 'produce-sold-detail'
    template_name = ('farm/produce-sold-details.html')


class Pdf(View):

    def get(self, request):
        records = FinancialRecords.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'records': records,
            'request': request,
        }
        return Render.render('farm/pdf.html', params)


class CropsPdf(View):
    def get(self, request):
        all_crops = Crops.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'all_crops': all_crops,
            'request': request
        }
        return Render.render('farm/crops-pdf.html', params)


class FarmMachineryPdf(View):
    def get(self, request):
        farm_machinery_report = FarmMachinery.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'farm_machinery_report': farm_machinery_report,
            'request': request
        }
        return Render.render('farm/farm-machinery-pdf.html', params)


class ProduceSalesPdf(View):
    def get(self, request):
        produce_sales_report = ProduceSold.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'produce_sales_report': produce_sales_report,
            'request': request
        }
        return Render.render('farm/produce-sales-pdf.html', params)


class FinancialPdf(View):
    def get(self, request):
        financial_report = FinancialRecords.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'financial_report': financial_report,
            'request': request
        }
        return Render.render('farm/financial-pdf.html', params)


class FertilizerPdf(View):
    def get(self, request):
        fertilizer_report = Fertilizer.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'fertilizer_report': fertilizer_report,
            'request': request
        }
        return Render.render('farm/fertilizer-pdf.html', params)


class UserPdf(View):
    def get(self, request):
        users_report = User.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'users_report': users_report,
            'request': request
        }
        return Render.render('farm/users-pdf.html', params)


class ProducePdf(View):
    def get(self, request):
        produce_report = Produce.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'produce_report': produce_report,
            'request': request
        }
        return Render.render('farm/produce-pdf.html', params)
