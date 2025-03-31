import re

class LimbajRegulat:
    def __init__(self, expresie=None, multime=None):
        if expresie is not None:
            self.expresie = expresie
            self.multime = self.regex_to_set(expresie)
        elif multime is not None:
            self.multime = set(multime)
            self.expresie = "{" + ",".join(multime) + "}"
        else:
            self.multime = set()
            self.expresie = "{}"

    def regex_to_set(self, expresie):
        if not isinstance(expresie, str):
            raise ValueError("Expresia trebuie sa fie un string")
        if not expresie.startswith("{") or not expresie.endswith("}"):
            raise ValueError(
                "Expresia trebuie sa inceapa cu '{' si sa se termine cu '}'")
        if not re.match(r'^\{(.+?)\}$', expresie):
            raise ValueError("Expresia trebuie sa fie de forma {a+b(c)...}")
        return set(re.findall(r'\w+', expresie))
           
    def __str__(self):
        return self.expresie
    
    def reuniune(self, alt_limbaj):
        rezultat = self.multime.union(alt_limbaj.multime)
        return LimbajRegulat(multime=rezultat)
    
    def intersectie(self, alt_limbaj):
        rezultat = self.multime.intersection(alt_limbaj.multime)
        return LimbajRegulat(multime=rezultat)
    
    def diferenta(self, alt_limbaj):
        rezultat = self.multime.difference(alt_limbaj.multime)
        return LimbajRegulat(multime=rezultat)
    
    def concatenare(self, alt_limbaj):
        rezultat = set()
        for cuvant1 in self.multime:
            for cuvant2 in alt_limbaj.multime:
                rezultat.add(cuvant1 + cuvant2)
        return LimbajRegulat(multime=rezultat)
    
    def putere(self, n):
        if n == 0:
            return LimbajRegulat(multime={"E"})  # epsilon (cuvant vid)
        elif n == 1:
            return LimbajRegulat(multime=self.multime)
        else:
            rezultat = self
            for _ in range(n-1):
                rezultat = rezultat.concatenare(self)
            return rezultat
    
    def reverse(self):
        rezultat = set(cuvant[::-1] for cuvant in self.multime)
        return LimbajRegulat(multime=rezultat)


def afiseaza_meniu():
    print("\n" + "=" * 50)
    print("OPERATII PE LIMBAJE REGULATE")
    print("=" * 50)
    print("1. Reuniune")
    print("2. Intersectie")
    print("3. Diferenta")
    print("4. Concatenare")
    print("5. Putere")
    print("6. Oglindire")
    print("7. Introducere limbaje noi")
    print("0. Iesire")
    print("=" * 50)


def citeste_limbaj(mesaj):
    while True:
        expresie = input(mesaj)
        try:
            limbaj = LimbajRegulat(expresie)
            print(f"Limbajul introdus: {limbaj}")
            return limbaj
        except ValueError as e:
            print(f"Eroare: {e}. Incercati din nou.")


def main():
    print("Bun venit la aplicatia pentru operatii pe limbaje regulate!")
    print("introduceti limbajele in formatul {regex}")
    print("de exemplu: {ab(a+b)} pentru limbajul care contine cuvintele 'aba' si 'abb'")
    
    l1 = LimbajRegulat("{ab+ba}")
    l2 = LimbajRegulat("{a+b}")
    
    print(f"Limbaj 1 implicit: {l1}")
    print(f"Limbaj 2 implicit: {l2}")
    
    while True:
        afiseaza_meniu()
        print(f"Limbaj 1: {l1}")
        print(f"Limbaj 2: {l2}")

        optiune = input("Alegeti o optiune (0-7): ")
        
        if optiune == "0":
            print("Multumesc, la revedere!")
            break
        
        elif optiune == "1":
            rezultat = l1.reuniune(l2)
            print(f"Rezultat: L1 U L2 = {rezultat}")
        
        elif optiune == "2":
            rezultat = l1.intersectie(l2)
            print(f"Rezultat: L1 intersectat cu L2 = {rezultat}")
        
        elif optiune == "3":
            rezultat = l1.diferenta(l2)
            print(f"Rezultat: L1 - L2 = {rezultat}")
        
        elif optiune == "4":
            rezultat = l1.concatenare(l2)
            print(f"Rezultat: L1 * L2 = {rezultat}")
        
        elif optiune == "5":
            try:
                n = int(input("Introduceti puterea n: "))
                if n < 0:
                    raise ValueError("Puterea trebuie sa fie un numar ne-negativ")
                rezultat = l1.putere(n)
                print(f"Rezultat: L1^{n} = {rezultat}")
            except ValueError as e:
                print(f"Eroare: {e}")
        
        elif optiune == "6":
            rezultat = l1.reverse()
            print(f"Rezultat: L1^R = {rezultat}")
        
        elif optiune == "7":
            l1 = citeste_limbaj("Introduceti primul limbaj (L1): ")
            l2 = citeste_limbaj("Introduceti al doilea limbaj (L2): ")
        
        else:
            print("Optiune invalida. Reincercati.")
        
        input("\nApasati ENTER pentru a continua...")


if __name__ == "__main__":
    main()