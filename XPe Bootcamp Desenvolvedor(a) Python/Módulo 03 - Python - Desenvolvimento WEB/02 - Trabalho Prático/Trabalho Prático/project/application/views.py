import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from application.logic import root_square_solver


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, 'index.html')


@csrf_exempt
def calcular_coeficientes(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        try:
            data: dict = json.loads(request.body)
            a = float(data.get('a', None))
            b = float(data.get('b', None))
            c = float(data.get('c', None))

            raizes = root_square_solver(a, b, c)
            if raizes is None:
                response_data = {'message': "A equação de 2º grau não possui raízes reais!"}

            else:
                raizes_str = ', '.join(str(root) for root in raizes)
                response_data = {'message': f"S = [{raizes_str}]"}

            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        except Exception as exc:
            return JsonResponse({'error': str(exc)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
