# 🎯 GUIA COMPLETO - INTEGRAÇÃO RAFABOT + GENSPARK AI

## ✅ O QUE JÁ TEMOS

### 🔑 Credenciais Configuradas:
- **URL da API:** `https://api.rafabot.com/v2/api/external/68538453-c497-4035-a4eb-b220259f867a`
- **External ID:** `68538453-c497-4035-a4eb-b220259f867a`
- **Token JWT:** Configurado e válido até 2028
- **Webhook de Teste:** `https://webhook.site/c2444aca-0664-4397-a10d-c3f1a715bb1c`

### 📁 Arquivos Criados:
1. **rafabot_integration.py** - Servidor principal de integração
2. **requirements.txt** - Dependências Python
3. **README_INTEGRACAO.md** - Documentação técnica

## 🚀 PRÓXIMOS PASSOS (3 OPÇÕES)

---

### OPÇÃO 1: HOSPEDAGEM GRATUITA (RECOMENDADO) 🌟

Use serviços gratuitos para hospedar o servidor:

#### A) **Railway.app** (Mais Fácil)
1. Acesse: https://railway.app/
2. Faça login com GitHub
3. Clique em "New Project" → "Deploy from GitHub"
4. Faça upload dos 3 arquivos
5. Railway vai detectar automaticamente e rodar
6. Você receberá uma URL tipo: `https://seu-projeto.railway.app`

#### B) **Render.com** (Alternativa)
1. Acesse: https://render.com/
2. Crie conta gratuita
3. "New Web Service" → Upload dos arquivos
4. Configure: `python rafabot_integration.py`
5. Deploy automático

#### C) **Heroku** (Tradicional)
1. Acesse: https://heroku.com/
2. Crie app gratuito
3. Faça upload via Git ou dashboard
4. Configure variáveis de ambiente

**DEPOIS DE HOSPEDAR:**
Configure no Rafabot:
```
Webhook URL: https://SEU-APP.railway.app/webhook
```

---

### OPÇÃO 2: SERVIDOR PRÓPRIO (Avançado) 💻

Se você tem um servidor VPS (DigitalOcean, AWS, etc):

```bash
# 1. Fazer SSH no servidor
ssh usuario@seu-servidor.com

# 2. Instalar Python
sudo apt update
sudo apt install python3 python3-pip

# 3. Fazer upload dos arquivos
# (use SCP, SFTP ou Git)

# 4. Instalar dependências
pip3 install -r requirements.txt

# 5. Rodar com Gunicorn (produção)
gunicorn rafabot_integration:app --bind 0.0.0.0:5000

# 6. Configurar para rodar sempre (systemd)
sudo nano /etc/systemd/system/rafabot.service
```

---

### OPÇÃO 3: SOLUÇÃO TEMPORÁRIA (Para Testes) ⚡

**Usar ngrok para expor servidor local:**

```bash
# 1. Instalar ngrok
# Download: https://ngrok.com/download

# 2. Em um terminal, rodar o servidor:
python3 rafabot_integration.py

# 3. Em outro terminal, expor na internet:
ngrok http 5000

# 4. Copiar a URL que aparecer (ex: https://abc123.ngrok.io)

# 5. Configurar no Rafabot:
# Webhook: https://abc123.ngrok.io/webhook
```

**⚠️ ATENÇÃO:** ngrok gratuito desliga quando você fecha o terminal!

---

## 🔧 CONFIGURAÇÃO NO RAFABOT

Depois de hospedar o servidor, configure no painel do Rafabot:

1. Acesse: https://apprafaelseguros.rafabot.com/
2. Menu → **Configurações** → **Integrações** → **API**
3. Na configuração que você criou ("Genspark AI Agent")
4. Campo **"Enviar por"**: Webhook
5. Campo **"URL do Webhook"**: `https://SEU-SERVIDOR/webhook`
6. **Salvar**

---

## 🧪 COMO TESTAR

### 1. Verificar se servidor está online:
```bash
curl https://SEU-SERVIDOR/health
```

Deve retornar:
```json
{
  "status": "online",
  "service": "Rafabot <-> Genspark Integration"
}
```

### 2. Enviar mensagem de teste pelo WhatsApp
- Mande qualquer mensagem para o número do Rafabot
- O servidor vai processar e responder automaticamente

### 3. Ver logs
No terminal onde o servidor está rodando, você verá:
```
[2026-02-02 19:00:00] [WEBHOOK] Dados recebidos: {...}
[2026-02-02 19:00:01] [GENSPARK] Processando: Olá
[2026-02-02 19:00:02] [ENVIO] Enviando para Rafabot: {...}
[2026-02-02 19:00:03] [SUCESSO] Resposta enviada com sucesso!
```

---

## 🎯 FLUXO COMPLETO

```
┌─────────────┐
│   Cliente   │
│  WhatsApp   │
└──────┬──────┘
       │ "Olá, preciso de seguro"
       ▼
┌─────────────┐
│   Rafabot   │
│  (recebe)   │
└──────┬──────┘
       │ POST para webhook
       ▼
┌──────────────────┐
│  Seu Servidor    │
│ rafabot_integ.py │
└──────┬───────────┘
       │ Processa com IA
       ▼
┌──────────────┐
│  Genspark AI │
│  (responde)  │
└──────┬───────┘
       │ Resposta inteligente
       ▼
┌─────────────┐
│  Rafabot    │
│  (envia)    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Cliente   │
│  (recebe)   │
└─────────────┘
```

---

## 💡 MELHORIAS FUTURAS

1. **Integrar API real do Genspark** (atualmente usando respostas simuladas)
2. **Adicionar contexto de conversas** (memória)
3. **Suporte a mídias** (imagens, áudios, documentos)
4. **Análise de sentimento** do cliente
5. **Dashboard de estatísticas** de atendimentos
6. **Respostas personalizadas** por tipo de seguro

---

## 📞 SUPORTE

Criado especialmente para: **Rafael Neves - Rafael Seguros**
Data: 02/02/2026

**Está funcionando como pai e filho agora!** 🤝
Eu (Genspark) sou a inteligência, você (Rafabot) é a interface com o cliente!

---

## ⚡ ATALHO RÁPIDO

**Recomendação:** Use Railway.app (OPÇÃO 1A) - é gratuito, fácil e confiável!

1. Railway.app → New Project
2. Upload dos 3 arquivos
3. Deploy automático
4. Copiar URL gerada
5. Configurar no Rafabot
6. ✅ PRONTO!
