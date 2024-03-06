# function based views
from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("Home page requested")
    friends = [
        'ankit',
        'ravi',
        'kishan'
    ]
    return JsonResponse(friends,safe=False)
    
# class/object based views