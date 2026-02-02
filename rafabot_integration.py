#!/usr/bin/env python3
"""
Servidor de Integração Rafabot <-> Genspark AI
Criado para Rafael Neves - Rafael Seguros
"""

from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

# Configurações do Rafabot
RAFABOT_API_URL = "https://api.rafabot.com/v2/api/external/68538453-c497-4035-a4eb-b220259f867a"
RAFABOT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6MSwicHJvZmlsZSI6ImFkbWluIiwiaWF0IjoxNzcwMDYxMDUyLCJleHAiOjE4MzMxMzMwNTJ9.rzITgu-o6EEcKE0Tzw6PGIfD51YlD3eXxdg6Hz4XLJk"

# Headers para autenticação
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {RAFABOT_TOKEN}"
}

def log_message(tipo, mensagem):
    """Log com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{tipo}] {mensagem}")

def process_with_genspark(message_text, sender_info):
    """
    Aqui seria a integração com Genspark API
    Por enquanto, vou simular respostas inteligentes
    """
    log_message("GENSPARK", f"Processando: {message_text}")
    
    # Respostas simuladas (você pode integrar com API do Genspark aqui)
    response = f"🤖 Olá! Sou o assistente IA do Rafael Seguros.\n\n"
    response += f"Recebi sua mensagem: '{message_text}'\n\n"
    response += f"Como posso ajudá-lo com seguros hoje?"
    
    return response

def send_to_rafabot(message_data):
    """Envia resposta de volta para o Rafabot"""
    try:
        log_message("ENVIO", f"Enviando para Rafabot: {json.dumps(message_data, indent=2)}")
        
        response = requests.post(
            RAFABOT_API_URL,
            headers=HEADERS,
            json=message_data,
            timeout=10
        )
        
        log_message("RESPOSTA", f"Status: {response.status_code} | Body: {response.text}")
        return response.status_code == 200
        
    except Exception as e:
        log_message("ERRO", f"Erro ao enviar para Rafabot: {str(e)}")
        return False

@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    """Recebe mensagens do Rafabot via webhook"""
    try:
        # Recebe dados do webhook
        data = request.get_json()
        log_message("WEBHOOK", f"Dados recebidos: {json.dumps(data, indent=2)}")
        
        # Extrai informações da mensagem
        # NOTA: O formato pode variar, ajustar conforme a estrutura real
        message_text = data.get('message', {}).get('text', '') or data.get('body', '')
        sender = data.get('from', {}).get('name', 'Cliente') or data.get('sender', 'Cliente')
        chat_id = data.get('chatId', '') or data.get('chat_id', '')
        
        if not message_text:
            log_message("AVISO", "Mensagem sem texto, ignorando")
            return jsonify({"status": "ignored", "reason": "no_text"}), 200
        
        log_message("RECEBIDO", f"De: {sender} | Mensagem: {message_text}")
        
        # Processa com IA
        ai_response = process_with_genspark(message_text, sender)
        
        # Prepara resposta para enviar de volta
        response_data = {
            "chatId": chat_id,
            "message": ai_response,
            "type": "text"
        }
        
        # Envia resposta
        success = send_to_rafabot(response_data)
        
        if success:
            log_message("SUCESSO", "Resposta enviada com sucesso!")
            return jsonify({"status": "success", "message": "Response sent"}), 200
        else:
            log_message("FALHA", "Falha ao enviar resposta")
            return jsonify({"status": "error", "message": "Failed to send response"}), 500
            
    except Exception as e:
        log_message("ERRO", f"Erro no webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de saúde"""
    return jsonify({
        "status": "online",
        "service": "Rafabot <-> Genspark Integration",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/test', methods=['POST'])
def test_endpoint():
    """Endpoint de teste"""
    data = request.get_json()
    log_message("TESTE", f"Teste recebido: {json.dumps(data, indent=2)}")
    return jsonify({"status": "test_received", "data": data}), 200

if __name__ == '__main__':
    log_message("INICIO", "🚀 Servidor de Integração Rafabot iniciando...")
    log_message("INFO", f"Webhook URL: https://api.rafabot.com/v2/api/external/68538453-c497-4035-a4eb-b220259f867a")
    log_message("INFO", "Servidor rodando na porta 5000")
    print("\n" + "="*60)
    print("📱 CONFIGURE NO RAFABOT:")
    print(f"   Webhook URL: http://SEU_SERVIDOR:5000/webhook")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
