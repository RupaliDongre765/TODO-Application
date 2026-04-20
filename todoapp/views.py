from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from .forms import ContactForm
from .models import CModel
from .forms import CForm
from django.contrib.auth.models import User
import datetime
import requests

def home(request):
	if request.user.is_authenticated:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c56398aa9dd4ea5e0854302e39acf5a5'
		city = 'Kalyan'
		r = requests.get(url.format(city)).json()
	
		city_weather = {
            		'city': city,
            		'temperature': r['main']['temp'],
            		'description': r['weather'][0]['description'],
            		'icon': r['weather'][0]['icon'],
        		}
		context = {'city_weather' : city_weather}
		return render(request, 'home.html', context)
	else:
		return redirect('ulogin')


def ucreatetask(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			todo = request.POST.get('task')
			todo = CModel(task=todo, user=request.user)
			todo.save()
			fm = CForm()
		
			return render(request,'ucreatetask.html',{'fm':fm,'msg':'Task is recorded'})
		else:
			fm = CForm()
			return render(request,'ucreatetask.html',{'fm':fm})
	else:
		return redirect('ulogin')
		



def taskview(request):
	if request.user.is_authenticated:
		log_user = request.user
		alltodos = CModel.objects.filter(user=log_user)
		return render(request, 'taskview.html', {'alltodos': alltodos})
	else:
		return redirect('ulogin')	


def delete(request, id):
	ds = CModel.objects.get(pk=id)
	ds.delete()
	return redirect('taskview')

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            
            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                
            }
            content = template.render(context)

            email = EmailMessage(
                "Feedback from the given user is",
                content,
                "Your website" +'',
                ['gvibes471@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.add_message(request, messages.INFO, 'Feedback is submitted to developer through mail, thank you for the response.')
            return redirect('contact')
        
    return render(request, 'contact.html', {
        'form': form_class
    
    })


       