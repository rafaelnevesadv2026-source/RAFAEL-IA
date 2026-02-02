#!/usr/bin/env python3
"""
Servidor de Integração Rafabot <-> Genspark AI
Aguarda mensagens do Rafabot e processa com IA
"""

from flask import Flask, request, jsonify
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

# ========== CONFIGURAÇÕES ==========
RAFABOT_API_URL = "https://api.rafabot.com/v2/api/external/68538453-c497-4035-a4eb-b220259f867a"
RAFABOT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6MSwicHJvZmlsZSI6ImFkbWluIiwiaWF0IjoxNzcwMDYxMDUyLCJleHAiOjE4MzMxMzMwNTJ9.rzITgu-o6EEcKE0Tzw6PGIfD51YlD3eXxdg6Hz4XLJk"

# ========== ROTAS ==========

@app.route('/', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        "status": "✅ Genspark AI Agent está online!",
        "timestamp": datetime.now().isoformat(),
        "service": "Integração Rafabot ↔ Genspark"
    }), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Recebe mensagens do Rafabot
    Processa com IA Genspark
    Envia resposta de volta
    """
    try:
        # Receber dados do Rafabot
        data = request.get_json()
        
        print(f"📥 Mensagem recebida do Rafabot:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        
        # Extrair informações
        chat_id = data.get('chatId', '')
        message_text = data.get('message', {}).get('text', '')
        sender_name = data.get('from', {}).get('name', 'Cliente')
        
        # ========== PROCESSAR COM IA ==========
        # Aqui você pode integrar a lógica da IA Genspark
        # Por enquanto, vou gerar uma resposta padrão
        
        ai_response = gerar_resposta_ia(message_text, sender_name)
        
        # ========== ENVIAR RESPOSTA PARA RAFABOT ==========
        response_payload = {
            "chatId": chat_id,
            "message": ai_response,
            "type": "text"
        }
        
        # Enviar para Rafabot
        headers = {
            "Authorization": f"Bearer {RAFABOT_TOKEN}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            RAFABOT_API_URL,
            json=response_payload,
            headers=headers,
            timeout=10
        )
        
        print(f"📤 Resposta enviada para Rafabot:")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
        
        return jsonify({
            "status": "✅ Mensagem processada com sucesso",
            "ai_response": ai_response,
            "rafabot_status": response.status_code
        }), 200
        
    except Exception as e:
        print(f"❌ ERRO: {str(e)}")
        return jsonify({
            "status": "❌ Erro ao processar mensagem",
            "error": str(e)
        }), 500

def gerar_resposta_ia(mensagem_cliente: str, nome_cliente: str) -> str:
    """
    Gera resposta usando lógica da IA Genspark
    Aqui você pode integrar chamadas para a API do Genspark
    ou adicionar lógica de IA customizada
    """
    
    # Resposta padrão para diferentes tipos de mensagens
    mensagem_lower = mensagem_cliente.lower()
    
    if not mensagem_cliente:
        return "Desculpe, não entendi sua mensagem. Pode tentar novamente?"
    
    if any(palavra in mensagem_lower for palavra in ['oi', 'olá', 'e aí', 'opa']):
        return f"🤖 Olá {nome_cliente}! Sou o assistente IA do Rafael Seguros. Como posso ajudá-lo hoje?"
    
    if any(palavra in mensagem_lower for palavra in ['seguro', 'cotação', 'preço']):
        return f"💼 Ótimo! Tenho várias opções de seguro para você:\n\n📋 Tipos disponíveis:\n• Automóvel\n• Residencial\n• Vida\n• Empresarial\n\nQual tipo de seguro você está buscando?"
    
    if any(palavra in mensagem_lower for palavra in ['obrigado', 'valeu', 'thanks']):
        return "De nada! 😊 Qualquer dúvida, é só chamar. Estou sempre aqui!"
    
    # Resposta padrão para qualquer outra mensagem
    return f"📞 Entendi! Você perguntou sobre: '{mensagem_cliente}'\n\nPara melhor atendê-lo, poderia detalhar mais sua necessidade? Estou aqui para ajudar!"

# ========== INICIAR SERVIDOR ==========
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*60)
    print("🤖 GENSPARK AI AGENT - SERVIDOR INICIADO")
    print("="*60)
    print(f"🌐 Servidor rodando em: http://localhost:{port}")
    print(f"📡 Webhook: http://localhost:{port}/webhook")
    print(f"💚 Health Check: http://localhost:{port}/")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)
