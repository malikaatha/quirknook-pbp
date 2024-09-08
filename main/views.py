from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'QuirkNook',
        'name': 'Malika Atha Indurasmi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
