from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return JsonResponse({
                'id': client.id,
                'name': client.name,
                'mobile1': client.mobile1,
                'mobile2': client.mobile2,
                'email': client.email,
                'created_at': client.created_at,
                'updated_at': client.updated_at,
            })
        return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return JsonResponse({
                'id': client.id,
                'name': client.name,
                'mobile1': client.mobile1,
                'mobile2': client.mobile2,
                'email': client.email,
                'created_at': client.created_at,
                'updated_at': client.updated_at,
            })
        return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def client_delete(request, id):
    if request.method == 'POST':
        client = get_object_or_404(Client, id=id)
        client.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid Request'}, status=400)
