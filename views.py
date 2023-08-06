from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PatientDataForm  # Import the form you create
from .forms import CustomerDetailsForm

def tasklist(request):
    return HttpResponse ('GAN Model for Chest Xrays')

def homepage(request):
    return render(request, 'homepage.html')
    
def patient_data_form(request):
    if request.method == 'POST':
        form = PatientDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_details')  # Redirect to the customer details page
    else:
        form = PatientDataForm()
    return render(request, 'patient_data_form.html', {'form': form})

def customer_details_form(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            # Process the customer details form data here (save to database, etc.)
            return HttpResponse("Customer details submitted successfully!")  # You can redirect to a success page instead
    else:
        form = CustomerDetailsForm()
    return render(request, 'customer_details_form.html', {'form': form})
