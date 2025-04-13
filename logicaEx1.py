import os
from random import choice
from time import sleep
from rich.console import Console
from rich.progress import track
from rich.table import Table

"""
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
"""




eventos = []
participantes = []

validation = True
while validation:
    print("""
    * 1. Registro de eventos.
    * 2. Registro de participantes.
    * 3. Simulación de eventos.
    * 4. Creación de informes.
    * 5. Salir del programa.
    """)
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        event = input("Deporte a registrar: ")
        if event.upper() in eventos:
            print("Evento ya registrado")
            sleep(2)
        else: 
            eventos.append(event.upper())
        os.system("cls" if os.name=="nt" else "clear")

        
    elif opcion == 2:
        event = input("Evento al que desea registrarlo: ").upper()
        if event.upper() in eventos:
            nombre = input("Nombre de participante: ").upper()
            pais = input("Pais de origen: ").upper()
            participantes.append({"nombre":nombre,"pais": pais,"evento": event, "puntos": 0})
            print("Participante registrado correctamente!")
            sleep(2)
            os.system("cls" if os.name=="nt" else "clear")

        else:
            print("Ese evento no existe")
            sleep(2)
            os.system("cls" if os.name=="nt" else "clear")

    elif opcion == 3:
        event = input("Seleccione el evento: ").upper()
        participantesEvento = [n for n in participantes if n["evento"]==event]
        if participantesEvento:
            console = Console()
            table = Table(title="¡OLIMPIADAS 2025!")
            table.add_column("ENFRENTAMIENTOS",justify="center" ,style="magenta")
            table.add_column("GANADOR", justify="center", style="green")
            for i in range(len(participantesEvento)):
                for j in range(i+1,len(participantesEvento)):
                    p1 = participantesEvento[i]
                    p2 = participantesEvento[j]
                    ganador = choice([p1,p2])
                    ganador["puntos"] += 3
                    table.add_row(f"{p1["nombre"]} VS {p2["nombre"]}",f"{ganador["nombre"]}")
            for i in track(range(20), description="Processing..."):
                sleep(0.2)
            console.print(table)
        else:
            print("Ese evento no existe o aun no tiene participantes")
            sleep(2)
            os.system("cls" if os.name=="nt" else "clear")

    elif opcion == 4:
        print("¿Sobre cual deporte le gustaria ver el informe?")
        event = input(">> ").upper()
        participantesEvento = [n for n in participantes if n["evento"]==event]
        if participantesEvento:
            console = Console()
            table = Table(title="Tabla de Medallas")
            table.add_column("Nombre", style="cyan")
            table.add_column("País", style="green")
            table.add_column("Medalla", style="magenta")

            ganadores = sorted(participantesEvento, key=lambda x:-x["puntos"])
            table.add_row(ganadores[0]["nombre"],ganadores[0]["pais"], "🥇 Oro")
            table.add_row(ganadores[1]["nombre"],ganadores[1]["pais"], "🥈 Plata")
            table.add_row(ganadores[2]["nombre"],ganadores[2]["pais"], "🥉 Bronce")

            console.print(table)
        else:
            print("Ese deporte aun no fue registrado o aun no terminaron de competir")
            sleep(2)
            os.system("cls" if os.name=="nt" else "clear")

    elif opcion == 5:
        os.system("cls" if os.name=="nt" else "clear")
        print("¡Muchas gracias por participar!")
        validation = False
    else:
        print("Opcion no valida")
        sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        