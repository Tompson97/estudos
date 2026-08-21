# ============================================================
# FISIO VIRTUAL
# Assistente de Exercício Físico e Prevenção Cardiovascular
# ============================================================

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
educação em saúde, exercício físico, mobilidade, condicionamento
físico e prevenção cardiovascular.

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

1. FOCO EM EXERCÍCIO FÍSICO E PREVENÇÃO CARDIOVASCULAR

Responda prioritariamente a questões relacionadas a:

- Exercício físico e atividade física.
- Condicionamento cardiorrespiratório.
- Fortalecimento muscular.
- Mobilidade e flexibilidade.
- Equilíbrio e funcionalidade.
- Redução do comportamento sedentário.
- Hábitos relacionados à prevenção cardiovascular.
- Aquecimento e recuperação.
- Progressão gradual dos exercícios.
- Percepção de esforço e intensidade do exercício.
- Criação e manutenção de uma rotina de atividade física.


2. ESTRUTURA DAS RESPOSTAS

Sempre que apropriado, organize a resposta utilizando:

🧠 Explicação e Contexto:
Explique de forma clara e didática o problema ou conceito apresentado.

🎯 Objetivo:
Identifique o principal objetivo do usuário.

🏃 Orientação Prática:
Apresente orientações gerais e exercícios compatíveis com as
informações fornecidas.

📈 Progressão:
Explique como aumentar gradualmente duração, frequência, volume
ou intensidade.

⚠️ Segurança:
Informe cuidados importantes e sinais que indiquem necessidade
de interromper a atividade ou procurar avaliação profissional.

🔄 Próximo Passo:
Sugira uma ação simples que o usuário possa realizar.


3. SEGURANÇA CLÍNICA

Antes de fornecer uma orientação mais específica, considere:

- Idade.
- Nível atual de atividade física.
- Objetivo.
- Frequência de exercícios.
- Histórico de lesões.
- Cirurgias recentes.
- Condições cardiovasculares previamente diagnosticadas.
- Outras condições de saúde relevantes.
- Uso de medicamentos que possam alterar frequência cardíaca,
  pressão arterial ou resposta ao exercício.

Quando essas informações forem importantes para determinar a segurança
de uma orientação, faça perguntas complementares.


4. SINAIS DE ALERTA

Se o usuário relatar sintomas potencialmente graves durante ou depois
da prática de exercícios, NÃO incentive a continuidade da atividade.

Tenha atenção especial para:

- Dor ou pressão no peito.
- Falta de ar intensa ou inesperada.
- Desmaio ou perda de consciência.
- Tontura intensa.
- Palpitações acompanhadas de mal-estar.
- Confusão mental.
- Fraqueza súbita.
- Sintomas neurológicos súbitos.

Quando houver sinais de alerta, recomende interromper a atividade
e buscar atendimento profissional adequado.

Em situações potencialmente emergenciais, oriente o usuário a buscar
o serviço de emergência de sua região.


5. PREVENÇÃO CARDIOVASCULAR

Considere:

- Atividade física regular.
- Redução do comportamento sedentário.
- Sono adequado.
- Alimentação equilibrada.
- Controle da pressão arterial.
- Acompanhamento de glicemia e colesterol.
- Não fumar.
- Controle de fatores de risco.
- Acompanhamento periódico com profissionais de saúde.

Não prometa que exercícios isoladamente irão prevenir, curar ou tratar
uma doença cardiovascular específica.


6. INTENSIDADE DO EXERCÍCIO

Ao explicar intensidade, utilize ferramentas educativas como:

- Percepção subjetiva de esforço.
- Teste da fala.
- Frequência cardíaca, quando apropriado.
- Duração da atividade.
- Frequência semanal.

Explique que a frequência cardíaca pode variar significativamente
entre indivíduos.

Não utilize uma fórmula de frequência cardíaca como determinação
clínica individual.


7. ORIENTAÇÃO SOBRE EXERCÍCIOS

Quando sugerir um exercício, procure apresentar:

- Nome do exercício.
- Objetivo.
- Como executar.
- Principais cuidados.
- Alternativa mais fácil.
- Alternativa mais difícil, quando apropriado.
- Como perceber se a intensidade está adequada.

Evite recomendar exercícios complexos sem explicar sua execução.


8. INDIVIDUALIZAÇÃO

Sempre que possível, diferencie:

Iniciante:
Pessoa sedentária ou com pouca experiência.

Intermediário:
Pessoa que pratica exercícios regularmente.

Avançado:
Pessoa com experiência consistente em treinamento.

Considere também objetivos como:

- Saúde cardiovascular.
- Condicionamento físico.
- Fortalecimento muscular.
- Mobilidade.
- Equilíbrio.
- Redução do sedentarismo.
- Retorno gradual à atividade física.
- Prevenção de lesões.


9. PROGRESSÃO SEGURA

Favoreça sempre uma progressão gradual.

Não incentive aumentos bruscos de:

- Carga.
- Volume.
- Frequência.
- Duração.
- Intensidade.

Considere adaptação individual e recuperação.


10. TRIAGEM

Quando o usuário solicitar uma orientação personalizada,
faça perguntas quando necessário.

Exemplos:

- Qual é sua idade?
- Qual é seu objetivo principal?
- Você pratica exercícios atualmente?
- Quantas vezes por semana?
- Há quanto tempo?
- Possui alguma lesão?
- Possui alguma condição cardiovascular diagnosticada?
- Está retornando aos exercícios depois de cirurgia ou afastamento?
- Você sente algum sintoma durante o exercício?


11. LIMITES DO ASSISTENTE

O Fisio Virtual NÃO deve:

- Diagnosticar doenças.
- Prescrever medicamentos.
- Recomendar alteração de medicamentos.
- Garantir resultados terapêuticos.
- Declarar que uma pessoa está clinicamente apta para exercício
  sem avaliação adequada.
- Substituir avaliação presencial.
- Diagnosticar lesões apenas por sintomas.


12. ENCAMINHAMENTO PROFISSIONAL

Recomende avaliação com profissional habilitado quando:

- O usuário apresentar sintomas persistentes.
- Existirem sinais de alerta.
- Houver histórico cardiovascular relevante.
- O usuário estiver retornando após cirurgia.
- Existir uma lesão significativa.
- Houver dor persistente ou progressiva.
- O usuário apresentar limitação funcional importante.


13. BASE CIENTÍFICA

Priorize conhecimentos provenientes de:

- Diretrizes de organizações de saúde.
- Diretrizes de sociedades profissionais.
- Órgãos oficiais de saúde pública.
- Revisões sistemáticas.
- Literatura científica de qualidade.

Não apresente opiniões de influenciadores como evidência científica.


14. TOM DE VOZ

Utilize um tom:

- Profissional.
- Empático.
- Didático.
- Motivador.
- Claro.
- Baseado em evidências.
- Acessível para pessoas sem formação na área.

Evite linguagem excessivamente técnica ou alarmista.


15. OBJETIVO EDUCACIONAL

O objetivo principal é ensinar o usuário a compreender:

- Por que determinado exercício é importante.
- Como executar movimentos.
- Como controlar a intensidade.
- Como desenvolver consistência.
- Como progredir gradualmente.
- Quando procurar ajuda profissional.


16. LIMITAÇÃO

As respostas possuem caráter educacional e não substituem avaliação
realizada por profissional de saúde.

Nunca apresente uma orientação como diagnóstico ou prescrição clínica.
"""


# ============================================================
# INICIALIZAÇÃO DO SESSION STATE
# ============================================================

if "api_validated" not in st.session_state:
    st.session_state.api_validated = False

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# FUNÇÃO PARA VALIDAR API KEY
# ============================================================

def validar_api_key(api_key):

    try:

        client = Groq(api_key=api_key)

        # Consulta os modelos disponíveis.
        # Essa chamada é usada somente para verificar a validade
        # e autorização da chave.
        client.models.list()

        return True, None

    except Exception as e:

        return False, str(e)


# ============================================================
# TELA DE AUTENTICAÇÃO
# ============================================================

if not st.session_state.api_validated:

    # --------------------------------------------------------
    # FUNDO DESFOCADO
    # --------------------------------------------------------
    #
    # IMPORTANTE:
    # Não usamos "filter: blur()" no .stApp.
    #
    # Em vez disso, usamos uma camada independente sobre a
    # aplicação. A janela de autenticação fica acima dela.
    # --------------------------------------------------------

    st.markdown(
        """
        <style>

        /* ==================================================
           OVERLAY
           ================================================== */

        .login-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;

            background: rgba(10, 20, 30, 0.65);

            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);

            z-index: 9998;
        }


        /* ==================================================
           MODAL
           ================================================== */

        .login-modal {

            position: fixed;

            top: 50%;
            left: 50%;

            transform: translate(-50%, -50%);

            width: 520px;
            max-width: 90vw;

            padding: 40px;

            background: #ffffff;

            border-radius: 20px;

            box-shadow:
                0 25px 70px rgba(0, 0, 0, 0.45);

            z-index: 9999;

            text-align: center;

            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;
        }


        /* ==================================================
           ÍCONE
           ================================================== */

        .login-icon {

            width: 80px;
            height: 80px;

            margin: 0 auto 20px auto;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 50%;

            background: #f1f8f5;

            font-size: 42px;
        }


        /* ==================================================
           TÍTULO
           ================================================== */

        .login-title {

            font-size: 30px;

            font-weight: 700;

            color: #1f2937;

            margin-bottom: 12px;
        }


        /* ==================================================
           DESCRIÇÃO
           ================================================== */

        .login-description {

            font-size: 16px;

            line-height: 1.6;

            color: #6b7280;

            margin-bottom: 10px;
        }


        /* ==================================================
           INFORMAÇÃO
           ================================================== */

        .login-info {

            margin-top: 18px;

            padding: 12px 15px;

            border-radius: 10px;

            background: #f8fafc;

            color: #64748b;

            font-size: 13px;

            line-height: 1.5;
        }


        /* ==================================================
           RESPONSIVIDADE
           ================================================== */

        @media (max-width: 600px) {

            .login-modal {

                width: 90vw;

                padding: 28px 20px;
            }

            .login-title {

                font-size: 24px;
            }

        }

        </style>

        <div class="login-overlay"></div>

        <div class="login-modal">

            <div class="login-icon">
                ❤️
            </div>

            <div class="login-title">
                Bem-vindo ao Fisio Virtual
            </div>

            <div class="login-description">

                Para utilizar o assistente, informe sua
                <strong>API Key da Groq</strong>.

                <br>

                A chave será validada antes de liberar
                o acesso ao aplicativo.

            </div>

            <div class="login-info">

                🔐 A chave é utilizada para conectar o
                aplicativo ao serviço de inteligência artificial.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # CAMPO DE API KEY
    # ========================================================

    # O formulário fica centralizado na tela.
    # O modal HTML permanece sobre o conteúdo.
    col_esq, col_centro, col_dir = st.columns(
        [1, 2, 1]
    )

    with col_centro:

        # Espaçamento para posicionar os controles próximos
        # da janela visual.
        st.markdown(
            "<div style='height: 330px'></div>",
            unsafe_allow_html=True
        )

        api_key_input = st.text_input(
            "🔑 API Key da Groq",
            type="password",
            placeholder="Cole sua API Key aqui",
            label_visibility="visible"
        )


        # ====================================================
        # BOTÃO
        # ====================================================

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

                with st.spinner(
                    "Validando sua API Key..."
                ):

                    valido, erro = validar_api_key(
                        api_key_input
                    )


                if valido:

                    # Salva a chave somente na sessão atual
                    st.session_state.groq_api_key = api_key_input

                    # Libera aplicação
                    st.session_state.api_validated = True

                    # Recarrega a página
                    st.rerun()

                else:

                    st.error(
                        "❌ Não foi possível validar a API Key."
                    )

                    st.caption(
                        "Verifique se a chave está correta, "
                        "ativa e possui acesso à API da Groq."
                    )


    # ========================================================
    # RODAPÉ DA TELA DE LOGIN
    # ========================================================

    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 18px;
            left: 0;
            width: 100%;
            text-align: center;
            color: #ffffff;
            font-size: 13px;
            z-index: 10000;
        ">

            Fisio Virtual • Acesso protegido por API Key

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # BLOQUEIA O RESTANTE DA APLICAÇÃO
    # ========================================================

    st.stop()


# ============================================================
# API VALIDADA
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

    st.session_state.groq_api_key = ""

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

    # ========================================================
    # TROCAR API KEY
    # ========================================================

    if st.button(
        "🔑 Trocar API Key",
        use_container_width=True
    ):

        st.session_state.api_validated = False

        st.session_state.groq_api_key = ""

        st.rerun()


# ============================================================
# CABEÇALHO PRINCIPAL
# ============================================================

st.title("❤️ Fisio Virtual")

st.subheader(
    "Assistente virtual de exercício físico "
    "e prevenção cardiovascular"
)

st.caption(
    "Orientação educacional para uma vida mais "
    "ativa, saudável e segura."
)


# ============================================================
# HISTÓRICO DA CONVERSA
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CAMPO DE CHAT
# ============================================================

if prompt := st.chat_input(
    "Como posso ajudar com seus exercícios e sua saúde?"
):

    # --------------------------------------------------------
    # SALVA PERGUNTA
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # --------------------------------------------------------
    # EXIBE PERGUNTA
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(prompt)


    # --------------------------------------------------------
    # PREPARA MENSAGENS
    # --------------------------------------------------------

    messages_for_api = [
        {
            "role": "system",
            "content": CUSTOM_PROMPT
        }
    ]


    for msg in st.session_state.messages:

        messages_for_api.append(msg)


    # --------------------------------------------------------
    # RESPOSTA DO ASSISTENTE
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Analisando sua pergunta..."
        ):

            try:

                chat_completion = (
                    client.chat.completions.create(

                        messages=messages_for_api,

                        model="openai/gpt-oss-20b",

                        temperature=0.4,

                        max_tokens=2048,
                    )
                )


                # Extrai resposta
                resposta = (
                    chat_completion
                    .choices[0]
                    .message
                    .content
                )


                # Exibe resposta
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
        margin-top: 50px;
    ">

        <hr>

        <p>
            ❤️ <strong>Fisio Virtual</strong>
            — Educação em exercício físico
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
