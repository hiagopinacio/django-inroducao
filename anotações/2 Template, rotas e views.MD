Aula 2 - Template, rotas e views 
================================

## 1. Criar HTML em arquivo separado

Deve-se criar uma pasta chamada templates dentro da pasta do app.
Dentro da pasta criada, criamos nossos arquivos html, ex.:

***nome_do_app/templates/index.html***  


### Retornando o HTML

Devemos mudar o retorno da função de view em view.py para renderizar o HTML.
  
Em vez de usar HTTPResponse, devemos utilizar o método ***django.shortcuts.render(request, 'path')***, passando o request e o caminho do arquivo HTML, ex.:

    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')

---  

## 2. Arquivos Estáticos

### CONFIGURÇÕES NO DJANGO

É necessário adicionar o diretório de templates em ***nome_do_projeto/settings.py***.  
No dicionário padrão da lista `TEMPLATES`, dentro da lista de DIR.
Para isso, usamos o **os.path.join(path_base, path_2)**. E para o path_base, já existe a variável `BASE_DIR`



    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'nome_do_app/templates')],

            ...

        },
    ]

Ainda no arquivo ***setting.py*** precisamos especificar o caminho dos arquivos estáticos. Estas configurações ficam no final do arquivo:

    STATIC_ROOT = os.pat.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'nome_do_projeto/static'),
    ]

**Agora precisamos criar a pasta *static* no diretório *nome_do_projeto***

> **CRIAR PASTA: *nome_do_projeto/static***

inserir nesta pasta os arquivos estáticos css, js, ...

após isso, no terminal:

    python manage.py collectstatic



### INFORMANDO ESTILOS NO HTML

Podemos utilizar instruções dentro de um arquivo HTML no django.  
Para isto basta colocar o código dentro de `{% cod %}`

Para informar referências para os arquivos estáticos utilizamos `{% static 'caminho/relativo.css %}`, a partir da pasta static, sem informa-la. Ex.:

    <script src='{% static 'js/arquivo.js' %}'></script>