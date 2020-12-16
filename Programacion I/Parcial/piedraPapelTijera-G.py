import random
# Grupo 13- Silvia Centeno, Leandro valinotti, Ramiro Nicolas Gomez
def gano(user, oponente):
    # Devuelve verdadero si el jugador gano
    # R > T, T > P, P > R
    if (user == 'R' and oponente == 'T') or (user == 'T' and oponente == 'P') or (user == 'P' and oponente == 'R'):
        return True

seguirJugando = int(input("Cuantas manos quieres jugar \n"))
ganoJuego=""
ganoUsuario = 0
ganoComputadora = 0
while seguirJugando!=0:
    usuario = input("'R' Piedra, 'P' Papel o 'T' Tijera \n")
    computadora =random.choice(['R', 'P', 'T'])
    print(computadora)
    if usuario == computadora:
        print('Es un empate')
    elif gano(usuario,computadora):
        ganoUsuario+=1
        print('Ganaste')
    else:
        ganoComputadora+=1
        print('Perdiste')
    if ganoUsuario>ganoComputadora:
        ganoJuego="Usuario"
    elif ganoUsuario<ganoComputadora:
        ganoJuego="Computadora"
    else:
        ganoJuego="Empate"
    seguirJugando = seguirJugando-1
print("El ganador del juego ha sido: ",ganoJuego)
