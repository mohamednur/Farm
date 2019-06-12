from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserprofileForm, CropsForm, addProduce
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Crops, Fertilizer


@login_required
def index(request):
    return render(request, 'index.html')


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

            return redirect('index')
    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserprofileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'farm/Add_employee.html', context)


def Add_crops(request):
    crops_form = CropsForm(request.POST)
    if crops_form.is_valid():
        crops = crops_form.save()

        return redirect('index')
    else:

        crops_form = CropsForm()

    context = {'crops_form': crops_form}
    return render(request, 'farm/Add_crop.html', context)


@login_required
def Add_produce(request):

    produce_form = addProduce(request.POST)

    if produce_form.is_valid():
        produce = produce_form.save()

    else:
        produce_form = addProduce()

    context = {'produce': produce_form}
    return render(request, 'farm/addProduce.html', context)


def success(request):
    return render(request, 'auth/success.html')


class UserListView(ListView):
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


class CropListView(ListView):
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
    fields = '__all__'
