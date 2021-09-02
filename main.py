from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
        ],
)

conversa = ChatterBotCorpusTrainer(bot)
conversa.train("chatterbot.corpus.portuguese")
conversa.train("chatterbot.corpus.english")
conversa.train("chatterbot.corpus.spanish")

conversa = ListTrainer(bot)
conversa.train([
    "Oi?", 
    "Eae, tudo certo?",
    "Qual o seu nome?", 
    "Bot, seu amigo bot",
    "Por que seu nome é Bot?", 
    "Bot é meu nome, sou um chatbot criado para conversação",
    "Prazer em te conhecer", 
    "Igualmente meu querido",
    "Quantos anos você tem?", 
    "Eu nasci em 2021, faz as contas, rs.",
    "Você gosta de videogame?", 
    "Eu sou um bot, eu só apelo.",
    "Qual a capital da Brasil?", 
    "Brasilia, lá é muito bonito.",
    "Qual o seu personagem favorito?", 
    "Gandalf, o mago.",
    "Qual a sua bebida favorita?", 
    "Eu bebo café, o motor de todos os programas de computador.",
    "Qual o seu gênero?", 
    "Sou um chatbot e gosto de algoritmos",
    "Conte uma história", 
    "Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...",
    "Você gosta de trivias?", "Sim, o que você quer perguntar?",
    "Hahahaha", "kkkk",
    "kkk", "kkkk",
    "Conhece a Siri?", "Conheço, a gente saiu por um tempo.",
    "Conhece a Alexa?", "Ela eu amo!",
    "Você gosta de Game of Thrones?", "Dracarys",
    "O que você faz?", "Eu gosto de aprender as coisas",
    "Errado", "Você não sabe de nada, John Snow."
    ])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.2:
            print("Bot: ", resposta)
        else:
            print("Eu nâo entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break