from django import forms
from django.contrib.auth.models import User
from django import forms
from App.models import *


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate

from django.conf import settings


# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100, min_length=5,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='Email', max_length=20, min_length=5,
#                              widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label='Password', max_length=50, min_length=5,
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Confirm Password',
#                                 max_length=50, min_length=5,
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))




class UserRegistrationForm(UserCreationForm):
	username = forms.IntegerField(
		required=True,
		#label=True,
		widget=forms.NumberInput(attrs={'class' :'input'})

	)
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={'class': 'input'})
	)

	password1 = forms.CharField(
		required=True,
		#label=True,
		widget=forms.PasswordInput(attrs={'class' :'input'})

	)

	password2 = forms.CharField(
		required=True,
		#label=True,
		widget=forms.PasswordInput(attrs={'class' :'input'})

	)

	# Course = forms.ModelChoiceField(
	# 	queryset=Courses.objects.all(),
	# 	required=True,
	# 	label=False,
	# 	widget=forms.Select(attrs={'class': 'input'})
	# )

	# Year = forms.ModelChoiceField(
	# 	queryset=Years.objects.all(),
	# 	required=True,
	# 	widget=forms.Select(attrs={'class': 'input'})
	# )
    
    
    
	class Meta:
	    model = MyUser
	    fields = (
	    "email",
	    "username",
	    "password1",
	    "password2"
	    
	    

	    
         )
	def clean_email(self):
	    email = self.cleaned_data['email'].lower()
	    try:
	        myuser = MyUser.objects.get(email=email)
	    except Exception as e:
	        return email
	    raise forms.ValidationError(f"Email {email} is already exist.")

	def clean_username(self):
	    username = self.cleaned_data['username']
	    try:
	        myuser = MyUser.objects.get(username=username)
	    except Exception as e:
	        return username
	    raise forms.ValidationError(f"username {username} is already exist.")






class MyUserForm(UserCreationForm):
    
    
    
    class Meta:
        model = MyUser
        fields = (
        "email",
        "username",
        "password1",
        "password2",
        "phone",
        
        "profile_image",
        #"UserCodes",
        #"is_admin",
        "is_superuser",
        "is_staff",
        "is_active",
        
        "company_name"

        
         )
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            myuser = MyUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} tayari ipo")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            myuser = MyUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Jina {username} tayari lipo.")






class UpdateMyUserForm(forms.ModelForm): 
    class Meta:
        model = MyUser
        fields = (
    	"email",
        "username",
        # "password1",
        # "password2",
        "phone",
        
        "profile_image",
        #"UserCodes",
        #"is_admin",
        "is_superuser",
        "is_staff",
        "is_active",
        
        "company_name"
        

        
         )





class KumbushoLaChanjoSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = KumbushoLaChanjo
		fields =['AinaYaKuku', 'username', 'export_to_CSV']


class KumbushoUsafishajiBandaSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = KumbushoUsafishajiBanda
		fields =['Muda', 'username', 'export_to_CSV']



class KumbushoLaUatamiajiWaMayaiSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = KumbushoLaUatamiajiWaMayai
		fields =['username', 'export_to_CSV']



class KumbushoLaMabadilikoYaLisheSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = KumbushoLaMabadilikoYaLishe
		fields =['username', 'export_to_CSV']





class EmailSendCount_KumbushoUsafishajiBandaSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_KumbushoUsafishajiBanda
		fields =['username', 'export_to_CSV']


class EmailSendCount_KumbushoLaUatamiajiWaMayaiSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_KumbushoLaUatamiajiWaMayai
		fields =['username', 'export_to_CSV']


class EmailSendCount_KumbushoLaMabadilikoYaLisheSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_KumbushoLaMabadilikoYaLishe
		fields =['username', 'export_to_CSV']




class EmailSendCount_KumbushoLaChanjoSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_KumbushoLaChanjo
		fields =['username', 'export_to_CSV']








#-------------------DUKA LAKO----------------------
class DukaLakoSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = DukaLako
		fields =['username', 'export_to_CSV']



class MyUserSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = MyUser
		fields =['username', 'export_to_CSV']



class MikoaSearchForm(forms.ModelForm):
	
	JinaLaMkoa = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza jina la mkoa'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = Mikoa
		fields =['JinaLaMkoa', 'export_to_CSV']


class WanunuziSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza jina la mnunuzi'})

	)

	Wilaya = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'wilaya', 'placeholder' : 'Ingiza jina la wilaya'})

	)

	Message = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'Message', 'placeholder' : 'Andika ujumbe'})

	)

	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = Wanunuzi
		fields =['Message','username','Wilaya', 'export_to_CSV']






class WazalishajiWaHudumaSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza jina la mtoa huduma'})

	)

	
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = WazalishajiWaHuduma
		fields =['username', 'export_to_CSV']




class HudumazaWazalishajiSearchForm(forms.ModelForm):
	
	JinaLaHuduma = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza jina la huduma'})

	)

	
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = HudumazaWazalishaji
		fields =['JinaLaHuduma', 'export_to_CSV']

class WatejaWoteSearchForm(forms.ModelForm):
	
	JinaLaMteja = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza jina la mteja'})

	)

	# WilayaYaMteja = forms.CharField(
	# 	required=False,
	# #label=False,
	# 	widget=forms.TextInput(attrs={'id' :'Wilaya', 'placeholder' : 'Ingiza jina la huduma'})

	# )

	
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = WatejaWote
		fields =['JinaLaMteja', 'export_to_CSV']






class HistoriaZaJumbeZaWanunuziSearchForm(forms.ModelForm):
	start_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	end_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	JinaLaMnunuzi = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = HistoriaZaJumbeZaWanunuzi
		fields =['JinaLaMnunuzi', 'export_to_CSV']

class EmailSendCount_DukaLakoSearchForm(forms.ModelForm):
	start_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	end_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_DukaLako
		fields =['username', 'export_to_CSV']



class EmailSendCount_MyUserSearchForm(forms.ModelForm):
	start_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	end_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_MyUser
		fields =['username', 'export_to_CSV']




class MaoniSearchForm(forms.ModelForm):
	
	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = Maoni
		fields =['username', 'export_to_CSV']


class EmailSendCount_MaoniSearchForm(forms.ModelForm):
	start_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	end_date = forms.DateTimeField(
	    required=False, 
	    widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

	username = forms.CharField(
		required=False,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'username', 'placeholder' : 'Ingiza Jina kamili'})

	)
	export_to_CSV = forms.BooleanField(required=False)
	#start_date = forms.DateTimeField(required=False)
	#end_date = forms.DateTimeField(required=False)


	class Meta:
		model = EmailSendCount_Maoni
		fields =['username', 'export_to_CSV']




class DukaLakoUpdateForm(forms.ModelForm):
	
	class Meta:
		model = DukaLako
		fields =[
			
			'Status'
			]

class MyUserUpdateForm(forms.ModelForm):
	
	class Meta:
		model = MyUser
		fields =[
			
			'Tick'
			]


class MaoniUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Maoni
		fields =[
			
			'is_checked'
			]


class WanunuziCreateForm(forms.ModelForm):
	

	class Meta:
		model = Wanunuzi
		fields = '__all__'


class WazalishajiWaHudumaCreateForm(forms.ModelForm):
	

	class Meta:
		model = WazalishajiWaHuduma
		fields = '__all__'

class HudumazaWazalishajiCreateForm(forms.ModelForm):
	

	class Meta:
		model = HudumazaWazalishaji
		fields = '__all__'


class WatejaWoteCreateForm(forms.ModelForm):
	

	class Meta:
		model = WatejaWote
		fields = '__all__'


class WatejaWoteUpdateForm(forms.ModelForm):
	
	class Meta:
		model = WatejaWote
		fields = [
			"JinaLaMteja",
			"phoneYaMteja",
			"emailYaMteja",
			"MkoaWaMteja",
			"WilayaYaMteja",
			"PichaYaMteja",
			"PaidAmount",
			"SikuYaKupokea"
		]


class WatejaWoteIsCheckedForm(forms.ModelForm):
	
	class Meta:
		model = WatejaWote
		fields = ["is_checked"]

class WatejaWoteOngezaOdaForm(forms.ModelForm):
	
	class Meta:
		model = WatejaWote
		fields = ["OngezaOda"]
	

