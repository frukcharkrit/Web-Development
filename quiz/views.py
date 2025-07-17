import json
from django.shortcuts import render
import io
import sys
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_question(request):
    if request.method == 'GET':
        question = {
            "id": 1,
            "text": "ประเทศไทยมีกี่จังหวัด",
            "choices": [50, 68, 72, 77]
        }
        return JsonResponse(question)

@csrf_exempt
def post_question(request):
    if request.method == 'POST':
        data = {
            "id": 9,
            "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล",
            "choices": ["C", "C++", "C#", "Python", "R", "Julia"]
        }
        return JsonResponse(data)