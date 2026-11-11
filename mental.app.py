<!DOCTYPE html>
<html lang="pt‑BR">
<head>
    <meta charset="UTF‑8">
    <meta name="viewport" content="width=device‑width, initial‑scale=1.0">
    <title>Saúde Mental dos Jovens</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box‑sizing: border‑box;
            font‑family: 'Arial', sans‑serif;
        }
        body {
            background‑color: #f8f5ff;
            color: #333;
            line‑height: 1.6;
        }
        header {
            background: linear‑gradient(135deg, #9d65c9, #5d54a4);
            color: white;
            text‑align: center;
            padding: 40px 20px;
        }
        header h1 {
            font‑size: 2.2rem;
            margin‑bottom:10px;
        }
        header p {
            font‑size:1.1rem;
            opacity:0.9;
        }
        .container {
            max‑width:1100px;
            margin: 40px auto;
            padding:0 20px;
        }
        .intro, .orientacoes {
            background:white;
            padding:30px;
            border‑radius:16px;
            box‑shadow:0 4px 12px #00000015;
            margin‑bottom:40px;
        }
        .orientacoes {
            background:#f0edff;
        }
        .grid {
            display: grid;
            grid‑template‑columns: repeat(auto‑fit, min‑max(300px, 1fr));
            gap:25px;
        }
        .card {
            background:white;
            border‑radius:16px;
            overflow:hidden;
            box‑shadow:0 4px 12px #00000012;
            transition: transform 0.3s;
        }
        .card:hover {
            transform: translateY(-6px);
        }
        .card img {
            width:100%;
            height:200px;
            object‑fit: cover;
        }
        .card‑content {
            padding:22px;
        }
        .card h3 {
            color:#5d54a4;
            margin‑bottom:10px;
        }
        footer {
            background:#5d54a4;
            color:white;
            text‑align:center;
            padding:20px;
            margin‑top:50px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Saúde Mental dos Jovens</h1>
        <p>Conheça os fatores que prejudicam a saúde mental e aprenda como cuidar de você e dos seus amigos</p>
    </header>

    <div class="container">
        <section class="intro">
            <h2>ℹ️ Introdução Completa</h2>
            <p>A adolescência é uma fase de grandes transformações: mudanças hormonais, busca pela identidade, novas responsabilidades na escola e maior convívio social. Por isso, os jovens ficam mais vulneráveis a sentimentos de ansiedade, tristeza e esgotamento. Muitas vezes esses sinais são confundidos com “mau humor”, mas são alertas do nosso corpo e da nossa mente. Reconhecer os fatores que prejudicam a saúde mental é o primeiro passo para pedir ajuda antes que a situação piore.</p>
        </section>

        <div class="grid">
            <!-- Card 1 Redes Sociais -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1611162616475‑46b635cb6868?auto=format&fit=crop&w=800&q=80" alt="Rede social no celular">
                <div class="card‑content">
                    <h3>📱 Uso excessivo das redes sociais</h3>
                    <p>Nas plataformas vemos apenas os momentos bons da vida das outras pessoas, o que gera comparação constante. A busca por curtidas, comentários positivos, o cyberbullying e ficar conectado até a madrugada alteram o sono, aumentam a ansiedade e diminuem a autoestima. Muitos jovens passam horas rolando a tela sem perceber quanto tempo passou e se sentem insuficientes em relação aos outros.</p>
                </div>
            </div>

            <!-- Card 2 Pressão Escolar -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1523050854058‑8df63ca3eeb7?auto=format&fit=crop&w=800&q=80" alt="Livros e cadernos escolares">
                <div class="card‑content">
                    <h3>📚 Pressão escolar e cobrança por resultados</h3>
                    <p>A cobrança por boas notas, vestibular, provas importantes e expectativas da família causa estresse contínuo. A sobrecarga de tarefas escolares faz com que muitos jovens abandonem o lazer e o descanso, sentindo medo de decepcionar os pais e professores. Essa pressão pode levar ao esgotamento mental, dificuldade de concentração e perda da motivação para estudar.</p>
                </div>
            </div>

            <!-- Card 3 Conflitos Familiares -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1511895460‑7ca7260573c2?auto=format&fit=crop&w=800&q=80" alt="Conversa familiar">
                <div class="card‑content">
                    <h3>🏠 Conflitos e falta de apoio familiar</h3>
                    <p>Brigas frequentes em casa, falta de diálogo, cobranças excessivas dos pais ou a sensação de não ser ouvido abalam muito o emocional. Quando o lar não é um local seguro para desabafar, o jovem guarda todos os sentimentos ruins dentro de si, aumentando a sensação de solidão e insegurança.</p>
                </div>
            </div>

            <!-- Card 4 Bullying -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1534238293‑122777499068?auto=format&fit=crop&w=800&q=80" alt="Jovens conversando">
                <div class="card‑content">
                    <h3>🤝 Bullying, cyberbullying e isolamento social</h3>
                    <p>Ser vítima de agressões verbais, físicas ou ataques online repetidos causa baixa autoestima, medo de ir à escola e vergonha de pedir ajuda. Mesmo sem sofrer bullying, muitos jovens sentem‑se excluídos dos grupos de amigos, sentindo que não pertencem a lugar nenhum, o que agrava a tristeza e a solidão.</p>
                </div>
            </div>

            <!-- Card 5 Rotina desequilibrada -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1506126613408‑eca40822d0a1?auto=format&fit=crop&w=800&q=80" alt="Pessoa dormindo">
                <div class="card‑content">
                    <h3>😴 Falta de sono, má alimentação e pouca atividade física</h3>
                    <p>Dormir menos de 7 horas por noite, comer alimentos processados e ficar sentado o dia todo alteram diretamente a química do cérebro. Essa rotina desequilibrada aumenta a irritabilidade, dificulta controlar as emoções e torna muito mais difícil lidar com os problemas do dia‑a‑dia.</p>
                </div>
            </div>

            <!-- Card 6 Incerteza do futuro -->
            <div class="card">
                <img src="https://images.unsplash.com/photo‑1507003211169‑0a1dd7228f2d?auto=format&fit=crop&w=800&q=80" alt="Jovem pensando">
                <div class="card‑content">
                    <h3>🔮 Incerteza sobre o futuro e preocupações financeiras</h3>
                    <p>Dúvidas sobre qual profissão escolher, medo de não conseguir emprego e preocupações com dinheiro geram angústia constante. Muitos jovens sentem‑se pressionados a decidir todo o futuro cedo, sem tempo para conhecer as próprias vontades, gerando ansiedade prolongada.</p>
                </div>
            </div>
        </div>

        <!-- SEÇÃO NOVA: INSTRUÇÕES COMPLETAS -->
        <section class="orientacoes" style="margin‑top:40px;">
            <h2>💛 Instruções Práticas para Cuidar da Saúde Mental</h2>
            <p><strong>1. Estabeleça horário para usar as redes sociais</strong><br>Defina um limite diário (ex: 1‑2 horas por dia) e evite abrir os aplicativos uma hora antes de dormir. Tire um tempo para atividades que gosta sem o celular.</p>
            <p><strong>2. Respeite os seus limites escolares</strong><br>Separe horários para estudar e horários para descansar. Não se cobre por notas perfeitas: erros fazem parte do aprendizado. Converse com pais ou professores se sentir sobrecarregado.</p>
            <p><strong>3. Busque alguém de confiança para desabafar</strong><br>Procure um familiar, professor ou amigo que você confie para falar como está se sentindo. Guardar sentimentos ruins dentro de si piora tudo.</p>
            <p><strong>4. Melhore a sua rotina diária</strong><br>Tente dormir entre 7‑9 horas por noite, caminhe ao menos 30 minutos por dia e priorize refeições equilibradas — pequenas mudanças já melhoram muito o humor.</p>
            <p><strong>5. Reconheça os sinais de alerta e peça ajuda</strong><br>Se sentir tristeza constante, perda de interesse nas coisas que gostava, choro frequente ou pensamentos ruins por mais de duas semanas: <strong>procure um psicólogo imediatamente</strong>.</p>
            <p><strong>📞 Apoio emocional gratuito: CVV 188</strong><br>O Centro de Valorização da Vida atende 24 horas por dia, todos os dias, sem cobrança. Ligue 188 quando precisar conversar com alguém.</p>
        </section>

        <section class="intro">
            <h2>🤝 Como ajudar um amigo que está sofrendo?</h2>
            <p>Se você perceber que um amigo está mudando de comportamento, se afastando ou falando que quer desistir: não ignore. Converse com ele sem julgar, diga que você está ali para apoiá‑lo e incentive‑o a procurar ajuda profissional. Não tente resolver tudo sozinho: avise um adulto de confiança se achar que ele está em risco.</p>
        </section>
    </div>

    <footer>
        <p>Site sobre Saúde Mental dos Jovens – Trabalho Escolar</p>
    </footer>
</body>
</html>
