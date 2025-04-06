from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .brain.main import main
# Create your views here.


@csrf_exempt
def test(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            query = data.get("Query")

            main_obj = main()

            all_data = main_obj.response_newspaperlib(query=query)

            keys = ["news_link","summary","result","confidence_Score","publish_date","text"]
            json_data = [dict(zip(keys, sublist)) for sublist in all_data]
            return JsonResponse(json_data, safe=False, json_dumps_params={"indent": 4})

        except json.JSONDecodeError:
            return JsonResponse({"Error": "Invalid Json Bruhh..."},status=400)
    
    JsonResponse({"Error":"Stupid fuck send a POST request"})

def render_query_page(request):
    return render(request, 'app1/query_input.html')