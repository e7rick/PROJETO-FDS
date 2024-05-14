from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados, Dica
from .models import Feedback
from .forms import FeedbackForm 
from .forms import ProgressoForm
from .models import Duvida
from .models import Consulta
from .forms import CadastroForm, LoginForm, DicaForm,ConsultaForm
from .models import Imagem


def login(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/login.html', {'imagens': imagens})

def cadastro(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/cadastro.html', {'imagens': imagens})

def dicas(request):

    return render(request, 'dicas.html')

def dicas_adm(request):

    return render(request, 'dicas_adm.html')

def home_aluno(request, nome_usuario=None):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            return redirect('/home_adm/')
        elif tipo == 'aluno':
            return redirect('/home_aluno/')
        else:
            return HttpResponse("Usuário ou senha inválidos", status=401)
    return render(request, 'home_aluno.html', {'nome_usuario': nome_usuario})

def home_adm(request):
    usuarios = Dados.objects.all()  # Obtém todos os usuários do banco de dados
    return render(request, 'home_adm.html', {'usuarios': usuarios})

def duvidas(request):

    return render(request,'duvidas.html')

def treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')

def treinospredefinidos_adm(request):

    return render(request, 'treinospredefinidos_adm.html')

def marcar_consulta(request):

    return render(request, 'marcar_consulta.html')

def progresso(request):

    return render(request,'progresso.html')

def feedback(request):

    return render(request,'feedback.html')


def enviar_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home_aluno.html', {'message': 'Feedback registrado com sucesso!'})
            
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def registrar_progresso(request):
    if request.method == 'POST':
        form = ProgressoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/progresso/')
    else:
        form = ProgressoForm()
    return render(request, 'progresso.html', {'form': form})

def enviar_duvida(request):
    if request.method == 'POST':
        duvida_escrita = request.POST.get('duvidaescrita')
        nome_treinador = request.POST.get('treinador')
        
        # Crie um novo objeto de Duvida e salve no banco de dados
        duvida = Duvida(duvida_escrita=duvida_escrita, nome_treinador=nome_treinador)
        duvida.save()
        
        # Retorna uma resposta para o usuário
        return redirect('/')
    else:
        return redirect('/')
    

def enviar_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_texto = form.cleaned_data['feedback']
            nome_aluno = form.cleaned_data['nome']

            # Verifica se o nome do aluno está cadastrado como "usuario" no banco de dados
            aluno = Dados.objects.filter(nome=nome_aluno, tipo='usuario').first()
            if aluno:
                # Cria uma instância do Feedback e salva no banco de dados
                Feedback.objects.create(aluno=nome_aluno, feedback=feedback_texto)
                
                sucesso = "Feedback enviado com sucesso."
                return redirect('/feedback/', {'mensagem_sucesso': sucesso})
                
            else:
                # Se o aluno não estiver cadastrado, exibe uma mensagem de erro
                erro = "O nome do aluno não corresponde a um usuário cadastrado."
                return render(request, 'feedback.html', {'mensagem_erro': erro})
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})
    

def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('/marcar_consulta/')  
    else:
        form = ConsultaForm() 

    return render(request, 'marcar_consulta.html', {'form': form})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})


def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            # Consulta ao banco de dados para verificar o usuário
            usuario = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if usuario:
                if tipo == 'usuario':
                    # Redirecionar usuário para a página home do aluno
                    return redirect('/home_aluno/')  # Passando o nome do usuário como parte da URL
                elif tipo == 'administrador':
                    # Redirecionar administrador para a página home do administrador
                    return redirect('/home_adm/')
            
            erro = 'Usuário não cadastrado ou credenciais incorretas.'
    else:
        form = LoginForm()
        erro = None
    return render(request, 'front/login.html', {'form': form, 'erro': erro})

def adicionar_dica(request):
    if request.method == 'POST':
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dicas_adm/')
    else:
        form = DicaForm()
    return render(request, 'dicasadm.html', {'form': form})

def exibir_dica(request):
    dicas = Dica.objects.all()
    return render(request, 'dicas.html', {'dicas': dicas})

