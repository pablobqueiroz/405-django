from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def mostrar_rolezinho(request):
    roles = ['Bailão','Shopping União','Quermesse da Paróquia de São João','Calçadão de Osasco','SESC','Risca Faca']
    bairro = 'Richdale'
    return render(request,'rolezinho.html',{'roles':roles})

