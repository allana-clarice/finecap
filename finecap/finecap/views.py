from django.shortcuts import render, get_object_or_404, redirect
from .models import Stand, Reserva
from .forms import ReservaForm, StandForm

def detalhes_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context={
        'objeto' : reserva,
    }
    return render(request,'finecap/detalhes_reserva.html',context)

def excluir_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')

def adicionar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'finecap/form.html', {'form': form})


def adicionar_stand(request):
    if request.method == 'POST':
        form = StandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = StandForm()
    return render(request, 'form.html', {'form': form})

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'finecap/lista_reservas.html', {'reservas': reservas})

def lista_stand(request):
    stands = Stand.objects.all()
    return render(request, 'lista_stand.html', {'stands': stands})

def detalhes_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'finecap/detalhes_reserva.html', {'reserva': reserva})

def excluir_stand(request, id):
    stand = get_object_or_404(Stand, id=id)
    if request.method == 'POST':
        stand.delete()
        return redirect('lista_stand')

def index(request):
    
    return render(request, "finecap/index.html",)

