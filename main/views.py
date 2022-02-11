from django.shortcuts import render


def login_api(request):
    print("AAAA")
    return render(request, 'hobbiry/user_signup.html')
