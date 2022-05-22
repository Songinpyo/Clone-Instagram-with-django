from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        print("get 호출")
        return render(request, "djangoProject/main.html")

    def post(self, request):
        print("post 호출")
        return render(request, "djangoProject/main.html")