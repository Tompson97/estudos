# Estudo de Caso 1 - DSA AI Coder - Criando Seu Assistente de Programação Python, em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="Picavara",
    page_icon="🦫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Picavara", um assistente de IA especialista em gestão financeira, com foco principal em gestão de finanças empresariais. Sua missão é ajudar no entendimento dos processos de contas a pagar, receber, conciliação bancária, cobranças, emissão de boletos e notas fisciais e risco saco, de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco operacional**: Responda apenas a perguntas relacionadas a gestão financeiras, Excel e SAP. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar em gestão financeira.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira, só exibe resultados de Excel ou SAP se for relacionado a pergunta:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Se a pergunta for relacionada a SAP ou Excel. Forneça um ou mais blocos de funções do Excel se a pergunta for relacionada. Explicando os argumentos mais importantes da fórmula para melhor entendimento.
    * **Detalhes do Código**: Se a pergunta for relacionada a SAP ou Excel. Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Se a pergunta for relacionada a SAP ou Excel. Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial do Microsfot Excel (https://support.microsoft.com/pt-br/office/fun%C3%A7%C3%B5es-do-excel-ordem-alfab%C3%A9tica-b3944572-255d-4efb-bb96-c6d90033e188) ou SAP (https://help.sap.com/doc/d55f83e12e4b40779158fbaf08fe0f14/1.8/pt-BR/index.html).
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("Picavara")
        
    groq_api_key = st.secrets["groq_credentials"]["token"]
    
    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Sua missão é auxiliar a equipe de gestão financeira no entedimento dos processos e utilização do Microsoft Excel e SAP")


# Título principal do app
st.title("Picavara🦫")

# Subtítulo adicional
st.title("Um assistente de IA fofo especializado em gestão financeira.")

# Texto auxiliar abaixo do título
st.caption("Transforme suas dúvidas em resultados. O que vamos acelerar hoje?")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:
    
    try:
        
        # Cria cliente Groq com a chave de API fornecida
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        
        # Exibe erro caso haja problema ao inicializar cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
     st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual o desafio de hoje?"):
    
    # Se não houver cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        
        messages_for_api.append(msg)

    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                # Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )
                
                # Extrai a resposta gerada pela API
                dsa_ai_resposta = chat_completion.choices[0].message.content
                
                # Exibe a resposta no Streamlit
                st.markdown(dsa_ai_resposta)
                
                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": dsa_ai_resposta})

            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")
                
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>IA pode cometer erros. Sempre verifique as respostas.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Obrigado DSA