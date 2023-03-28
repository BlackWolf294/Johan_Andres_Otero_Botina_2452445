from django.http import HttpResponse
from django.template import Template, Context
from autos.models import cliente, auto


def lista_autos(request):
    lista_autos = auto.objects.all()
    document=open(r'C:\Users\SENA\Desktop\Internet Explorer\Trabajos\Evaluacion\Johan_Andres_Otero_Botina_2452445\concesionario\Template\lista_autos.html')
    plt=Template(document.read())
    document.close()
    cxt=Context({
        "lista_autos":lista_autos
    })
    document=plt.render(cxt)
    return HttpResponse(document)

def lista_clientes(request):
    lista_clientes = cliente.objects.all()
    document=open(r'C:\Users\SENA\Desktop\Internet Explorer\Trabajos\Evaluacion\Johan_Andres_Otero_Botina_2452445\concesionario\Template\lista_clientes.html')
    plt=Template(document.read())
    document.close()
    cxt=Context({
        "lista_clientes":lista_clientes
        })
    document=plt.render(cxt)
    return HttpResponse(document)

