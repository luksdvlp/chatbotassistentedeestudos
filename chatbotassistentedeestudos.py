
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)
materiaEscolhida = False

trainer.train([
    'Oi',
    'Olá, sou o Assistente de Estudo e irei lhe auxiliar hoje! Por favor, escolher uma das disciplinas abaixo:\n [1]- Ciências\n [2]- História\n [3]- Matemática',
    '',
    'Olá, sou o Assistente de Estudo e irei lhe auxiliar hoje! Por favor, escolher uma das disciplinas abaixo:\n [1]- Ciências\n [2]- História\n [3]- Matemática'
])

matematica = [
    'O que é uma matriz?',
    'Em matemática, uma matriz é uma tabela retangular de números, símbolos ou expressões dispostas em linhas e colunas.',
    'Quanto é 2+2?',
    'É 4.',
    'Como cálcular a área de um quadrado?',
    'A área de um quadrado é igual a altura multiplicado pela lárgura'
]

ciencias = [
    'Qual o maior osso do corpo humano??',
    'O maior osso do corpo humano é o fêmur. Ele é o osso da coxa, estendendo-se do quadril até o joelho..',
    'Qual o maior orgão do corpo humano?',
    'O maior órgão do corpo humano é a pele. A pele cobre todo o corpo e atua como uma barreira protetora contra o ambiente externo.',
]

historia = [
    'Quem aboliu a escravidão?',
    'A escravidão foi oficialmente abolida no Brasil pela Lei Áurea, assinada pela Princesa Isabel em 13 de maio de 1888. Este foi o último país das Américas a abolir a escravidão.',
    'Quem foi o primeiro presidente do brasil pós ditadura?',
    'O primeiro presidente do Brasil após o fim da ditadura militar foi José Sarney.',
]

print('Olá, sou o Assistente de Estudo e irei lhe auxiliar hoje! Por favor, escolha uma das disciplinas abaixo:\n [1]- Ciências\n [2]- História\n [3]- Matemática')
while True:
    request = input('Você: ')
    if request.lower() == 'sair':
        print('Bot: Tchau')
        break
    elif not materiaEscolhida:
        if request.lower() == '1':
            trainer.train(ciencias)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        elif request.lower() == '2':
            trainer.train(historia)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        elif request.lower() == '3':
            trainer.train(matematica)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        else:
            print('Bot: Não entendi, poderia repetir?')
    else:
        response = bot.get_response(request)
        if float(response.confidence) < 0.1:
            print('Bot: Desculpe, não possuo resposta para esta pergunta.')
        else:
            print('Bot:', response)

