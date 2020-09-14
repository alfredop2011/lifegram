
from django.http import HttpResponse
from django.http import JsonResponse
import json

from datetime import datetime

def hello_World(request):
    now = datetime.now().strftime('%B %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current sercer time is {now}'.format(now=str(now)))


def sorted_ints(request):
    numbers = [int(i) for i in request.GET['number'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'Message': 'Integers Sorted Successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), 
    content_type='application/json')

    # response = JsonResponse([numbers], safe=False)
    # return response

def say_hi():
    return HttpResponse('Oh, hi! Current')