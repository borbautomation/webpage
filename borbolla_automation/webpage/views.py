from django.shortcuts import render
from django.http import HttpResponse
#Add this import at the top of the file
from webpage.forms import WebpageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from webpage.send_email.send_mail import send_email_base as contact_email

    
def index(request):
    
    
    if request.method == 'POST':
    	form = WebpageForm(request.POST)

    	if form.is_valid():
    		form.save(commit=True)
    		users = User.objects.all()
    		emails = []
    		for user in users:
    		    emails.append(user.email)
            
            text = 'Nombre : %s\nCompania : %s\nEmail : %s\n Mensaje : %s\n'%(request.POST['nombre'],
            																  request.POST['compania'],
            																  request.POST['email'],
            																  request.POST['text'],)

            _send_mail = contact_email(emails,'Nuevo mensaje desde pagina web!',text)

    		return HttpResponseRedirect('/gracias/')

    else:
    	form = WebpageForm() 			

    return render(request, 'webpage/index.html', {'form':form})
# Create your views here.
