from cv2 import randShuffle
from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    
    except:
        raise  Http404("404 GENERIC ERROR ") 

# domain.com/fist_app/0 --> domain.com/first_app/sports

def num_page_view(request, num_page):
    topics_list = list(articles.keys()) # ['sports','finance','politics']
    topic = topics_list[num_page]
    
    return HttpResponseRedirect(topic)
    
def add_view(request, num1, num2):
    # domain.com/first_app/4/4/ --> 8
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result)) 
