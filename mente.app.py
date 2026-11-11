<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌿 Mente Saudável — Saúde Mental de Jovens</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #e0f4ff 0%, #f0efff 50%, #e8f8f5 100%);
            min-height: 100vh;
        }

        header {
            background: linear-gradient(135deg, #5b7cfa 0%, #8b5cf6 100%);
            color: white;
            text-align: center;
            padding: 3rem 2rem;
            box-shadow: 0 4px 20px rgba(91, 124, 250, 0.3);
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.95;
        }

        nav {
            background: white;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            padding: 0.5rem;
        }

        nav a {
            display: block;
            padding: 0.9rem 1.5rem;
            color: #5b7cfa;
            text-decoration: none;
            font-weight: 600;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        nav a:hover {
            background: #5b7cfa;
            color: white;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 2rem;
        }

        section {
            margin-bottom: 3.5rem;
        }

        h2 {
            color: #5b7cfa;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #a78bfa;
            display: inline-block;
        }

        .card {
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 5px 20px rgba(91, 124, 250, 0.12);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .image-box {
            background: linear-gradient(135deg, #dbeafe 0%, #ede9fe 100%);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            margin: 1rem 0;
            font-size: 4rem;
        }

        .quote {
            background: #fef3c7;
            border-left: 5px solid #f59e0b;
            padding: 1.5rem;
            border-radius: 8px;
            font-style: italic;
            font-size: 1.1rem;
        }

        .help-box {
            background: linear-gradient(135deg, #d1fae5 0%, #d4e7ff 100%);
            border-radius: 16px;
            padding: 2rem;
            border: 2px solid #6ee7b7;
        }

        .help-box h3 {
            color: #065f46;
            margin-bottom: 1rem;
        }

        .team-box {
            background: #fef7ff;
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
        }

        footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        @media (max-width: 768px) {
            header h1 { font-size: 1.8rem; }
            .container { padding: 1rem; }
        }
    </style>
</head>
<body>

<!-- Cabeçalho -->
<header>
    <h1>🌿 Mente Saudável</h1>
    <p>Compreendendo e Cuidando da Saúde Mental dos Jovens</p>
</header>

<!-- Navegação -->
<nav>
    <ul>
        <li><a href="#inicio">🏠 Início</a></li>
        <li><a href="#o-que-e">💡 O Que É</a></li>
        <li><a href="#desafios">⚡ Desafios</a></li>
        <li><a href="#cuidados">💜 Cuidados</a></li>
        <li><a href="#ajuda">🆘 Preciso de Ajuda</a></li>
        <li><a href="#equipe">👩‍🏫 Sobre Nós</a></li>
    </ul>
</nav>

<div class="container">

    <!-- Página Início -->
    <section id="inicio" class="card">
        <h2>Bem-vindo ao Nosso Projeto 💙</h2>
        <div class="image-box">🌸🧠✨</div>
        <p style="font-size: 1.1rem;">
            A saúde mental é tão importante quanto a saúde física. No entanto, muitas vezes ela é deixada de lado ou compreendida de forma errada, especialmente entre os jovens que estão passando por tantas mudanças ao mesmo tempo. Este site foi criado por um grupo de estudantes com um objetivo simples mas muito importante: <strong>informar, conscientizar e acolher</strong>. Aqui você vai encontrar informações verdadeiras, dicas práticas e saber onde buscar ajuda quando precisar. Você não está sozinho! 💚
        </p>
        <br>
        <div class="quote">
            "Cuidar da mente não é luxo, é necessidade. E buscar ajuda não é sinal de fraqueza, é sinal de coragem."
        </div>
    </section>

    <!-- O Que É Saúde Mental -->
    <section id="o-que-e">
        <h2>💡 O Que É Saúde Mental</h2>
        
        <div class="card">
            <h3>🧠 Conceito</h3>
            <p>Saúde mental não significa apenas "não ter uma doença mental". Segundo a Organização Mundial da Saúde (OMS), saúde mental é um estado de bem-estar no qual a pessoa consegue desenvolver suas habilidades, lidar com os desafios normais da vida, trabalhar de forma produtiva e contribuir com a sua comunidade. Ela inclui o nosso bem-estar emocional, psicológico e social. A forma como pensamos, sentimos e agimos depende dela. Também influencia como lidamos com o estresse, nos relacionamos com outras pessoas e fazemos escolhas.</p>
        </div>

        <div class="grid">
            <div class="card">
                <div class="image-box">😊🧘‍♀️🌻</div>
                <h3>Quando estamos bem:</h3>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li>Conseguimos reconhecer nossas emoções</li>
                    <li>Enfrentamos os problemas com mais calma</li>
                    <li>Temos energia para as coisas que gostamos</li>
                    <li>Conseguimos pedir ajuda quando necessário</li>
                    <li>Não temos medo de sonhar e tentar</li>
                </ul>
            </div>

            <div class="card">
                <div class="image-box">⚖️💗🌟</div>
                <h3>Fatores que influenciam:</h3>
                <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li>Quem somos — nossa biologia e genética</li>
                    <li>Nossa família e amigos</li>
                    <li>Onde vivemos e estudamos</li>
                    <li>Eventos difíceis que acontecem na vida</li>
                    <li>Como nos tratamos e nos valorizamos</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Desafios Enfrentados pelos Jovens -->
    <section id="desafios">
        <h2>⚡ Desafios Enfrentados pelos Jovens</h2>
        
        <div class="card">
            <p>Ser jovem hoje não é uma tarefa fácil. A pressão vem de todos os lados: escola, família, redes sociais, expectativas sobre o futuro e até a incerteza sobre o mundo em que vivemos. Esses fatores afetam diretamente como nos sentimos e como vemos a nós mesmos.</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>📱 Redes Sociais</h3>
                <p>As redes sociais aproximam pessoas, mas também podem gerar comparação excessiva, ansiedade e sensação de insuficiência quando começamos a comparar nossa realidade com a aparência dos outros. Lembre-se: ninguém mostra tudo — só os melhores momentos!</p>
            </div>

            <div class="card">
                <h3>📚 Pressão e Estresse</h3>
                <p>Notas, provas, vestibular, escolhas sobre o futuro... tudo isso cria uma carga pesada. É importante entender que seu valor como pessoa não está em uma nota ou em uma aprovação. Você vale muito mais do que resultados!</p>
            </div>

            <div class="card">
                <h3>😔 Solidão e Isolamento</h3>
                <p>Muitas vezes nos sentimos sozinhos mesmo rodeados de pessoas. Isso é mais comum do que você imagina. Falar sobre o que sentimos é o primeiro passo para se sentir menos só. Não guarde tudo só com você.</p>
            </div>

            <div class="card">
                <h3>🔄 Mudanças Constantes</h3>
                <p>A adolescência é uma fase de grandes transformações — no corpo, nos sentimentos, nas amizades. Tudo isso pode causar confusão e insegurança. Isso faz parte do processo de crescer e descobrir quem você é.</p>
            </div>
        </div>

        <div class="quote" style="margin-top: 1rem;">
            "Não tenha medo de não estar bem. Ter dias difíceis não significa que você está falhando — significa que você é humano."
        </div>
    </section>

    <!-- Como Cuidar -->
    <section id="cuidados">
        <h2>💜 Como Cuidar da Sua Saúde Mental</h2>
        
        <div class="card">
            <p style="font-size: 1.1rem;">Assim como cuidamos do nosso corpo escovando os dentes ou praticando esportes, a mente também precisa de atenção diária. Aqui vão algumas dicas simples que fazem muita diferença:</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>😴 Durma Bem</h3>
                <p>O sono é fundamental para descansar o corpo e a mente. Tente dormir entre 8 e 10 horas por noite. Estabeleça um horário e, se possível, afaste o celular pelo menos 30 minutos antes de dormir. A tela atrapalha o sono!</p>
            </div>

            <div class="card">
                <h3>🏃 Movimente-se</h3>
                <p>A prática de exercícios libera substâncias no cérebro que nos fazem sentir melhor, como a endorfina. Não precisa ser atleta: caminhar, dançar, andar de bicicleta ou brincar com o cachorro já faz uma enorme diferença.</p>
            </div>

            <div class="card">
                <h3>🗣️ Fale Sobre O Que Sente</h3>
                <p>Encontre alguém de confiança — um amigo, um familiar, um professor. Colocar para fora o que sentimos alivia o peso. Você não precisa resolver tudo sozinho. Compartilhar é fortalecer!</p>
            </div>

            <div class="card">
                <h3>🌿 Tenha Tempo Para Você</h3>
                <p>Reserve um tempo para fazer coisas que te fazem feliz: ler, desenhar, ouvir música, cuidar de plantas, descansar. Você não precisa ser produtivo o tempo todo. Descansar também é necessário!</p>
            </div>

            <div class="card">
                <h3>🍎 Cuide do Corpo</h3>
                <p>Comer bem, beber água e evitar excessos também refletem em como nos sentimos emocionalmente. O corpo e a mente trabalham juntos — cuidar de um é cuidar do outro.</p>
            </div>

            <div class="card">
                <h3>🤝 Aprenda a Dizer Não</h3>
                <p>Estabelecer limites não é ser egoísta. É saber respeitar seus próprios sentimentos e energias. Se algo te incomoda ou te cansa, você tem todo o direito de recuar e dizer não.</p>
            </div>
        </div>
    </section>

    <!-- Preciso de Ajuda -->
    <section id="ajuda">
        <h2>🆘 Preciso de Ajuda</h2>
        
        <div class="help-box">
            <h3>📞 Canais de Apoio Gratuito</h3>
            <p><strong>CVV — Centro de Valorização da Vida:</strong> Ligue <strong>188</strong> — funciona 24 horas por dia, todos os dias. É gratuito e confidencial. Você também pode acessar o site cvv.org.br e conversar por chat.</p>
            <p><strong>CAPS — Centro de Atenção Psicossocial:</strong> Procure a unidade mais próxima da sua casa. O atendimento é gratuito, pelo SUS.</p>
            <p><strong>Professor(a), Coordenador(a) ou Diretor(a):</strong> Na sua escola também existem pessoas prontas para te ouvir e ajudar. Não hesite em procurar!</p>
            <p><strong>Família e amigos:</strong> Conversar com alguém em quem confiamos já é um grande passo. Eles podem te acompanhar para buscar ajuda profissional.</p>
        </div>

        <div class="card" style="margin-top: 1.5rem;">
            <h3>⚠️ Sinais de que Você Precisa Procurar Ajuda</h3>
            <p>Não ignore esses sinais. Eles são o seu corpo e sua mente pedindo apoio:</p>
            <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                <li>Sentir tristeza ou desespero que não passa por vários dias</li>
                <li>Perder o interesse em coisas que você gostava</li>
                <li>Dormir demais ou não conseguir dormir</li>
                <li>Mudanças bruscas de apetite — comer muito ou quase nada</li>
                <li>Sentir que tudo é inútil ou que não há esperança</li>
                <li>Dificuldade para se concentrar ou tomar decisões</li>
                <li>Isolar-se de amigos e familiares</li>
            </ul>
            <br>
            <p><strong>Lembre-se:</strong> buscar ajuda é um ato de coragem. Você não está sozinho e sua vida é importante. 💛</p>
        </div>
    </section>

    <!-- Sobre Nós -->
    <section id="equipe">
        <h2>👩‍🏫 Sobre Nós</h2>
        <div class="team-box">
            <div class="image-box">👩‍🎓🤝👩‍🎓</div>
            <h3>Projeto Mente Saudável — Turma [Sua Turma]</h3>
            <p>Este site foi desenvolvido por um grupo de cinco estudantes que acreditam que falar sobre saúde mental deveria ser algo tão natural quanto falar sobre saúde física. Nosso objetivo é levar informação verdadeira, sem medos nem tabus, para que mais jovens se sintam compreendidos e saibam que não estão sós.</p>
            <br>
            <p><strong>Nossa mensagem final:</strong> Cuide de você. Respeite seus limites. Valorize sua jornada. E lembre-se: está tudo bem não estar bem às vezes — o importante é saber que pode pedir ajuda. 💚</p>
        </div>
    </section>

</div>

<!-- Rodapé -->
<footer>
    <p>🌿 <strong>Mente Saudável — Saúde Mental de Jovens</strong></p>
    <p>Projeto Escolar — Novembro de 2026</p>
    <p style="margin-top: 0.5rem; font-size: 0.9rem;">💛 Você importa. Sua história importa. Não desista de você.</p>
</footer>

</body>
</html>
