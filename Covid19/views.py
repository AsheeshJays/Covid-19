from django.shortcuts import render
import  requests

def index(request):
    data = True
    result = None
    globalSummary = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            globalSummary = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'Covid19/index.html',{'globalSummary':globalSummary,'countries':countries})

def worldco(request):
    data = True
    result = None
    globalSummary = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            globalSummary = json['Global']
            countries = json['Countries']
            data = False
        except:
            data = True
    return render(request, 'Covid19/worldco.html',{'globalSummary':globalSummary,'countries':countries})

def indiaco(request):
    data = True
    result = None
    statedata = None
    while(data):
        try :
            result = requests.get('https://api.covid19india.org/data.json')
            json= result.json()
            statedata = json['statewise']
            data = False
        except:
            data = True
    return render(request, 'Covid19/indiaco.html',{'statedata':statedata})

def daywise(request):
    data = True
    result = None
    daywise = None
    while(data):
        try:
            result = requests.get('https://api.covid19india.org/data.json')
            json = result.json()
            daywise = json['cases_time_series']
            data = False
        except:
            data = True
    return render(request, 'Covid19/daywise.html',{'daywise':daywise})
