from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EquipmentForm, EquipmentCategoryForm, ResponsiblePersonForm, EquipmentLogForm, UserProfileForm, UserOwnedEquipmentForm
from .models import Equipment, EquipmentCategory, ResponsiblePerson, EquipmentLog, UserProfile, UserOwnedEquipment


def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            try:
                equipment, created = Equipment.objects.get_or_create(defaults=form.cleaned_data)
                if not created:

                    equipment.name = form.cleaned_data['name']
                    equipment.model = form.cleaned_data['model']
                    equipment.serial_number = form.cleaned_data['serial_number']
                    equipment.cost = form.cleaned_data['cost']
                    equipment.save()
                return redirect('equipment_list')
            except IntegrityError:
                form.add_error(None, 'equipment already exists.')
    else:
        form = EquipmentForm()
    return render(request, 'equipment_form.html', {'form': form, 'title': 'Create New Equipment'})


def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})


def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment_form.html', {'form': form, 'title': 'Update equipment'})


def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.delete()
    messages.success(request, 'Equipment deleted successfully')
    return redirect('equipment_list')


def equipment_category_create(request):
    if request.method == 'POST':
        form = EquipmentCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment category created successfully')
            return redirect('equipment_category_list')
    else:
        form = EquipmentCategoryForm()
    return render(request, 'equipment_category_form.html', {'form': form})


def equipment_category_list(request):
    categories = EquipmentCategory.objects.all()
    return render(request, 'equipment_category_list.html', {'categories': categories})


def equipment_category_update(request, pk):
    category = get_object_or_404(EquipmentCategory, pk=pk)
    if request.method =='POST':
        form = EquipmentCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment category updated successfully')
            return redirect('equipment_category_list')
    else:
        form = EquipmentCategoryForm(instance=category)
    return render(request, 'equipment_category_form.html', {'form': form})


def equipment_category_delete(request, pk):
    category = get_object_or_404(EquipmentCategory, pk=pk)
    category.delete()
    messages.success(request, 'Equipment category deleted successfully')
    return redirect('equipment_category_list')


def responsible_person_create(request):
    if request.method == 'POST':
        form = ResponsiblePersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Responsible person created successfully')
            return redirect('responsible_person_list')
    else:
        form = ResponsiblePersonForm()
    return render(request, 'responsible_person_form.html', {'form': form})


def responsible_person_list(request):
    responsible_persons = ResponsiblePerson.objects.all()
    return render(request, 'responsible_person_list.html', {'responsible_persons': responsible_persons})


def responsible_person_update(request, pk):
    responsible_person = get_object_or_404(ResponsiblePerson, pk=pk)
    if request.method == 'POST':
        form = ResponsiblePersonForm(request.POST, instance=responsible_person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Responsible person updated successfully')
            return redirect('responsible_person_list')
    else:
        form = ResponsiblePersonForm(instance=responsible_person)
    return render(request, 'responsible_person_form.html', {'form': form})


def equipment_log_create(request):
    if request.method == 'POST':
        form = EquipmentLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment log created successfully')
            return redirect('equipment_log_list')
    else:
        form = EquipmentLogForm()
    return render(request, 'equipment_log_form.html', {'form': form})


def equipment_log_list(request):
    equipment_logs = EquipmentLog.objects.all()
    return render(request, 'equipment_log_list.html', {'equipment_logs': equipment_logs})


def equipment_log_update(request, pk):
    equipment_log = get_object_or_404(EquipmentLog, pk=pk)
    if request.method == 'POST':
        form = EquipmentLogForm(request.POST, instance=equipment_log)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment log updated successfully')
            return redirect('equipment_log_list')
    else:
        form = EquipmentLogForm(instance=equipment_log)
    return render(request, 'equipment_log_form.html', {'form': form})


def equipment_log_delete(request, pk):
    equipment_log = get_object_or_404(EquipmentLog, pk=pk)
    equipment_log.delete()
    messages.success(request, 'Equipment log deleted successfully')
    return redirect('equipment_log_list')

@login_required
def user_profile_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            try:
                profile, created = UserProfile.objects.get_or_create(user=request.user, defaults=form.cleaned_data)
                if not created:
                    # Если профиль уже существует, обновляем его поля
                    profile.first_name = form.cleaned_data['first_name']
                    profile.last_name = form.cleaned_data['last_name']
                    profile.email = form.cleaned_data['email']
                    profile.save()
                return redirect('user_profile_list')
            except IntegrityError:
                form.add_error(None, 'User profile already exists.')
    else:
        form = UserProfileForm()
    return render(request, 'user_profile_form.html', {'form': form, 'title': 'Create New User Profile'})


@login_required
def user_profile_update(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile_list')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profile_form.html', {'form': form, 'title': 'Update User Profile'})

def user_profile_list(request):
    profiles = UserProfile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'user_profile_list.html', context)


# def user_profile_update(request, pk):
#     user_profile = get_object_or_404(UserProfile, pk=pk)
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your account has been updated!')
#             return redirect('user_profile')
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form
#     }
#     return render(request, 'user_profile_form.html', context)
#
# def user_profile_delete(request):
#     if request.method == 'POST':
#         request.user.delete()
#         messages.success(request, 'Your account has been deleted!')
#         return redirect('home')
#     return render(request, 'user_profile_form.html')