from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("<h1>Hello World<h1>")
#
# def about(request):
#     return HttpResponse("<h1>This is the about page<h1>")

def index(request):
    # params = {'name':'Harry', 'place': 'Earth'}
    return render(request,"index.html")
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('Charcount', 'off')
    # print(removepunc)
    # print(djtext)
    # analyzetext = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext=analyzed
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext=analyzed
    if extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        djtext=analyzed
    if charcount == 'on':
        count = 0
        analyzed = ""
        for char in djtext:
                count= count+1
        return HttpResponse("Character count = "+str(count))
    if removepunc=='off' and fullcaps=='off' and newlineremover == 'off' and extraspaceremover=='off' and charcount=='off':
        return HttpResponse("Error!")
    
    params = {'purpose':'Remove punctuation', 'analyzed_text': analyzed}
    return render(request, "analyze.html", params)

# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("New Line remover")
#
# def spaceremove(request):
#     return HttpResponse("Space remover")

# def charcount(request):
#     return HttpResponse("Character count")