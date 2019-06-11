from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserprofileForm, CropsForm, addProduce
from .models import User


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
    if request.method == 'POST':
        produce_form = addProduce(request.POST)

        if produce_form.is_valid():
            produce = produce_form.save()

            produce.save()

            return redirect('#')
    else:
        produce_form = addProduce()

    context = {'produce': produce_form}
    return render(request, 'farm/addProduce.html', context)


class UserListView(class ModelNameList(ListView):
                   model=User
                   context_object_name='user_list'
                   template_name='farm/user_list')
