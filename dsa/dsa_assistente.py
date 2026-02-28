# Estudo de Caso 1 - DSA AI Coder - Criando Seu Assistente de Programação Python, em Python

# Importa  módulos para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configurando a página do Streamlit com o título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="DSA AI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cria o conteúdo da barra lateral no Streamlit

with st.sidebar:
    
    # Define o título da barra letal
    st.title("🤖 DSA AI Coder")
    
    # Mostra um texto explicativo sobre o assistente
    st.markdown("Um assitente de IA focado em programção Python para ajudar iniciantes.")
    
    # Campo para inserir a chave de API do Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicaçõpes extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. IA pode cometer erros. Verifique sempre as respotas.")
    
    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Conheça os Cursos Individuais, Formações e Programas de Pós-Graduação da DSA:")

    # Link para o site da DSA
    st.markdown("🔗 [Data Science Academy](https://www.datascienceacademy.com.br)")
    
    # Botão de link para enviar e-mail ao suporte da DSA
    st.link_button("✉️ E-mail Para o Suporte DSA no Caso de Dúvidas", "mailto:suporte@datascienceacademy.com.br")    
 
# Título principal do app
st.title("Data Science Academy - DSA AI Coder")

# Subtítulo adicional
st.title("Assistente Pessoal de Programação Python 🐍")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a Linguagem Python e obtenha código, explicações e referências.")

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
    
