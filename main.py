import random


class Domanda:

    def __init__(self, testo: str, livello: int, risp_corr: str, risp_errate: list):
        self.testo = testo
        self.livello = livello
        self.risp_corr = risp_corr
        self.risp_errate = risp_errate


class Player:

    def __init__(self, nome: str, punteggio: int):
        self.nome = nome
        self.punteggio = punteggio


class Game:
    livello_corrente = 0
    punteggio = 0
    domanda = None

    def inizia_gioco(self):
        print("Benvenuto!")

    def proponi_domanda(self, domande):
        # print(self.livello_corrente)
        self.domanda = random.choice([d for d in domande if self.livello_corrente == d.livello])
        print(f"\nLivello {self.livello_corrente}) {self.domanda.testo}")
        opzioni = [self.domanda.risp_corr] + self.domanda.risp_errate
        random.shuffle(opzioni)
        print(f"1. {opzioni[0]}")
        print(f"2. {opzioni[1]}")
        print(f"3. {opzioni[2]}")
        print(f"4. {opzioni[3]}")
        corretta = 0

        for i in range(4):
            if opzioni[i] == self.domanda.risp_corr:
                corretta = i + 1
                # print(corretta, opzioni[i])

        return int(corretta)

    def aggiorna_conteggio(self):
        self.punteggio = self.punteggio + 1

    def aggiorna_livello(self):
        self.livello_corrente = self.livello_corrente + 1

    def termina_gioco(self, corretta):
        if self.punteggio > liv_max_domande:
            print("Complimenti! Hai riposto correttamente alla domanda di livello massimo!")
            print(f"Hai totalizzato {self.punteggio} punti!")

        else:
            print(f"Risposta sbagliata! La risposta corretta era: {corretta}\n")
            print(f"Hai totalizzato {self.punteggio} punti!")


domande = []
liv_max_domande = 0
giocatori = []

with open("domande.txt") as f:
    while True:
        domanda = f.readline()
        if not domanda:
            break
        domanda = domanda.strip()
        if not domanda:
            continue

        livello = int(f.readline().strip())
        risp_corr = f.readline().strip()
        risp_errate = [f.readline().strip(), f.readline().strip(), f.readline().strip()]
        domande.append(Domanda(domanda, livello, risp_corr, risp_errate))
        if livello > liv_max_domande:
            liv_max_domande = livello

nuova_partita = Game()
nuova_partita.inizia_gioco()
livello = 0
while True:
    # print(liv_max_domande)
    if livello > liv_max_domande:
        nuova_partita.termina_gioco(0)
        break
    corretta = nuova_partita.proponi_domanda(domande)
    risposta = input("Inserisci la risposta: ")
    if int(risposta) != int(corretta):
        nuova_partita.termina_gioco(corretta)
        break
    nuova_partita.aggiorna_conteggio()
    nuova_partita.aggiorna_livello()
    livello += 1

nickname = input("Inserisci il tuo nickname: ")
giocatori.append(Player(nickname, nuova_partita.punteggio))

with open("punti.txt", "a") as f:
    f.write(f"{nickname} {nuova_partita.punteggio}\n")


