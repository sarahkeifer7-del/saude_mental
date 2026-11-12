import streamlit as st

# ---------------- CONFIGURAÇÕES DA PÁGINA ----------------
st.set_page_config(
    page_title="Mente Saudável — Saúde Mental dos Jovens",
    page_icon="🌿",
    layout="wide"
)



# ---------------- ESTILO E CORES — NEON ROXO E AZUL ----------------
st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at 15% 10%, rgba(120, 59, 255, 0.20), transparent 30%),
            radial-gradient(circle at 85% 80%, rgba(67, 217, 232, 0.12), transparent 30%),
            linear-gradient(135deg, #17152D 0%, #1B1935 50%, #101B35 100%);
        color: #F5F1FF;
    }

    [data-testid="stHeader"] {
        background: rgba(23, 21, 45, 0.95);
    }

    h1 {
        color: #C7A5FF;
        text-shadow: 0 0 12px rgba(181, 106, 255, 0.7);
    }

    h2 {
        color: #BFA0FF;
        text-shadow: 0 0 8px rgba(120, 59, 255, 0.4);
    }

    h3 {
        color: #71E8FF;
    }

    p, li, ul {
        color: #F0ECFF;
        font-size: 16px;
    }

    .card {
        background: linear-gradient(135deg, #30205C, #252B50);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid rgba(181, 106, 255, 0.55);
        box-shadow:
            0 0 12px rgba(120, 59, 255, 0.25),
            0 0 25px rgba(67, 217, 232, 0.10);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }

    .card:hover {
        border-color: #B56AFF;
        box-shadow:
            0 0 18px rgba(181, 106, 255, 0.65),
            0 0 35px rgba(67, 217, 232, 0.20);
        transform: translateY(-4px);
    }

    .quote {
        background: linear-gradient(135deg, #30204F, #252B50);
        border-left: 5px solid #43D9E8;
        padding: 15px;
        font-style: italic;
        border-radius: 8px;
        color: #F5F1FF;
        box-shadow: 0 0 12px rgba(67, 217, 232, 0.18);
    }

    .help-box {
        background: linear-gradient(135deg, #173C50, #25205A);
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #43D9E8;
        color: #E8FAFF;
        box-shadow: 0 0 18px rgba(67, 217, 232, 0.30);
    }

    .help-box p, .help-box strong {
        color: #E8FAFF;
    }

    /* MENU LATERAL */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #20163F, #152443);
        border-right: 1px solid rgba(181, 106, 255, 0.5);
    }

    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span {
        color: #F5F1FF !important;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        background: rgba(120, 59, 255, 0.10);
        border: 1px solid rgba(181, 106, 255, 0.20);
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 5px;
        transition: all 0.2s ease;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(120, 59, 255, 0.30);
        border-color: #B56AFF;
    }

</style>
""", unsafe_allow_html=True)



# ---------------- CABEÇALHO ----------------
st.markdown("""
<div style="
    background: linear-gradient(120deg, #5B2CFF 0%, #783BFF 55%, #176BFF 100%);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    color: white;
    border: 1px solid rgba(181, 106, 255, 0.8);
    box-shadow:
        0 0 18px rgba(120, 59, 255, 0.65),
        0 0 38px rgba(67, 217, 232, 0.22);
">
    <h1 style="
        color: white;
        text-shadow: 0 0 15px rgba(255,255,255,0.5);
    ">🌿 Mente Saudável</h1>

    <h3 style="color: #E0E7FF;">
        Compreendendo e Cuidando da Saúde Mental dos Jovens
    </h3>
</div>
<br>
""", unsafe_allow_html=True)



# ---------------- MENU LATERAL ----------------
menu = st.sidebar.radio(
    "📋 Navegação",
    ["🏠 Início", "💡 O Que É", "⚡ Desafios", "💜 Cuidados", "🆘 Preciso de Ajuda", "👩‍🏫 Sobre Nós"]
)

# ---------------- PÁGINA INÍCIO ----------------
if menu == "🏠 Início":
    st.header("Bem-vindo ao Nosso Projeto 💙")
    st.markdown("""
    <div class="card">
        <h3>🌸🧠✨</h3>
        <p>
        A saúde mental é tão importante quanto a saúde física. No entanto, muitas vezes ela é deixada de lado ou compreendida de forma errada, especialmente entre os jovens que estão passando por tantas mudanças ao mesmo tempo.
        </p>
        <p>
        Este site foi criado por um grupo de cinco estudantes com um objetivo simples mas muito importante: <strong style="color:#a78bfa;">informar, conscientizar e acolher</strong>. Aqui você vai encontrar informações verdadeiras, dicas práticas e saber onde buscar ajuda quando precisar. Você não está sozinho! 💚
        </p>
    </div>
    <div class="quote">
    "Cuidar da mente não é luxo, é necessidade. E buscar ajuda não é sinal de fraqueza, é sinal de coragem."
    </div>
    """, unsafe_allow_html=True)

# ---------------- PÁGINA: O QUE É SAÚDE MENTAL ----------------
elif menu == "💡 O Que É":
    st.header("💡 O Que É Saúde Mental")
    
    st.markdown("""
    <div class="card">
        <h3>🧠 Conceito</h3>
        <p>Saúde mental não significa apenas "não ter uma doença mental". Segundo a Organização Mundial da Saúde (OMS), saúde mental é um estado de bem-estar no qual a pessoa consegue desenvolver suas habilidades, lidar com os desafios normais da vida, trabalhar de forma produtiva e contribuir com a sua comunidade.</p>
        <p>Ela inclui o nosso bem-estar emocional, psicológico e social. A forma como pensamos, sentimos e agimos depende dela. Também influencia como lidamos com o estresse, nos relacionamos com outras pessoas e fazemos escolhas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h3>😊 Quando estamos bem:</h3>
            <ul>
                <li>Conseguimos reconhecer nossas emoções</li>
                <li>Enfrentamos os problemas com mais calma</li>
                <li>Temos energia para as coisas que gostamos</li>
                <li>Conseguimos pedir ajuda quando necessário</li>
                <li>Não temos medo de sonhar e tentar</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h3>⚖️ Fatores que influenciam:</h3>
            <ul>
                <li>Quem somos — nossa biologia e genética</li>
                <li>Nossa família e amigos</li>
                <li>Onde vivemos e estudamos</li>
                <li>Eventos difíceis que acontecem na vida</li>
                <li>Como nos tratamos e nos valorizamos</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------- PÁGINA: DESAFIOS ----------------
elif menu == "⚡ Desafios":
    st.header("⚡ Desafios Enfrentados pelos Jovens")
    
    st.markdown("""
    <div class="card">
    <p>Ser jovem hoje não é uma tarefa fácil. A pressão vem de todos os lados: escola, família, redes sociais, expectativas sobre o futuro e até a incerteza sobre o mundo em que vivemos. Esses fatores afetam diretamente como nos sentimos e como vemos a nós mesmos.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📱 Redes Sociais</h3>
            <p>As redes sociais aproximam pessoas, mas também podem gerar comparação excessiva, ansiedade e sensação de insuficiência. Lembre-se: ninguém mostra tudo — só os melhores momentos!</p>
        </div>
        <div class="card">
            <h3>📚 Pressão e Estresse</h3>
            <p>Notas, provas, vestibular... seu valor como pessoa não está em uma nota ou em uma aprovação. Você vale muito mais do que resultados!</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h3>😔 Solidão e Isolamento</h3>
            <p>Muitas vezes nos sentimos sozinhos mesmo rodeados de pessoas. Falar sobre o que sentimos é o primeiro passo para se sentir menos só.</p>
        </div>
        <div class="card">
            <h3>🔄 Mudanças Constantes</h3>
            <p>A adolescência é uma fase de grandes transformações. Tudo isso pode causar confusão e insegurança. Isso faz parte de crescer!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote">
    "Não tenha medo de não estar bem. Ter dias difíceis não significa que você está falhando — significa que você é humano."
    </div>
    """, unsafe_allow_html=True)

# ---------------- PÁGINA: CUIDADOS ----------------
elif menu == "💜 Cuidados":
    st.header("💜 Como Cuidar da Sua Saúde Mental")
    
    st.markdown("""
    <div class="card">
    <p>Assim como cuidamos do nosso corpo, a mente também precisa de atenção diária. Aqui vão algumas dicas simples que fazem muita diferença:</p>
    </div>
    """, unsafe_allow_html=True)
    
    cuidados = [
        ("😴 Durma Bem", "Tente dormir entre 8 e 10 horas por noite. Afaste o celular 30 minutos antes de dormir!"),
        ("🏃 Movimente-se", "Caminhar, dançar, andar de bicicleta — exercício libera endorfina, que nos faz sentir melhor!"),
        ("🗣️ Fale Sobre O Que Sente", "Encontre alguém de confiança. Compartilhar é fortalecer!"),
        ("🌿 Tenha Tempo Para Você", "Reserve tempo para coisas que te fazem feliz. Descansar também é necessário!"),
        ("🍎 Cuide do Corpo", "Comer bem, beber água — corpo e mente trabalham juntos."),
        ("🤝 Aprenda a Dizer Não", "Estabelecer limites não é ser egoísta. É respeitar seus sentimentos.")
    ]
    
    for i in range(0, len(cuidados), 2):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='card'><h3>{cuidados[i][0]}</h3><p>{cuidados[i][1]}</p></div>", unsafe_allow_html=True)
        if i + 1 < len(cuidados):
            with col2:
                st.markdown(f"<div class='card'><h3>{cuidados[i+1][0]}</h3><p>{cuidados[i+1][1]}</p></div>", unsafe_allow_html=True)

# ---------------- PÁGINA: AJUDA ----------------
elif menu == "🆘 Preciso de Ajuda":
    st.header("🆘 Preciso de Ajuda")
    
    st.markdown("""
    <div class="help-box">
        <h3 style="color:#6ee7b7;">📞 Canais de Apoio Gratuito</h3>
        <p><strong>CVV — Centro de Valorização da Vida:</strong> Ligue <strong style="color:#fbbf24;">188</strong> — funciona 24h, todos os dias. É gratuito e confidencial. Ou acesse: cvv.org.br</p>
        <p><strong>CAPS:</strong> Procure a unidade mais próxima da sua casa. Atendimento gratuito pelo SUS.</p>
        <p><strong>Escola:</strong> Professores, coordenadores e diretores podem te ajudar e orientar.</p>
        <p><strong>Família e amigos:</strong> Conversar com alguém de confiança já é um grande passo!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="margin-top: 20px;">
        <h3>⚠️ Sinais de que Você Precisa Procurar Ajuda</h3>
        <ul>
            <li>Sentir tristeza que não passa por vários dias</li>
            <li>Perder o interesse em coisas que você gostava</li>
            <li>Dormir demais ou não conseguir dormir</li>
            <li>Mudanças bruscas de apetite</li>
            <li>Sentir que tudo é inútil ou sem esperança</li>
            <li>Dificuldade para se concentrar ou tomar decisões</li>
            <li>Isolar-se de amigos e familiares</li>
        </ul>
        <br>
        <p><strong style="color:#fbbf24;">Lembre-se:</strong> buscar ajuda é um ato de coragem. Você não está sozinho e sua vida é importante. 💛</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PÁGINA: SOBRE NÓS ----------------
elif menu == "👩‍🏫 Sobre Nós":
    st.header("👩‍🏫 Sobre Nós")
    
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h3>👩‍🎓🤝👩‍🎓 Projeto Mente Saudável</h3>
        <p>Este site foi desenvolvido por um grupo de cinco estudantes que acreditam que falar sobre saúde mental deveria ser algo tão natural quanto falar sobre saúde física.</p>
        <p>Nosso objetivo é levar informação verdadeira, sem medos nem tabus, para que mais jovens se sintam compreendidos e saibam que não estão sós.</p>
        <br>
        <p style="font-size: 18px;"><strong style="color:#a78bfa;">Nossa mensagem final:</strong></p>
        <p style="font-size: 18px;">Cuide de você. Respeite seus limites. Valorize sua jornada.</p>
        <p style="font-size: 18px;">Está tudo bem não estar bem às vezes — o importante é saber que pode pedir ajuda. 💚</p>
        <br>
        <p>Projeto Escolar — Novembro de 2026</p>
        <p style="color:#fbbf24;">💛 Você importa. Sua história importa. Não desista de você.</p>
    </div>
    """, unsafe_allow_html=True)
