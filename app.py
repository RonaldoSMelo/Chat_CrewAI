from flask import Flask, jsonify, render_template, request
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['GET'])
@app.route('/run/', methods=['GET'])
def run():
    return jsonify({'status': 'running'}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'crewai-chat'}), 200

@app.route('/crewai-test', methods=['GET'])
def crewai_test():
    """Teste básico - sem CrewAI por enquanto"""
    try:
        # Verificar se a API key está configurada
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return jsonify({
                'message': 'Olá Mundo! Este é um teste básico.',
                'status': 'demo_mode',
                'note': 'CrewAI temporariamente desabilitado para evitar problemas de build'
            })
        
        return jsonify({
            'message': 'Olá Mundo! API Key configurada.',
            'status': 'ready',
            'api_key': 'configured',
            'note': 'CrewAI será adicionado em breve'
        })
        
    except Exception as e:
        return jsonify({
            'message': 'Olá Mundo! Erro no teste.',
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    # Resposta simulada
    response = f"Você disse: {user_message}. (Simulação CrewAI)"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 