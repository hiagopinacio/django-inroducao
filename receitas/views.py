from django.shortcuts import render


def index(request):
    receitas = ["Lasanha", "Bolo", "Sopa", "Sorvete"]

    return render(request, "index.html", {"receitas": receitas})


def receita(request):
    return render(request, "receita.html")
