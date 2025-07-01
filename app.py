from flask import Flask, render_template, request, jsonify
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurar o modelo LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

def create_crew_response(user_message):
    """
    Cria uma resposta usando CrewAI baseada na mensagem do usuário
    """
    # Criar agentes
    researcher = Agent(
        role='Pesquisador',
        goal='Analisar e entender a mensagem do usuário',
        backstory='Você é um pesquisador experiente que analisa mensagens e fornece insights úteis.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    writer = Agent(
        role='Escritor',
        goal='Criar uma resposta clara e útil baseada na análise',
        backstory='Você é um escritor talentoso que transforma análises em respostas claras e úteis.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    # Criar tarefas
    research_task = Task(
        description=f"""
        Analise a seguinte mensagem do usuário e identifique:
        1. O que o usuário está perguntando ou solicitando
        2. O contexto da mensagem
        3. Qual seria a melhor abordagem para responder
        
        Mensagem do usuário: {user_message}
        """,
        expected_output="Uma análise detalhada da mensagem do usuário com identificação clara do que está sendo solicitado, contexto e abordagem recomendada para resposta.",
        agent=researcher
    )
    
    writing_task = Task(
        description="""
        Com base na análise anterior, crie uma resposta clara, útil e amigável.
        A resposta deve ser:
        - Direta e objetiva
        - Útil para o usuário
        - Escrita em português brasileiro
        - Com no máximo 3 parágrafos
        """,
        expected_output="Uma resposta clara, objetiva e útil em português brasileiro, com no máximo 3 parágrafos, que atenda diretamente à solicitação do usuário.",
        agent=writer
    )
    
    # Criar e executar o crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
        process=Process.sequential
    )
    
    result = crew.kickoff()
    return result

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/run', methods=['GET'])
def run():
    return jsonify({'status': 'running'})

@app.route('/process_message', methods=['POST'])
def process_message():
    """Processa a mensagem do usuário usando CrewAI"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensagem não fornecida'}), 400
        
        # Verificar se a API key está configurada
        if not os.getenv("OPENAI_API_KEY"):
            return jsonify({
                'response': 'Olá! Este é um projeto CrewAI de demonstração. Para usar a funcionalidade completa, configure sua chave da OpenAI no arquivo .env'
            })
        
        # Processar com CrewAI
        response = create_crew_response(user_message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': f'Erro ao processar mensagem: {str(e)}'}), 500

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Para produção no Render, usar: gunicorn app:app 