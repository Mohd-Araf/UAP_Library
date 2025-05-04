from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def library_rules(request):
    return render(request, 'rules.html')
def about(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')
def membership_activation(request):
    return render(request, 'membershipactivation.html')
def borrowing_policy(request):
    return render(request, 'borrowing_policy.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
