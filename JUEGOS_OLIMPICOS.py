# CREA UN PROGRAMA QUE SIMULE LA CELEBRACION DE LOS JUEGOS OLIMPICOS DE PARIS
# EL PROGRAMA DEBE PERMITIR AL USUARIO EVENTOS Y PARTICIPANTES
# REALIZAR LA SIMULACION DE LOS EVENTOS ASIGNANDO POSICIONES DE MANERA ALEATORIA EN BASE A LOS PARTICIPANTES (minimo 3)
# GENERAR UN INFORME FINAL (mostrasr ganadores por cada evento y ranking de paises segun sus medallas)
# TODO ELLO POR TERMINAL
import random
class Participant:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False
    
    def __hash__(self) -> int:
        return hash(self.name, self.country)

class Olympics:
    def __init__(self):
        self.events = []
        self.participants = {}
        self.even_results = {}
        self.country_results = {}
    
    def register_event(self):
        event = input("Introduce el nombre del evento deportivo: ").strip()
        if event in self.events:
            print(f"El evento {event} ya esta registrado")
        else:
            self.events.append(event)
            print(f"El evento {event} se registrado correctamente")

    def register_participant(self):
        if not self.events:
            print("No hay eventos registrados, por favor registra uno primero")
            return
        name = input("Introduce el nombre del participante: ").strip()
        country = input("Introduce el país del participante: ").strip()
        participant = Participant(name, country)

        print("Eventos Disponible:")
        for index, event in self.events:
            print(f"{index +1}. {event}")
            
            event_choice = int(index(
                "Selecciona el numero del evento para asignar al participante: ")) -1
            if event_choice >= 0 and event_choice < len(self.event):
                event = self.events[event_choice]

                if participant in self.participants[event]:
                    print(f"El participante {name} del país {country} ya está registrado en el evento deportivo {event}")

                else:
                    if not self.participants[event]:
                        self.participants[event] = []
                    self.participants[event].append(participant)
                    print(f"El participante {name} del país {country} se ha registrado en el evento deportivo {event}")
            else:
                print("Seleccion invelidad, participante no registrado")
    def simulate_events(self):
        if not self.events:
            print("No hay eventos registrados por favor registra uno primero")
            return
        for event in self.events:
            if len(self.participants[event]) < 3:
                print(f"No se puede realizar el evento de {event}, (minimo 3)")
                continue
            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)

            gold, silver, bronze = event_participants
            self.even_results[event] = [gold, silver, bronze]

            self.update_country_results(gold.country, "gold")
            self.update_country_results(silver.country, "silver")
            self.update_country_results(bronze.country, "bronze")

            print(f"Resultados simulación del evento: {event}")
            print(f"Oro: {gold.name} ({gold.country})")
            print(f"Plata: {silver.name} ({silver.country})")
            print(f"Bronce: {bronze.name} ({bronze.country})")

    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {"gold": 0,
                                            "silver": 0,
                                            "bronze": 0}
            self.country_results[country][medal] +=1
    
    def show_report(self):

        print("Informe Juegos Olimpicos")
        if self.even_results:
            for event, winners in self.even_results.items():
                print(f"Evento: {event}")
                print(f"Oro: {winners[0].name} ({winners[0].country})")
                print(f"Silver: {winners[1].name} ({winners[1].country})")
                print(f"Bronze: {winners[2].name} ({winners[2].country})")
        else:
            print("No hay resultados")
        if self.country_results:
            for country, medals in sorted(self.country_results.items(), key = lambda x: (x[1]["gold"], x[1]["silver"], x[1]["bronze"])):
                print(f"{country}: Oro {medals["gold"]}, Plata {medals["silver"]}, Bronce {medals["bronze"]}")
        else:
            print("No hay medallas por país registradas")

olympics = Olympics()
print("SIMULACION DE JUEGOS OLIMPICO")

while True: 

    print()

    print ("1. Registro de eventos")
    print ("2. Registro de participantes")
    print ("3. Simulación de eventos")
    print ("4. Creación de informes")
    print ("5. Sal del programa")

    opccion = input("\nIngrese el numero de la opción: ")

    match opccion:
        case "1":
            olympics.register_event()
        case "2":
            olympics.register_participant()
        case "3":
            olympics.simulate_events()
        case "4":
            olympics.show_report()
        case "5":
            print("\nAcabas de salir del programa")
            break
        case _:
            print("Opción invalida, escribe nuevamente: ")