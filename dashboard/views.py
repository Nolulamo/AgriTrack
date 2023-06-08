from django.shortcuts import render, redirect
from .forms import UserAuthForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Nutrient
from .serializers import NutrientSerializer
from django.views.decorators.csrf import csrf_exempt
from .decorators import login_required


def HomeView(request):

    return render(request, 'dashboard/home.html', {})


def UserSignUp(request):
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserAuthForm()
    return render(request, 'dashboard/register.html', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'dashboard/login.html', {})

def UserLogOut(request):
    logout(request)
    return redirect('home')

class NutrientsData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        nutrients = Nutrient.objects.all()
        serializer = NutrientSerializer(nutrients, many=True)
        data = {
            'nutrients': serializer.data,
        }
        return Response(data)
    
@csrf_exempt
@api_view(['POST'])
def PostNutrients(request):
    serializer = NutrientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required
def NutrientsView(request):

    nutrients = Nutrient.objects.all()[:1]

    return render(request, 'dashboard/dashboard.html', {'nutrients': nutrients})

@login_required
def Notes(request):

    return render(request, 'dashboard/notes.html', {})