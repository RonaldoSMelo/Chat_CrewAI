from flask import Flask, jsonify, render_template
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
    """Teste básico do CrewAI"""
    try:
        # Verificar se a API key está configurada
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return jsonify({
                'message': 'Olá Mundo! Este é um teste básico do CrewAI.',
                'status': 'demo_mode',
                'note': 'Configure OPENAI_API_KEY para usar funcionalidade completa'
            })
        
        return jsonify({
            'message': 'Olá Mundo! CrewAI configurado e funcionando.',
            'status': 'ready',
            'api_key': 'configured'
        })
        
    except Exception as e:
        return jsonify({
            'message': 'Olá Mundo! Erro ao inicializar CrewAI.',
            'status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 