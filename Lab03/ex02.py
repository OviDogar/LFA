class ParkingAutomaton:
    def __init__(self, total_spots):
        if total_spots <= 0:
            raise ValueError("Numarul de locuri de parcare trebuie sa fie pozitiv")
        
        self.total_spots = total_spots
        self.parking_spots = [False] * total_spots
        
    def get_state(self):
        occupied = sum(self.parking_spots)
        free = self.total_spots - occupied
        
        state = {
            "total_spots": self.total_spots,
            "occupied_spots": occupied,
            "free_spots": free,
            "spots_status": ["Ocupat" if spot else "Liber" for spot in self.parking_spots]
        }
        return state
    
    def park(self, spot_number):
        if spot_number < 1 or spot_number > self.total_spots:
            return {"success": False, "message": f"Locul {spot_number} nu exista"}
        
        spot_index = spot_number - 1
        
        if self.parking_spots[spot_index]:
            return {"success": False, "message": f"Locul {spot_number} este deja ocupat"}
        
        self.parking_spots[spot_index] = True
        return {"success": True, "message": f"Masina a fost parcata cu succes pe locul {spot_number}"}
    
    def leave(self, spot_number):
        if spot_number < 1 or spot_number > self.total_spots:
            return {"success": False, "message": f"Locul {spot_number} nu exista"}
        
        spot_index = spot_number - 1
        
        if not self.parking_spots[spot_index]:
            return {"success": False, "message": f"Locul {spot_number} este deja liber"}
        
        self.parking_spots[spot_index] = False
        return {"success": True, "message": f"Masina a fost scoasă cu succes de pe locul {spot_number}"}
    
    def find_free_spot(self):
        for i, occupied in enumerate(self.parking_spots):
            if not occupied:
                return i + 1  # Returnam numarul locului (indexul + 1)
        return None  # Nu exista locuri libere


def main():

    # cerem de la consola numarul de locuri din parcare

    print("Introduceti numarul de locuri din parcare: ")
    total_spots = int(input())

    parking = ParkingAutomaton(total_spots)

    # creem un meniu in consola pentru a parca si a scoate masini

    while True:
        print("\n1. Parcare masina")
        print("2. Scoatere masina")
        print("3. Afisare starea parcarii")
        print("4. Iesire")

        option = input("Optiunea dvs.: ")

        if option == "1":
            spot_number = int(
                input("Introduceti numarul locului unde doriti sa parcati: "))
            result = parking.park(spot_number)
            print(result["message"])
        elif option == "2":
            spot_number = int(
                input("Introduceti numarul locului de unde doriti sa scoateti masina: "))
            result = parking.leave(spot_number)
            print(result["message"])
        elif option == "3":
            print(parking.get_state())
        elif option == "4":
            break
        else:
            print("Optiune invalida. Reintroduceti.")

if __name__ == "__main__":
    main()