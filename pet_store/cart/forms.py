from .models import Orders,Payment,OrderPet,Pet
from django import forms


class OrderForm(forms.modelForm):
    status = (('new','new'),('pending','pending'),('delivered','devlivered'),('cancelled','cancelled'))

    states = [
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('GOA','Goa'),
        ('GJ','Gajrat'),
        ('RJ','Rajasthan'),
        ('MH','Maharashtra'),
        ('UP','Uttar Pradesh'),
    ]   



    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'})) 
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'})) 
    phone= forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'})) 
    email= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    address= forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'})) 
    country= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    state= forms.CharField(widget=forms.Select(choices=states,attrs={'class':'form-control'})) 
    city= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))  


    class Meta:
        models = Orders
        fields = ['first_name','last_name','phone','email','address','country','state','city'] 

