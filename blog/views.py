from django.shortcuts import render

def blog_index(request):
    return render(request, "blog_index.html")

def Detect(request):
    return render(request, "Detect.html")

def Mov_lateral(request):
    return render(request, "Mov_lateral.html")

def hydra(request):
    return render(request, "hydra.html")

def Buffer(request):
    return render(request, "Buffer.html")

def DefEv(request):
    return render(request, "DefEv.html")

def Minitalk(request):
    return render(request, "minitalk.html")

def chisel(request):
    return render(request, "chisel.html")

def persist(request):
    return render(request, "perist.html")

def soc(request):
    return render(request, "soc.html")

def scrap(request):
    return render(request, "scrap.html")

