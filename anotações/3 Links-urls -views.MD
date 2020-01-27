# Aula 2 - Links, urls e views


## 1. Definindo Rotas das URLs

Na ancoras dentro do código HTML, devemos adicionar um código em python com `{%  %}`. Ex.:

    <a href="{% url 'nome' %}>link</a>

Onde o nome é definido no arquivo urls.py, na propriedade `name` dentro de cada path. Ex.:

    urlpatterns = [
        path('', views.index, name='index')
    ]

Para novas urls, devemos adicionar novos paths:

    urlpatterns = [
        path('', views.index, name='index'),
        path('paginax', views.func_paginax, name='paginax')
    ]

no arquivo views.py, devemos criar a função informada na lista `urlpatterns`:

    def func_pagina(request):
        render(request, 'paginax.html')

---
## 2. Extendendo HTML

Podemos criar código HTML que se repetem em mais de uma página de maneira otimizada.

Para isso :

1. Criamos um arquivo HTML base contendo cabeçalhos, importações javascript, e tudo que se repete nas outras páginas.
2. Não esquecer de carregar os arquivos estáticos com `{% load static %}`
3. Definir o local onde entrará um bloco de código com `{% block nome_do_bloco %}` e `{% endblock %}`
> Exemplo:
>
>     {% load static %}
>     <!DOCTYPE html>
>     <html lang="pt-br"> -->
>
>     <head>
>         <title>Titulo</title>
>         <link rel="icon" href="{% static 'img/favicon.ico' %}">
>         <link rel="stylesheet" href="{% static 'site.css' %}">
>     </head>
>
>     <body>
>         {% block corpo %}{% endblock %}
>         <script src="{% static 'js/principal.js' %}"></script>
>     </body>
>
>     </html>
> ---


Para utilizar o arquivo base em outras páginas:

1. No início do arquivo HTML, colocar o conteúdo `{% extends 'arquivo_base.html' %}`
2. Carregar os arquivos estáticos com `{% load static %}`
3. Inserir o conteúdo html desejado entre `{% block nome_do_bloco %}` e `{% endblock %}`

Exemplo:

    {% extends 'base.html' %}
    {% load static %}

    {% block corpo %}
        <h1>Título</h1>
        <p> Hello, World of blocks</p>
    {% endblock %}


---
## 3. Partials

Além de criar um template base para nossas páginas, podemos criar partials para códigos html que se repetem em diversas páginas como menus de navegação, rodapé, etc.

1. Para melhor organização, criamos uma pasta chamada partials dentro da pasta templates.
2. Criamos agora, um arquivo html com o código a ser repetido, por exemplo, o código html do menu.
3. Não esquecer de carregar arquivos estáticos no início do novo arquivo com `{% load static %}`
4. No arquivo html da página a ser chamada pela url, adicionamos o  código `{% include 'partials/file.html' %}`.