from django.shortcuts import render
from django.http import HttpResponse
#Add this import at the top of the file
from webpage.forms import WebpageForm
from django.http import HttpResponseRedirect


    
def index(request):
    
    
    if request.method == 'POST':
    	form = WebpageForm(request.POST)

    	if form.is_valid():
    		form.save(commit=True)
    		return HttpResponseRedirect('/gracias/')

    else:
    	form = WebpageForm() 			

    return render(request, 'webpage/index.html', {'form':form})
# Create your views here.
