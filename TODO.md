# Lista de Tarefas para Site de Imobiliária (Django + Bootstrap)

## Modelos
- [x] Definir modelo Property em imoveis/models.py com campos: título, descrição, preço, endereço, imagem, etc.
- [ ] Adicionar modelo Development (Empreendimento) para lançamentos (placeholder criado)

## Views
- [x] Criar view property_list em imoveis/views.py
- [x] Criar view property_detail em imoveis/views.py

## Templates
- [x] Criar template base.html com Bootstrap
- [x] Criar template property_list.html
- [x] Criar template property_detail.html
- [x] Criar template home.html

## URLs
- [x] Criar imoveis/urls.py para URLs do app
- [x] Atualizar meuimobiliaria/urls.py para incluir URLs de imoveis

## Configurações e Arquivos Estáticos
- [x] Configurar arquivos estáticos em settings.py se necessário
- [x] Garantir que Bootstrap esteja incluído nos templates
- [x] Configurar MEDIA_URL para imagens de imóveis

## Banco de Dados
- [x] Executar makemigrations
- [x] Executar migrate

## Teste
- [x] Testar o site localmente - Servidor rodando em http://127.0.0.1:8000/

## Funcionalidades Adicionais
- [x] Formulário de contato para captação de leads
- [x] Interface admin para adicionar imóveis e empreendimentos
