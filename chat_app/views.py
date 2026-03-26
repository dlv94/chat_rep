from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ChatForm
from .models import Chat

@login_required
def chat(request):
    # Processa o formulário se for POST
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            new_chat = form.save(commit=False)
            new_chat.owner = request.user
            new_chat.save()
            return redirect('chat')   # redireciona para a mesma página
    else:
        form = ChatForm()

    # Busca todas as mensagens do usuário atual, ordenadas da mais antiga para a mais recente
    chats = Chat.objects.order_by('date_added')

    context = {
        'form': form,
        'chats': chats,
    }
    return render(request, 'chat.html', context)