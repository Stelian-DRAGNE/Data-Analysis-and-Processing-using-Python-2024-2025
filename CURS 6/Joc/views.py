from django.shortcuts import render


# Create your views here.

import random
import enum


class Optiuni(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizzard = 4
    Spock = 5

    def __str__(self):
        return self.name

    @property
    def emoji(self):
        return  {Optiuni.Rock: "🪨", Optiuni.Paper:"🧻", Optiuni.Scissors:"✂️", Optiuni.Lizzard:"🦎", Optiuni.Spock:"🖖"}[self]

    @classmethod
    def values(self):
        return [op.value for op in Optiuni]

    @classmethod
    def pairs(cls):
        return [(op, op.value) for op in Optiuni]

    @classmethod
    def wins_over(self, other):
        WINNERS = {
            Optiuni.Rock : (Optiuni.Scissors, Optiuni.Lizzard),
            Optiuni.Scissors : (Optiuni.Paper, Optiuni.Lizzard),
            Optiuni.Paper : (Optiuni.Rock, Optiuni.Spock),
            Optiuni.Spock : (Optiuni.Scissors, Optiuni.Rock),
            Optiuni.Lizzard : (Optiuni.Paper, Optiuni.Spock),
        }
        return other in WINNERS[other]

def logica_de_joc(client:int):
    client = Optiuni(client)
    server = Optiuni(random.choice(Optiuni.values()))

    if client == server:
        rezultat = 'Egalitate !'
    elif client.wins_over(server):
        rezultat = 'Ai castigat !'
    else:
        rezultat = 'Ai pierdut !'

    return client, server, rezultat


def rock_paper_view(request):
    context = {'pairs' : Optiuni.pairs()}
    if request.method == "POST":
        print('Metoda -- POST')
        print(request.POST)
        client = request.POST.get('chosen')

        # Logica de business ...
        if client and (client in map(str, Optiuni.values())):
            alegere_client, alegere_server, rezultat_joc = logica_de_joc(int(client))
            context.update({
                'client' : alegere_client,
                'server' : alegere_server,
                'rezultat' : rezultat_joc,
            })
    else:
        print('Metoda -- GET')
    return render(request, "rock_paper.html", context)


def rock_paper_scissors_lizzard_spock_view(request):
    context = {'pairs' : Optiuni.pairs()}
    if request.method == "POST":
        client = request.POST.get('chosen')
        if client and (client in map(str, Optiuni.values())):
            alegere_client, alegere_server, rezultat_joc = logica_de_joc(int(client))
            context.update({
                'client' : alegere_client,
                'server' : alegere_server,
                'rezultat' : rezultat_joc,
            })

    return render(request, 'rock_paper_scissors_lizzard_spock.html', context)