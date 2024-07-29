from django.shortcuts import render

def inicio(request):
    if request.method == "POST":
        try:
            quantidade = int(request.POST.get('quantidade', 0))
            context = {
                'quantidade': range(quantidade)
            }
            return render(request, 'notas_pesos.html', context)
        except ValueError:
            error_message = "Por favor, insira um número válido para a quantidade."
            return render(request, 'inicio.html', {'error': error_message})
    return render(request, 'inicio.html')

def calcular_media(request):
    if request.method == "POST":
        try:
            # Usamos a quantidade com base no número de campos de nota ou peso
            quantidade = len([key for key in request.POST if key.startswith('nota')])
            notas = []
            pesos = []
            
            for i in range(quantidade):
                nota = float(request.POST.get(f'nota{i}', 0))
                peso = float(request.POST.get(f'peso{i}', 0))
                notas.append(nota)
                pesos.append(peso)
            
            soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
            soma_pesos = sum(pesos)
            media_ponderada = soma_ponderada / soma_pesos if soma_pesos != 0 else 0
            
            return render(request, 'resultado.html', {'media_ponderada': media_ponderada})
        except ValueError:
            error_message = "Por favor, insira valores válidos para notas e pesos."
            return render(request, 'notas_pesos.html', {'error': error_message, 'quantidade': quantidade})
    return render(request, 'inicio.html')
