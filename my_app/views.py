from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def analyze(request):
   
        djtext = request.GET.get('text', 'default')
        removepunc = request.GET.get('removepunc', 'off')
        uppercasetext = request.GET.get('touppercase', 'off')
        tolowercase = request.GET.get('tolowercase', 'off')
        removenewlines = request.GET.get('remonewlines', 'off')
        print(djtext)
        analyzed =''
        if removepunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
           
            
            for char in djtext:
                if  char not in punctuations:
                        analyzed = analyzed + char
            param ={
                'analyzed': analyzed
            }
        
            # return render(request, 'analyzed.html', param)
        # else:
        #     return HttpResponse("error")            
        
        if uppercasetext =='on':
            # analyzed =''
            djtext = request.GET.get('text', 'default')
            analyzed= djtext.upper()
        param ={
            'analyzed': analyzed
        }
        # return render(request, 'analyzed.html', param)
        
        
        if tolowercase =='on':
            # analyzed =''
            # djtext = request.GET.get('text', 'default')
            analyzed= djtext.lower()
        param ={
            'analyzed': analyzed
        }
        
        if removenewlines =='on':
          for char in djtext:
             if char != '\n':
                analyzed =analyzed +char
        param ={
            'analyzed': analyzed
        }
        return render(request, 'analyzed.html', param)