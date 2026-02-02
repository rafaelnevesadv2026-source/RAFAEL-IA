# 🤖 Integração Rafabot <-> Genspark AI

## 📋 Visão Geral

Este servidor atua como ponte entre o Rafabot e a IA Genspark, permitindo que todas as mensagens dos clientes sejam processadas automaticamente pela inteligência artificial.

## 🔧 Configuração

### Dados da Integração:
- **API Rafabot:** `https://api.rafabot.com/v2/api/external/68538453-c497-4035-a4eb-b220259f867a`
- **External ID:** `68538453-c497-4035-a4eb-b220259f867a`
- **Token JWT:** Configurado no código

### Fluxo de Funcionamento:

```
Cliente → Rafabot → Webhook → Servidor Python → Genspark AI → Resposta → Rafabot → Cliente
```

## 🚀 Como Usar

### 1. Instalar Dependências:
```bash
pip install -r requirements.txt
```

### 2. Rodar o Servidor:
```bash
python rafabot_integration.py
```

### 3. Configurar no Rafabot:
No painel do Rafabot, configure o webhook para apontar para:
```
http://SEU_SERVIDOR_IP:5000/webhook
```

## 🌐 Endpoints Disponíveis

### `/webhook` (POST)
Recebe mensagens do Rafabot e processa com IA

### `/health` (GET)
Verifica se o servidor está online

### `/test` (POST)
Endpoint de teste para debug

## 📝 Formato de Dados

### Entrada (do Rafabot):
```json
{
  "chatId": "123456",
  "message": {
    "text": "Olá, preciso de ajuda"
  },
  "from": {
    "name": "Cliente"
  }
}
```

### Saída (para Rafabot):
```json
{
  "chatId": "123456",
  "message": "Resposta da IA",
  "type": "text"
}
```

## 🔐 Segurança

- Token JWT configurado para autenticação
- Logs detalhados de todas as operações
- Timeout de 10s para requisições

## 🎯 Próximos Passos

1. ✅ Servidor criado
2. ⏳ Hospedar em servidor público (Heroku, Railway, DigitalOcean)
3. ⏳ Configurar webhook no Rafabot
4. ⏳ Testar integração
5. ⏳ Integrar API real do Genspark

## 📞 Suporte

Criado para: Rafael Neves - Rafael Seguros
Data: 2026-02-02
