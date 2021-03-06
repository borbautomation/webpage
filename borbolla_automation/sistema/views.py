from django.shortcuts import render
from django.http import HttpResponse
from sistema.printing.printing import MyPrint
from io import BytesIO
 
#@staff_member_required
def print_users(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Dolar_hoy.pdf"'
 
    buffer = BytesIO()
 
    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users()
 
    response.write(pdf)
    return response

# Create your views here.
