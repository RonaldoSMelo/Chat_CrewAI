# 🤖 CrewAI - Projeto de Demonstração

Este é um projeto simples que demonstra o uso do CrewAI com uma interface web moderna. O sistema usa múltiplos agentes para processar e responder mensagens dos usuários.

## 🚀 Funcionalidades

- **Interface Web Moderna**: Página HTML responsiva com design elegante
- **Múltiplos Agentes**: Sistema CrewAI com Pesquisador e Escritor
- **Processamento Inteligente**: Análise e resposta baseada em IA
- **API REST**: Endpoint para processamento de mensagens
- **Design Responsivo**: Funciona em desktop e mobile

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chave da API OpenAI (opcional, mas recomendado)

## 🛠️ Instalação

1. **Clone ou baixe o projeto**

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure a API Key** (opcional):
   - Renomeie `config.env` para `.env`
   - Substitua `your_api_key_here` pela sua chave real da OpenAI
   - Se não configurar, o sistema funcionará em modo de demonstração

## 🚀 Como Executar

1. **Inicie o servidor**:
   ```bash
   python app.py
   ```

2. **Acesse a aplicação**:
   - Abra seu navegador
   - Vá para: `http://localhost:5000`

## 🏗️ Arquitetura do Projeto

### Estrutura de Arquivos
```
project_online/
├── app.py              # Servidor Flask principal
├── requirements.txt    # Dependências Python
├── config.env         # Configuração de ambiente
├── README.md          # Este arquivo
└── templates/
    └── index.html     # Interface web
```

### Agentes CrewAI

1. **Pesquisador**: Analisa a mensagem do usuário e identifica o contexto
2. **Escritor**: Cria respostas claras e úteis baseadas na análise

### Fluxo de Processamento

1. Usuário envia mensagem via interface web
2. Flask recebe a requisição POST
3. CrewAI processa com os agentes (Pesquisador → Escritor)
4. Resposta é retornada para a interface
5. Interface exibe a resposta ao usuário

## 🎨 Interface

A interface web inclui:
- Design moderno com gradientes
- Chat responsivo
- Indicador de loading
- Animações suaves
- Suporte a mobile

## 🔧 Configuração Avançada

### Variáveis de Ambiente
- `OPENAI_API_KEY`: Sua chave da API OpenAI

### Personalização
Você pode modificar:
- Modelo LLM no arquivo `app.py`
- Agentes e suas tarefas
- Design da interface em `templates/index.html`

## 🐛 Solução de Problemas

### Erro de API Key
Se você não configurar a API key, o sistema funcionará em modo de demonstração com respostas pré-definidas.

### Erro de Conexão
Verifique se:
- O servidor está rodando
- A porta 5000 está disponível
- Não há firewall bloqueando

### Erro de Dependências
Execute:
```bash
pip install --upgrade -r requirements.txt
```

## 📝 Exemplo de Uso

1. Acesse `http://localhost:5000`
2. Digite uma pergunta como: "Como funciona o CrewAI?"
3. O sistema processará com os agentes
4. Receba uma resposta inteligente

## 🤝 Contribuição

Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Contribuir com código

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

**Desenvolvido com ❤️ usando CrewAI e Flask** 