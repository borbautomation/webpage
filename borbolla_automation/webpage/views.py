from django.shortcuts import render
from django.http import HttpResponse
#Add this import at the top of the file
from webpage.forms import WebpageForm


    
def index(request):
    
    form = WebpageForm()
    context_dict = {'form': form}
    if request.method == 'POST':
    	form = WebpageForm(request.POST)

    	if form.is_valid():
    		form.save(commit=True)
    		return index(request)

    	else:
    		print(form.errors)	

    return render(request, 'webpage/index.html', context=context_dict)
# Create your views here.
