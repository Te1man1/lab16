from django import forms
from .models import Equipment, EquipmentCategory, ResponsiblePerson, EquipmentLog, UserProfile, UserOwnedEquipment


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('name', 'model', 'serial_number', 'cost')


class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = '__all__'


class ResponsiblePersonForm(forms.ModelForm):
    class Meta:
        model = ResponsiblePerson
        fields = '__all__'


class EquipmentLogForm(forms.ModelForm):
    class Meta:
        model = EquipmentLog
        fields = '__all__'


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user', 'first_name', 'last_name', 'email', 'role')


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserOwnedEquipmentForm(forms.ModelForm):
    class Meta:
        model = UserOwnedEquipment
        fields = '__all__'
