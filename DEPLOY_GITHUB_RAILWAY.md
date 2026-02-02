# 🚀 GUIA RÁPIDO: GITHUB + RAILWAY

## 📦 ARQUIVOS NECESSÁRIOS (Todos já criados!)

✅ **rafabot_integration.py** - Código principal
✅ **requirements.txt** - Dependências Python
✅ **Procfile** - Configuração para deploy
✅ **runtime.txt** - Versão do Python
✅ **README_INTEGRACAO.md** - Documentação (opcional)
✅ **GUIA_COMPLETO.md** - Guia completo (opcional)

---

## 📋 PASSO A PASSO COMPLETO

### **PARTE 1: CRIAR REPOSITÓRIO NO GITHUB** (5 minutos)

#### 1. Acesse GitHub
- Vá para: https://github.com/
- Se não tem conta: clique em "Sign up" (criar conta grátis)
- Se já tem conta: faça login

#### 2. Criar Novo Repositório
- Clique no **botão verde "New"** (canto superior esquerdo)
- Ou acesse: https://github.com/new

#### 3. Preencher Informações
```
Repository name: rafabot-genspark-integration
Description: Integração Rafabot com Genspark AI
✅ Public (pode ser público, não tem dados sensíveis visíveis)
✅ Marque: "Add a README file"
```
- Clique em **"Create repository"**

#### 4. Fazer Upload dos Arquivos
Existem 2 formas:

**FORMA A - Pelo Site (Mais Fácil):**
1. Na página do repositório criado, clique em **"Add file"** → **"Upload files"**
2. Arraste os arquivos que eu criei:
   - `rafabot_integration.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
3. No campo de commit, escreva: "Integração inicial"
4. Clique em **"Commit changes"**

**FORMA B - Via Git (Linha de Comando):**
```bash
# Se você tem Git instalado
git clone https://github.com/SEU_USUARIO/rafabot-genspark-integration.git
cd rafabot-genspark-integration
# Copie os arquivos para esta pasta
git add .
git commit -m "Integração inicial"
git push
```

---

### **PARTE 2: DEPLOY NO RAILWAY** (3 minutos)

#### 1. Acesse Railway
- Vá para: https://railway.app/
- Clique em **"Login"**
- Escolha **"Login with GitHub"**
- Autorize o Railway a acessar seu GitHub

#### 2. Criar Novo Projeto
- Clique em **"New Project"**
- Selecione **"Deploy from GitHub repo"**
- Escolha o repositório: **rafabot-genspark-integration**
- Clique para confirmar

#### 3. Railway Detecta Automaticamente
- Railway vai ver os arquivos e detectar que é Python
- Vai instalar dependências automaticamente
- Em 1-2 minutos, estará rodando!

#### 4. Obter URL Pública
- Clique no projeto criado
- Vá na aba **"Settings"**
- Role até **"Networking"** ou **"Domains"**
- Clique em **"Generate Domain"**
- Copie a URL gerada (tipo: `https://seu-projeto.up.railway.app`)

---

### **PARTE 3: CONFIGURAR NO RAFABOT** (2 minutos)

#### 1. Acesse o Painel Rafabot
- Vá para: https://apprafaelseguros.rafabot.com/

#### 2. Ir para Configurações de API
- Menu → Configurações → Integrações → API
- Localize a configuração "Genspark AI Agent" que você criou

#### 3. Configurar Webhook
```
URL do Webhook: https://SEU-PROJETO.up.railway.app/webhook
```
- Substitua `SEU-PROJETO` pela URL que o Railway gerou
- Salve as configurações

---

## ✅ TESTAR A INTEGRAÇÃO

### Teste 1: Verificar se está online
Abra no navegador:
```
https://SEU-PROJETO.up.railway.app/health
```

Deve aparecer:
```json
{
  "status": "online",
  "service": "Rafabot <-> Genspark Integration"
}
```

### Teste 2: Enviar mensagem real
- Mande uma mensagem para o número do Rafabot via WhatsApp
- A IA deve responder automaticamente!

---

## 📊 MONITORAR LOGS

No Railway:
1. Clique no seu projeto
2. Vá na aba **"Deployments"**
3. Clique no deployment ativo
4. Veja os logs em tempo real!

Você verá mensagens tipo:
```
[2026-02-02 19:00:00] [WEBHOOK] Dados recebidos: {...}
[2026-02-02 19:00:01] [GENSPARK] Processando: Olá
[2026-02-02 19:00:02] [SUCESSO] Resposta enviada!
```

---

## 🎯 RESUMO ULTRA-RÁPIDO

1. **GitHub:** Criar repositório → Upload dos 4 arquivos
2. **Railway:** Login com GitHub → Deploy do repositório → Copiar URL
3. **Rafabot:** Configurar webhook com a URL do Railway
4. **Testar:** Mandar mensagem no WhatsApp

**TEMPO TOTAL: ~10 minutos** ⚡

---

## 🆘 SE DER ERRO

### Erro no Railway:
- Verifique os logs na aba "Deployments"
- Certifique-se que todos os 4 arquivos foram enviados

### Erro no Rafabot:
- Verifique se a URL do webhook está correta
- Teste a URL /health no navegador primeiro

### Precisa de ajuda:
- Tire print da tela onde está o erro
- Me mostre e eu te ajudo!

---

## 📁 ONDE ESTÃO OS ARQUIVOS

Todos os arquivos necessários estão em:
`/mnt/user-data/outputs/rafabot-integration/`

Arquivos obrigatórios:
- ✅ rafabot_integration.py
- ✅ requirements.txt  
- ✅ Procfile
- ✅ runtime.txt

---

## 💡 DICA IMPORTANTE

Você **NÃO precisa** me passar nenhuma senha ou credencial do GitHub ou Railway!

Eu só preciso que você:
1. Faça upload dos arquivos no GitHub
2. Conecte o Railway
3. Me passe a **URL final** que o Railway gerou

Aí eu te ajudo a testar e configurar! 🚀
