#!/usr/bin/env python
"""
popular o banco de dados com dados de exemplo
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuimobiliaria.settings')
django.setup()

from django.contrib.auth.models import User
from imoveis.models import Property

def create_users():
    """Cria usuários corretor"""
    print("Criando usuários...")

    # Criar superusuário
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@imobiliaria.com', 'admin123')
        print("✓ Superusuário 'admin' criado (senha: admin123)")

    # Criar corretores
    corretores = [
        {'username': 'corretor1', 'email': 'corretor1@imobiliaria.com', 'first_name': 'João', 'last_name': 'Silva'},
        {'username': 'corretor2', 'email': 'corretor2@imobiliaria.com', 'first_name': 'Maria', 'last_name': 'Santos'},
        {'username': 'corretor3', 'email': 'corretor3@imobiliaria.com', 'first_name': 'Pedro', 'last_name': 'Oliveira'},
    ]

    for corretor_data in corretores:
        if not User.objects.filter(username=corretor_data['username']).exists():
            user = User.objects.create_user(
                username=corretor_data['username'],
                email=corretor_data['email'],
                password='senha123',
                first_name=corretor_data['first_name'],
                last_name=corretor_data['last_name']
            )
            print(f"✓ Corretor '{user.get_full_name()}' criado (usuário: {user.username}, senha: senha123)")

def create_properties():
    """Cria imóveis de exemplo"""
    print("\nCriando imóveis...")

    properties_data = [
        {
            'title': 'Apartamento 3 Quartos - Centro',
            'description': 'Excelente apartamento no coração da cidade, próximo ao metrô e comércio. 3 quartos sendo 1 suíte, sala ampla, cozinha planejada, 2 vagas de garagem.',
            'price': 450000.00,
            'address': 'Rua das Flores, 123',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01234-567',
            'bedrooms': 3,
            'bathrooms': 2.0,
            'area': 85,
            'image': 'properties/casa3.jpeg',
            'whatsapp_number': '5511999999999',
            'rental_type': 'compra',
        },
        {
            'title': 'Casa com Piscina - Jardim América',
            'description': 'Linda casa com 4 quartos, piscina, jardim, 3 vagas. Área total de 300m². Perfeita para família.',
            'price': 850000.00,
            'address': 'Av. Brasil, 456',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01456-789',
            'bedrooms': 4,
            'bathrooms': 3.0,
            'area': 300,
            'image': 'properties/casa4.jpg',
            'whatsapp_number': '5511988888888',
            'rental_type': 'compra',
        },
        {
            'title': 'Cobertura Duplex - Vila Madalena',
            'description': 'Cobertura duplex com vista panorâmica, 3 quartos, terraço de 50m², acabamento de alto padrão.',
            'price': 1200000.00,
            'address': 'Rua Harmonia, 789',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '05435-123',
            'bedrooms': 3,
            'bathrooms': 2.5,
            'area': 180,
            'image': 'properties/casa5.webp',
            'whatsapp_number': '5511977777777',
            'rental_type': 'compra',
        },
        {
            'title': 'Studio Moderno - Pinheiros',
            'description': 'Studio compacto e moderno, ideal para jovens profissionais. Mobiliado, com academia e segurança 24h.',
            'price': 280000.00,
            'address': 'Rua dos Pinheiros, 321',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '05422-001',
            'bedrooms': 1,
            'bathrooms': 1.0,
            'area': 35,
            'image': 'properties/casa6.jpg',
            'whatsapp_number': '5511966666666',
            'rental_type': 'aluguel',
        },
        {
            'title': 'Casa de Praia - Ubatuba',
            'description': 'Casa de praia com 3 quartos, vista para o mar, piscina, churrasqueira. Perfeita para férias e investimento.',
            'price': 650000.00,
            'address': 'Av. Beira Mar, 1000',
            'city': 'Ubatuba',
            'state': 'SP',
            'zip_code': '11680-000',
            'bedrooms': 3,
            'bathrooms': 2.0,
            'area': 150,
            'image': 'properties/casa7.jpg',
            'whatsapp_number': '5511955555555',
            'rental_type': 'compra',
        },
        {
            'title': 'Apartamento 2 Quartos - Moema',
            'description': 'Apartamento reformado, 2 quartos, sala, cozinha americana, 1 vaga. Próximo ao shopping e parques.',
            'price': 380000.00,
            'address': 'Alameda Santos, 2000',
            'city': 'São Paulo',
            'state': 'SP',
            'zip_code': '01418-200',
            'bedrooms': 2,
            'bathrooms': 1.0,
            'area': 65,
            'image': 'properties/casa8.webp',
            'whatsapp_number': '5511944444444',
            'rental_type': 'compra',
        },
    ]

    for prop_data in properties_data:
        property_obj, created = Property.objects.get_or_create(
            title=prop_data['title'],
            defaults=prop_data
        )
        if created:
            print(f"✓ Imóvel '{property_obj.title}' criado - R$ {property_obj.price:,.2f}")
        else:
            # Update existing property with image if it doesn't have one
            if not property_obj.image and 'image' in prop_data:
                property_obj.image = prop_data['image']
                property_obj.save()
                print(f"✓ Imóvel '{property_obj.title}' atualizado com imagem")

def main():
    """Função principal"""
    print("Populando banco de dados com dados de exemplo...\n")

    try:
        create_users()
        create_properties()

        print("\n✅ Dados populados com sucesso!")
        print(f"\n📊 Resumo:")
        print(f"   Usuários criados: {User.objects.count()}")
        print(f"   Imóveis criados: {Property.objects.count()}")

        print("\n🔐 Credenciais de acesso:")
        print("   Admin: admin / admin123")
        print("   Corretores: corretor1, corretor2, corretor3 / senha123")

        print("\n🌐 Acesse:")
        print("   Site: http://127.0.0.1:8000/")
        print("   Admin: http://127.0.0.1:8000/admin/")

    except Exception as e:
        print(f" Erro ao popular dados: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
