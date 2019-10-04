from django.shortcuts import render

def homePage(request):
    teamName = request.user
    context = {'teamname': teamName}
    template = 'home.html'
    return render(request, template, context)