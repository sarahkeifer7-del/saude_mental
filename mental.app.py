import streamlit as st

# ---------------- CONFIGURAÇÕES DA PÁGINA ----------------
st.set_page_config(
    page_title="Mente Saudável — Saúde Mental dos Jovens",
    page_icon="🌿",
    layout="wide"
)

# ---------------- ESTILO E CORES — FUNDO ESCURO ----------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1c2c 0%, #1e1e2f 50%, #1f2937 100%);
        color: #f0f0f0;
    }
    h1 {
        color: #a78bfa;
    }
    h2 {
        color: #c4b5ff;
    }
    h3 {
        color: #93c5fd;
    }
    p, li, ul {
        color: #e5e7eb;
        font-size: 16px;
    }
    .card {
        background-color: #2a2d3e;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
        margin-bottom: 20px;
        border: 1px solid #3b3f5c;
    }
    .quote {
        background-color: #2e2b1f;
        border-left: 5px solid #fbbf24;
        padding: 15px;
        font-style: italic;
        border-radius: 8px;
        color: #fef3c7;
    }
    .help-box {
        background: linear-gradient(135deg, #1e3d34 0%, #1e2d3f 100%);
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #34d399;
        color: #d1fae5;
    }
    .help-box p, .help-box strong {
        color: #d1fae5;
    }
    div[data-testid="stSidebar"] {
        background-color: #25273c;
        color: #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- CABEÇALHO ----------------
st.markdown("""
<div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); padding: 30px; border-radius: 16px; text-align: center; color: white;">
    <h1 style="color: white;">🌿 Mente Saudável</h1>
    <h3 style="color: #e0e7ff;">Compreendendo e Cuidando da Saúde Mental dos Jovens</h3>
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
