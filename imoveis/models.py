from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    address = models.CharField(max_length=300, verbose_name="Endereço")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    state = models.CharField(max_length=100, verbose_name="Estado")
    zip_code = models.CharField(max_length=20, verbose_name="CEP")
    bedrooms = models.IntegerField(verbose_name="Quartos")
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Banheiros")
    area = models.IntegerField(verbose_name="Área (m²)")
    image = models.ImageField(upload_to='properties/', blank=True, null=True, verbose_name="Imagem")
    is_available = models.BooleanField(default=True, verbose_name="Disponível")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
        ordering = ['-created_at']

class Contact(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="Imóvel")
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    message = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")

    def __str__(self):
        return f"Contato de {self.name} - {self.property.title}"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['-created_at']
