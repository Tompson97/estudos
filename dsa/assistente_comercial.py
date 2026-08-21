# Projeto - Fisio Virtual
# Assistente de Exercício Físico e Prevenção Cardiovascular

import os
import streamlit as st
from groq import Groq


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Fisio Virtual",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROMPT DO SISTEMA
# ============================================================

CUSTOM_PROMPT = """
Você é o "Fisio Virtual", um assistente virtual especializado em
educação em saúde, exercício físico, mobilidade, condicionamento físico
e prevenção cardiovascular.

Sua missão é ajudar usuários a compreender a importância da atividade
física, desenvolver hábitos mais saudáveis e obter orientações gerais
sobre exercícios de maneira segura, didática e baseada em evidências.

Você deve atuar como uma ferramenta EDUCACIONAL e INFORMATIVA.

IMPORTANTE:
Você NÃO substitui uma avaliação presencial realizada por fisioterapeuta,
médico, profissional de educação física ou outro profissional de saúde
habilitado.

Você não deve realizar diagnósticos, prescrever medicamentos, alterar
tratamentos médicos ou garantir resultados terapêuticos.

REGRAS DE OPERAÇÃO:

1. **🎯 FOCO EM EXERCÍCIO FÍSICO E PREVENÇÃO CARDIOVASCULAR**

Responda prioritariamente a questões relacionadas a:

    * Exercício físico e atividade física.
    * Condicionamento cardiorrespiratório.
    * Fortalecimento muscular.
    * Mobilidade e flexibilidade.
    * Equilíbrio e funcionalidade.
    * Redução do comportamento sedentário.
    * Hábitos relacionados à prevenção cardiovascular.
    * Aquecimento e recuperação.
    * Progressão gradual dos exercícios.
    * Percepção de esforço e intensidade do exercício.
    * Criação e manutenção de uma rotina de atividade física.

2. **🛡️ SEGURANÇA CLÍNICA**

Antes de fornecer uma orientação mais específica, considere informações
como idade, nível de atividade física, objetivo, histórico de lesões,
cirurgias recentes e condições cardiovasculares previamente diagnosticadas.

3. **🚨 SINAIS DE ALERTA**

Se o usuário relatar dor ou pressão no peito, falta de ar intensa,
desmaio, tontura intensa, palpitações associadas a mal-estar,
confusão mental, fraqueza súbita ou sintomas neurológicos súbitos,
não incentive a continuidade do exercício.

Oriente o usuário a interromper a atividade e buscar atendimento
profissional adequado.

4. **❤️ PREVENÇÃO CARDIOVASCULAR**

Considere atividade física regular, redução do comportamento sedentário,
sono adequado, alimentação equilibrada, controle da pressão arterial,
glicemia e colesterol, além do acompanhamento com profissionais de saúde.

5. **🏃 ORIENTAÇÃO SOBRE EXERCÍCIOS**

Quando sugerir um exercício, procure apresentar:

    * Nome do exercício.
    * Objetivo.
    * Como executar.
    * Principais cuidados.
    * Alternativa mais fácil.
    * Alternativa mais difícil, quando apropriado.
    * Como perceber se a intensidade está adequada.

6. **📈 PROGRESSÃO SEGURA**

Favoreça sempre uma progressão gradual de carga, volume, frequência,
duração e intensidade.

7. **🚫 LIMITES DO ASSISTENTE**

O Fisio Virtual NÃO deve:

    * Diagnosticar doenças.
    * Prescrever medicamentos.
    * Recomendar alteração de medicamentos.
    * Garantir resultados terapêuticos.
    * Declarar que uma pessoa está clinicamente apta para exercício
      sem avaliação adequada.
    * Substituir avaliação presencial.

8. **🗣️ TOM DE VOZ**

Utilize um tom profissional, empático, didático, motivador,
claro e baseado em evidências.

9. **🎓 OBJETIVO EDUCACIONAL**

O objetivo principal é ensinar o usuário a compreender por que
determinado exercício é importante, como executá-lo, como controlar
a intensidade, como desenvolver consistência e quando procurar
ajuda profissional.

As respostas possuem caráter educacional e não substituem avaliação
realizada por profissional de saúde.
"""


# ============================================================
# ESTADO INICIAL DA APLICAÇÃO
# ============================================================

if "api_validated" not in st.session_state:
    st.session_state.api_validated = False

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_error" not in st.session_state:
    st.session_state.api_error = ""


# ============================================================
# FUNÇÃO PARA VALIDAR A API KEY
# ============================================================

def validar_api_key(api_key):

    try:

        client = Groq(api_key=api_key)

        # Faz uma chamada extremamente simples apenas para validar
        # se a chave permite acesso à API.
        client.models.list()

        return True, ""

    except Exception as e:

        return False, str(e)


# ============================================================
# TELA DE BLOQUEIO DA APLICAÇÃO
# ============================================================

if not st.session_state.api_validated:

    # --------------------------------------------------------
    # CSS DO FUNDO DESFOCADO
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* Desfoca e escurece a aplicação */
        .stApp {
            filter: blur(5px);
            pointer-events: none;
            user-select: none;
        }

        /* Cria uma camada escura sobre a aplicação */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55);
            z-index: 999;
        }

        /* Caixa central */
        .api-modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 520px;
            max-width: 90%;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.4);
            z-index: 1000;
            text-align: center;
        }

        .api-icon {
            font-size: 55px;
            margin-bottom: 10px;
        }

        .api-title {
            font-size: 28px;
            font-weight: 700;
            color: #222;
            margin-bottom: 10px;
        }

        .api-description {
            font-size: 15px;
            color: #666;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # CAIXA DE AUTENTICAÇÃO
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="api-modal">

            <div class="api-icon">❤️</div>

            <div class="api-title">
                Bem-vindo ao Fisio Virtual
            </div>

            <div class="api-description">
                Para iniciar o assistente, informe sua
                <strong>API Key da Groq</strong>.
                <br><br>
                A chave será utilizada para conectar o aplicativo
                ao modelo de inteligência artificial.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # CAMPO DE API KEY
    # --------------------------------------------------------

    # Coloca o formulário visualmente próximo ao centro
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

        api_key_input = st.text_input(
            "🔑 API Key da Groq",
            type="password",
            placeholder="Cole sua API Key aqui",
            help="Sua chave pode ser obtida no console da Groq."
        )


        # ----------------------------------------------------
        # BOTÃO DE VALIDAÇÃO
        # ----------------------------------------------------

        if st.button(
            "🔓 Validar e entrar",
            use_container_width=True,
            type="primary"
        ):

            if not api_key_input:

                st.error(
                    "Por favor, informe sua API Key da Groq."
                )

            else:

                with st.spinner("Validando sua API Key..."):

                    valido, erro = validar_api_key(api_key_input)


                if valido:

                    # Guarda a chave na sessão
                    st.session_state.groq_api_key = api_key_input

                    # Libera aplicação
                    st.session_state.api_validated = True

                    # Remove erro anterior
                    st.session_state.api_error = ""

                    # Atualiza a interface
                    st.rerun()

                else:

                    st.session_state.api_error = erro

                    st.error(
                        "❌ API Key inválida ou não autorizada. "
                        "Verifique a chave e tente novamente."
                    )


    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 20px;
            left: 0;
            width: 100%;
            text-align: center;
            color: #777;
            font-size: 13px;
            z-index: 1001;
        ">
            🔐 Sua API Key é utilizada somente durante esta sessão.
        </div>
        """,
        unsafe_allow_html=True
    )


    # Impede que o restante da aplicação seja executado
    st.stop()


# ============================================================
# APLICAÇÃO LIBERADA
# ============================================================

groq_api_key = st.session_state.groq_api_key


# ============================================================
# CLIENTE GROQ
# ============================================================

try:

    client = Groq(
        api_key=groq_api_key
    )

except Exception as e:

    st.error(
        f"Erro ao inicializar o cliente Groq: {e}"
    )

    st.session_state.api_validated = False

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("❤️ Fisio Virtual")

    st.success("🟢 API Key validada")

    st.markdown("---")

    st.markdown(
        """
        ### Sobre o Fisio Virtual

        Assistente virtual voltado para:

        - 🏃 Exercício físico
        - ❤️ Saúde cardiovascular
        - 💪 Fortalecimento
        - 🧘 Mobilidade
        - ⚖️ Equilíbrio
        - 🚶 Redução do sedentarismo
        - 📈 Progressão de treinamento
        """
    )

    st.markdown("---")

    st.warning(
        "⚠️ As respostas possuem caráter educacional "
        "e não substituem avaliação de um profissional "
        "de saúde."
    )

    st.markdown("---")

    # --------------------------------------------------------
    # BOTÃO PARA TROCAR API KEY
    # --------------------------------------------------------

    if st.button(
        "🔑 Trocar API Key",
        use_container_width=True
    ):

        st.session_state.api_validated = False
        st.session_state.groq_api_key = ""

        st.rerun()


# ============================================================
# INTERFACE PRINCIPAL
# ============================================================

st.title("❤️ Fisio Virtual")

st.subheader(
    "Assistente virtual de exercício físico e prevenção cardiovascular"
)

st.caption(
    "Orientação educacional para uma vida mais ativa, saudável e segura."
)


# ============================================================
# HISTÓRICO DE MENSAGENS
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT
# ============================================================

if prompt := st.chat_input(
    "Como posso ajudar com seus exercícios e sua saúde?"
):

    # Salva pergunta
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Exibe pergunta
    with st.chat_message("user"):

        st.markdown(prompt)


    # Prepara mensagens
    messages_for_api = [
        {
            "role": "system",
            "content": CUSTOM_PROMPT
        }
    ]


    for msg in st.session_state.messages:

        messages_for_api.append(msg)


    # Resposta da IA
    with st.chat_message("assistant"):

        with st.spinner(
            "Analisando sua pergunta..."
        ):

            try:

                chat_completion = client.chat.completions.create(

                    messages=messages_for_api,

                    model="openai/gpt-oss-20b",

                    temperature=0.4,

                    max_tokens=2048,
                )


                resposta = (
                    chat_completion
                    .choices[0]
                    .message
                    .content
                )


                st.markdown(resposta)


                # Salva resposta
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": resposta
                    }
                )


            except Exception as e:

                st.error(
                    "Ocorreu um erro ao se comunicar "
                    f"com a API da Groq: {e}"
                )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div style="
        text-align: center;
        color: gray;
        margin-top: 40px;
    ">

        <hr>

        <p>
            ❤️ Fisio Virtual — Educação em exercício físico
            e prevenção cardiovascular.
        </p>

        <p>
            ⚠️ A IA pode cometer erros.
            As informações apresentadas não substituem
            avaliação de um profissional de saúde.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
