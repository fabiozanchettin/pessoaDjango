from django.shortcuts import render, redirect
from .forms import PessoaForm, ProfissaoForm
from .models import Profissao, Pessoa


def index(request):
    pessoas = Pessoa.objects.all()
    profissoes = Profissao.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas, 'profissoes': profissoes})


def cadastrar_profissao(request):
    if request.method == 'POST':
        form = ProfissaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfissaoForm()
    return render(request, 'cadastrar_profissao.html', {'form': form})


def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            profissao = form.cleaned_data.get('profissao')  # Note que aqui é 'profissao', não 'profissao_id'
            if profissao is None:
                form.add_error('profissao', 'erro')
            else:
                form.save()
                return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastrar_pessoa.html', {'form': form})
