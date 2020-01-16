# Aula 1 - Iniciando aplicação e subindo o servidor 

## 1. Instalando o Django.
	pip install django

---

## 2. Iniciando o projeto
	django-admin startproject nome_do_projeto

Será criado uma pasta com o nome do projeto no diretório atual.
Para iniciar o projeto em um diretório específico, basta adicionar o caminho após o nome do projeto, evitando a criação de uma pasta, ex.:
	django-admin startproject nome_do_projeto .

### Configurações iniciais do projeto:

No arquivo nome_do_projeto/settings.py, já é possível definir LANGUAGE_CODE e TIME_ZONE. Basta olhar na documentação.

Padrões para português-br e fuso horário de SP:

	LANGUAGE_CODE = 'pt-br'
	
	TIME_ZONE = 'America/Sao_Paulo'

---

## 3. Iniciando o Servidor

No terminal, na pasta do projeto, onde está o arquivo manage.py:

	python manage.py runserver

O servidor ficará executando no terminal e acessando <localhost:8000> no navegador, teremos a pagina introdutória do Django

---

## 4. Criando uma aplicação no django

No terminal:

	python manage.py startapp nome_do_app

Cada parte fechada do sistema, deve estar em apps diferentes para melhorar organização de urls, views, e demais partes do código.

### Confgs iniciais de um App

1. Criar um arquivo chamado urls.py dentro da pasta do app

2. Importar módulo path do django:
    
        from django.urls import path

3.  Importar o arquivo views para chamar suas funções a partir das urls:
	
        from . import views

4. Adicionar urlpatterns, ex:

        urlpatterns = [
            path('', views.index, name='index'
        ]

    O primeiro parâmetro em path é a pagina requisitada, sendo levado em conta o caminho após endereço padrão do site.

5. Criar a função em view.py

    O segundo parâmetro é o nome da função que será chamada no arquivo views.py importado. O Django já cuida de repassar uma request para esta função, então devemos cria-la no arquivo views.py, ex:

        from django.http import HttpResponse

        # Create your views here.


        def index(request):
            return HttpResponse("<h1>Olá, mundo!</h1>")

6. informar arquivo de urls do app para o projeto.
   
    Por fim, precisamos incluir o arquivo de urls que criamos, no arquivo padrão de urls, para que o django entenda que alí também há urls possíveis de serem utilizadas.
    então devemos adicionar  no arquivo nome_do_projeto/urls.py, a importação do método include, 
    e uma linha chamando redirecionando urls para aplicação:

        from django.urls import path, include

        urlpatterns = [
                    ... ,
                    path("app/", include("receitas.urls")
        ]

    caso seja o aplicativo padrão, passar uma string vazia no primeiro parâmetro.

