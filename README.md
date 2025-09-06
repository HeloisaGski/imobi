# 👑 Luxury Realty - Imobiliária de Luxo

Site premium de imobiliária desenvolvido com Django e design luxuoso, incluindo integração completa com WhatsApp para contato direto e experiência excepcional para clientes VIP.

## 🚀 Funcionalidades

### ✅ Implementadas
- ✅ **Sistema de Imóveis**: CRUD completo de propriedades
- ✅ **Interface Responsiva**: Design moderno com Bootstrap 5
- ✅ **Integração WhatsApp**: Botões de contato direto nos imóveis
- ✅ **Formulário de Contato**: Captação de leads
- ✅ **Painel Administrativo**: Interface completa para gerenciar imóveis
- ✅ **Sistema de Usuários**: Autenticação e perfis de corretores
- ✅ **Sistema de Favoritos**: Usuários podem favoritar imóveis (AJAX)
- ✅ **Carousel de Imóveis**: Destaques na página inicial
- ✅ **Perfil do Usuário**: Página pessoal com imóveis favoritados
- ✅ **Templates Dinâmicos**: Páginas responsivas e otimizadas
- ✅ **Newsletter**: Sistema de inscrição para novidades
- ✅ **Seção do Corretor**: Perfil profissional com foto personalizada

### 🔄 Próximas Implementações
- 🔄 **Empreendimentos**: Sistema de lançamentos imobiliários
- 🔄 **Busca Avançada**: Filtros por preço, localização, tipo
- 🔄 **Galeria de Imagens**: Múltiplas fotos por imóvel
- 🔄 **API WhatsApp Business**: Integração profissional
- 🔄 **Sistema de Mensagens**: Comunicação interna

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.6
- **Frontend**: Bootstrap 5.1.3 + Font Awesome 6.0.0
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Linguagem**: Python 3.13
- **Integração**: WhatsApp Web API

## 📦 Instalação e Configuração

### 1. Clonagem do Repositório
```bash
git clone <url-do-repositorio>
cd meuimobiliaria
```

### 2. Ambiente Virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Dependências
```bash
pip install -r requirements.txt
```

### 4. Migrações do Banco
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Popular Banco de Dados (Dados de Exemplo)
```bash
python populate_data.py
```

### 6. Executar Servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## 👥 Usuários de Teste

### Administrador
- **Usuário**: admin
- **Senha**: admin123
- **Acesso**: http://127.0.0.1:8000/admin/

### Corretores
- **corretor1** (João Silva) - senha: senha123
- **corretor2** (Maria Santos) - senha: senha123
- **corretor3** (Pedro Oliveira) - senha: senha123

## 📱 Integração WhatsApp

### Como Configurar
1. Acesse o painel admin
2. Vá para "Imóveis" > "Properties"
3. Adicione ou edite um imóvel
4. No campo "WhatsApp", insira o número no formato: `5511999999999`
5. Salve o imóvel

### Funcionamento
- Botão verde "Falar no WhatsApp" aparece automaticamente
- Mensagem pré-definida: "Olá! Tenho interesse no imóvel: [Nome] - R$ [Preço]. Podemos conversar?"
- Link direto para WhatsApp Web ou app

## 📁 Estrutura do Projeto

```
meuimobiliaria/
├── imoveis/                    # App principal
│   ├── models.py              # Modelos (Property, Favorite)
│   ├── views.py               # Views (property_list, property_detail, profile, auth)
│   ├── urls.py                # URLs do app
│   ├── forms.py               # Formulários de contato
│   ├── admin.py               # Configuração do admin
│   └── migrations/            # Migrações do banco
├── templates/
│   └── imoveis/              # Templates HTML
│       ├── base.html         # Template base com navegação
│       ├── home.html         # Página inicial com carousel
│       ├── property_list.html # Lista de imóveis
│       ├── property_detail.html # Detalhes do imóvel
│       ├── login.html        # Página de login
│       ├── register.html     # Página de registro
│       └── profile.html      # Perfil do usuário
├── meuimobiliaria/           # Configurações do projeto
│   ├── settings.py           # Configurações Django
│   ├── urls.py               # URLs principais
│   └── wsgi.py               # Configuração WSGI
├── media/
│   └── properties/           # Imagens dos imóveis
├── populate_data.py          # Script para popular BD
├── WHATSAPP_INTEGRATION.md   # Documentação WhatsApp
├── TODO.md                   # Lista de tarefas
└── manage.py                 # Comando Django
```

## 🎨 Páginas do Site

### Página Inicial (`/`)
- Carousel de imóveis em destaque
- Seção do corretor Cristiano Domingues
- Valores da empresa (segurança, excelência, confiança)
- Imóveis em destaque
- Navegação principal responsiva

### Lista de Imóveis (`/imoveis/`)
- Grid responsivo de imóveis
- Cards com informações principais
- Botão WhatsApp em cada imóvel
- Filtros por preço, cidade e tipo
- Sistema de paginação

### Detalhes do Imóvel (`/imoveis/<id>/`)
- Galeria de imagens
- Informações completas do imóvel
- Formulário de contato
- Botão WhatsApp
- Botão de favoritar (para usuários logados)
- Localização e mapa

### Sistema de Autenticação
- **Login** (`/login/`): Página de login elegante
- **Registro** (`/register/`): Formulário de cadastro de usuário
- **Logout**: Funcionalidade de sair da conta

### Perfil do Usuário (`/profile/`)
- Lista de imóveis favoritados
- Opção de remover favoritos
- Informações do perfil
- Navegação personalizada

### Painel Admin (`/admin/`)
- Gerenciamento completo de imóveis
- Sistema de usuários
- Gerenciamento de favoritos
- Estatísticas básicas

## 🔧 Configurações Importantes

### Settings.py
```python
# Arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imoveis',
]
```

### URLs Principais
```python
# meuimobiliaria/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imoveis.urls')),
]
```

## 📊 Dados de Exemplo

O script `populate_data.py` cria:
- **4 usuários**: 1 admin + 3 corretores
- **6 imóveis**: Apartamentos, casas, cobertura, studio
- **Números WhatsApp**: Para teste da integração


