# 📱 Integração com WhatsApp - Luxury Realty

## Visão Geral
A integração com WhatsApp permite que os visitantes do site entrem em contato diretamente com os corretores através do WhatsApp, facilitando a comunicação e aumentando as chances de conversão.

## Como Funciona

### 1. **Campo WhatsApp no Admin**
- No painel administrativo, ao criar/editar um imóvel, há um campo chamado "WhatsApp"
- Formato esperado: `5511999999999` (código do país + DDD + número)
- O campo aceita apenas números, removendo automaticamente caracteres especiais

### 2. **Botão "Falar no WhatsApp"**
- Aparece automaticamente nos cards da lista de imóveis
- Aparece na página de detalhes do imóvel
- Só é exibido se o imóvel tiver um número de WhatsApp cadastrado

### 3. **Mensagem Automática**
Quando o usuário clica no botão, é aberta uma conversa no WhatsApp com a seguinte mensagem pré-definida:

```
Olá! Tenho interesse no imóvel: [Nome do Imóvel] - R$ [Preço]. Podemos conversar?
```

## Como Configurar

### Passo 1: Adicionar Número do WhatsApp
1. Acesse o admin: `http://127.0.0.1:8000/admin/`
2. Faça login com suas credenciais
3. Vá para "Imóveis" > "Properties"
4. Clique em um imóvel existente ou crie um novo
5. No campo "WhatsApp", digite o número no formato: `5511999999999`
6. Salve o imóvel

### Passo 2: Testar a Integração
1. Acesse a página de imóveis: `http://127.0.0.1:8000/imoveis/`
2. Clique no botão verde "Falar no WhatsApp" em qualquer imóvel
3. Verifique se o WhatsApp Web ou app abre com a mensagem correta

## Funcionalidades Técnicas

### Modelo Property Atualizado
```python
class Property(models.Model):
    # ... outros campos ...
    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="WhatsApp",
        help_text="Número do WhatsApp (ex: 5511999999999)"
    )

    def get_whatsapp_link(self):
        """Gera link do WhatsApp com mensagem pré-definida"""
        if self.whatsapp_number:
            number = ''.join(filter(str.isdigit, self.whatsapp_number))
            message = f"Olá! Tenho interesse no imóvel: {self.title} - R$ {self.price:,.2f}. Podemos conversar?"
            encoded_message = message.replace(' ', '%20').replace('\n', '%0A')
            return f"https://wa.me/{number}?text={encoded_message}"
        return None
```

### Template com Botão WhatsApp
```html
{% if property.whatsapp_number and property.get_whatsapp_link %}
<a href="{{ property.get_whatsapp_link }}" target="_blank" class="btn btn-success">
    <i class="fab fa-whatsapp me-2"></i>Falar no WhatsApp
</a>
{% endif %}
```

## Benefícios

✅ **Contato Direto**: Elimina intermediários na comunicação
✅ **Resposta Rápida**: WhatsApp permite resposta imediata
✅ **Conversão**: Aumenta as chances de fechar negócio
✅ **Praticidade**: Usuário não precisa copiar/colar informações
✅ **Mobile-Friendly**: Funciona perfeitamente em dispositivos móveis

## Dicas de Uso

1. **Use sempre o formato internacional**: `5511999999999`
2. **Teste cada número**: Certifique-se de que o WhatsApp está ativo
3. **Atualize regularmente**: Mantenha os números atualizados
4. **Monitore as conversas**: Use o WhatsApp Business para analytics

## Solução de Problemas

### Botão não aparece
- Verifique se o campo WhatsApp está preenchido no admin
- Certifique-se de que o número está no formato correto

### Link não funciona
- Verifique se o número do WhatsApp está correto
- Teste o link manualmente: `https://wa.me/5511999999999`

### Mensagem não é enviada
- O WhatsApp pode pedir confirmação para abrir links externos
- Certifique-se de que o WhatsApp está instalado no dispositivo

## Próximas Melhorias

- [ ] Integração com WhatsApp Business API
- [ ] Templates de mensagem personalizáveis
- [ ] Analytics de conversas iniciadas
- [ ] Suporte a múltiplos números por imóvel
- [ ] Horário comercial configurável

---
**Desenvolvido para maximizar a eficiência no contato com clientes em imóveis.**
