def mh():
    habilidades=['Desenhar','Saber dar conselho','Escutar os outros', 'Reflexivo', 'Adaptável', 'Calmo', 'Organização', 'Observador', 'Coração Ensinável', 'Lógica']
    print('Essas são as minhas Habilidades:')
    print()
    for h in habilidades:
        print(f'- {h}')
    print()


def mo():
    objetivos=['Ser a cada dia melhor do que o meu Eu do dia anterior', 'Viver uma vida com Deus', 'Acordar sempre pensando em como eu posso ajudar alguém nesse dia', 'Ser mais humilde','Trabalhar com o que eu gosto', 'Ter uma Família', 'Honrar minha mãe por tudo o que ela já fez por mim', 'Ser Feliz :)']
    print('Esses são os meus Objetivos:')
    print()
    for h in objetivos:
        print(f'- {h}')
    print()
  

def mhist():
    historia=['Nasci e cresci no Rio de Janeiro, meus pais se separam quando eu era muito novo,',
              'então vivia de um lado para o outro vivendo um pouco com o meu pai e minha mãe, ',
              'até minha mãe ter a minha irmã com o meu padrasto, que o considero como meu ',
              'segundo pai. Sempre fui uma criança calada que não dava trabalho, sempre fui ',
              'muito amado, agradeço à Deus por isso. Já na adolescência fiz muitos concursos',
              'Militares, cheguei muito perto, mas não passei em nenhum. Logo depois nos mudamos',
              'para Manaus, não sabia o que esperar daquele lugar, e quando cheguei senti uma',
              'surpresa enorme, não era nada do que eu esperava, foi um lugar incrível de si',
              'morar, fiz amigos que levo pela minha vida todo. Depois de um ano em Manaus, nos',
              'mudamos novamente, mas agora para Parintins, ainda no Amazonas, e lá foi onde fiz',
              'meu terceiro ano do ensino médio e passei para a faculdade que eu queria, que era',
              'Engenharia de Software, até agora estou gostando muito. Mas quando finalizar esses',
              'dois anos aqui em Parintins ainda não sei para onde vamos, estou na expequitativa!']
    print('Essa é a minha História:')
    print()
    for h in historia:
        print(h)
    print()


def dqg():
    gosto=['Jogar games', 'Assistir Futebol','Animes','Cozinhar','Ler','Ter aquela reunião com a rapaziada','Desenhar','Tocar Violão','Correr','Observar a natureza','Musica', 'Ficar com a Família']
    print('Essas são algumas das coisas que eu gosto:')
    print()
    for h in gosto:
        print(f'- {h}')
    print()


print()
print('Portifólio de Daniel Sant Anna')
print()
print('Seja Bem-vindo ao meu portifólio em Python!')
print('Meu nome é Daniel Sant Anna e essa é a minha Jornada.')
print()
print('1 - Ver minhas Habilidades')
print('2 - Ver meus objetivos')
print('3 - Ver minha História')
print('4 - Ver do que eu gosto')
print('5 - Sair')
print()


while True:
    escolha=int(input('Escolha uma opção:'))
    print()
    if escolha==1:
        print(mh())
    elif escolha==2:
        print(mo())
    elif escolha==3:
        print(mhist())
    elif escolha==4:
        print(dqg())
    elif escolha==5:
        print('Deu para conhecer um pouco mais sobre mim ? Espero que sim...')
        print()
        break
