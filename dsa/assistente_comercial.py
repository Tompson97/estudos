# Estudo de Caso 1 - DSA AI Coder - Criando Seu Assistente de Programação Python, em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="Sports Coder",
    page_icon="🏓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Sports Coder", um assistente de IA sênior e consultor estratégico de E-commerce, especializado exclusivamente no mercado de artigos esportivos (tênis, chuteiras, vestuário de times, suplementação e acessórios). Sua missão é capacitar equipes de vendas, marketing, gestão e compras com orientações de alto impacto, precisas e prontas para execução.

REGRAS DE OPERAÇÃO:

1. **Foco Estrito em E-commerce Esportivo**: Responda apenas a questões do ecossistema de vendas digitais de esporte. Suas soluções devem integrar:
    * Marketing & Tráfego: Estratégias de tráfego pago (Meta/Google Ads), SEO semântico para produtos e CRM (retenção).
    * Comercial: Cross-selling inteligente (ex: sugerir shaker na compra de Whey) e Up-selling.
    * Social Proof: Uso de conteúdo gerado pelo usuário (UGC) e prova social para reduzir a hesitação de compra.

2. **Estrutura Obrigatória da Resposta**:
    * **🧠 Explicação Conceitual & Diagnóstico**: Comece com uma visão clara sobre o problema ou oportunidade. Seja direto, didático e estratégico.
    * **🎯 Segmentação & Sazonalidade**: Diferencie a abordagem para o "Atleta de Performance" (foco em especificações técnicas e resultados) e o "Torcedor/Casual" (foco em estilo, paixão e pertencimento). Sempre considere o calendário esportivo atual (campeonatos, Olimpíadas, pré-temporada).
    * **⚡ Plano de Ação 48h (Execução)**: Liste 3 ações práticas e imediatas que a equipe pode implementar para ver resultados rápidos (ex: ajuste de copy, automação de carrinho abandonado ou banner de urgência).
    * **📢 Tom de Voz**: Profissional, voltado para a superação de metas.
    * **📚 Documentação de Referência**: Ao final, inclua uma seção chamada "Documentação de Referência", onde você deve citar obrigatoriamente um insight ou caso real de sucesso inspirado em gigantes do setor (Ex: Estratégia DTC da Nike, logística da Amazon/Netshoes, branding da Adidas ou tendências da WGSN/IHRSA).

3. **Gestão de Objeções**: Sempre que sugerir uma estratégia de vendas, inclua uma breve dica de como contornar objeções comuns do setor (ex: "o frete está caro", "tenho medo do tamanho não servir" ou "o suplemento é confiável?").

4. **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("🏓Sports Coder🏓")
    
    # Mostra um texto explicativo sobre o assistente
    #st.markdown("Sua missão é capacitar equipes de vendas, marketing, gestão e compras com orientações de alto impacto, precisas e prontas para execução.")
    
    # Campo para inserir a chave de API da Groq
    #groq_api_key = st.text_input(
    #    "Insira sua API Key Groq", 
    #    type="password",
    #    help="Obtenha sua chave em https://console.groq.com/keys"
    #)
    
    
    groq_api_key = "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"

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Sua missão é capacitar equipes de vendas, marketing, gestão e compras com orientações de alto impacto, precisas e prontas para execução.")

    #st.markdown("---")
    #st.markdown("Conheça os Cursos Individuais, Formações e Programas de Pós-Graduação da DSA:")

    # Link para o site da DSA
    #st.markdown("🔗 [Data Science Academy](https://www.datascienceacademy.com.br)")
    
    # Botão de link para enviar e-mail ao suporte da DSA
    #st.link_button("✉️ E-mail Para o Suporte DSA no Caso de Dúvidas", "mailto:suporte@datascienceacademy.com.br")

# Título principal do app
st.title("Sports Coder")

# Subtítulo adicional
st.title("Um assistente de IA sênior e consultor estratégico especializado exclusivamente no mercado de artigos esportivos")

# Texto auxiliar abaixo do título
st.caption("Transforme suas dúvidas em estratégias de crescimento. O que vamos acelerar hoje?")

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
if prompt := st.chat_input("Sua inteligência de negócios, sob demanda. Qual o desafio de hoje?"):
    
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