import re
from pathlib import Path

class InvoiceValidator:
    def __init__(self):
        self.patterns = {
            'client': {
                'nume': r'^Nume Client: ([A-Z][a-z]+ [A-Z][a-z]+)$',
                'cnp': r'^CNP: (\d{13})$',
                'adresa': r'^Adresa: (.+)$',
                'tel': r'^Telefon: (\+?40|0)\d{9}$'
            },
            'produs': {
                'cod': r'^Cod Produs: ([A-Z0-9]{5,10})$',
                'nume': r'^Denumire: (.+)$',
                'cantitate': r'^Cantitate: (\d+(?:\.\d{1,2})?)$',
                'pret': r'^Pret: (\d+(?:\.\d{2})?)$',
                'tva': r'^TVA: (\d{1,2})%$'
            }
        }

    def validate_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip().split('\n')
        except FileNotFoundError:
            return ["Eroare: Fisierul nu a fost gasit."]
        except Exception as e:
            return [f"Eroare la citirea fisierului: {str(e)}"]

        errors = []
        line_number = 0

        if len(content) < 4:
            return ["Eroare: Fisierul nu contine suficiente informatii."]

        for field, pattern in self.patterns['client'].items():
            line_number += 1
            if line_number <= len(content):
                if not re.match(pattern, content[line_number - 1]):
                    errors.append(f"Linia {line_number}: Format invalid pentru {field}")

        line_number += 1

        while line_number < len(content):
            if not content[line_number].strip():
                line_number += 1
                continue

            product_lines = content[line_number:line_number + 5]
            if len(product_lines) < 5:
                errors.append(f"Produs incomplet la linia {line_number}")
                break

            for field, pattern in self.patterns['produs'].items():
                current_line = product_lines[list(self.patterns['produs'].keys()).index(field)]
                if not re.match(pattern, current_line):
                    errors.append(f"Linia {line_number + list(self.patterns['produs'].keys()).index(field)}: "
                                f"Format invalid pentru {field}")

            line_number += 5

        return errors if errors else ["Fisierul respecta formatul corect!"]

def main():
    validator = InvoiceValidator()
    
    print("Program de validare facturi")
    print("Format asteptat:")
    print("""
    Nume Client: Prenume Nume
    CNP: 1234567890123
    Adresa: Strada, Numar, Oras
    Telefon: 0722123456

    Cod Produs: ABC123
    Denumire: Nume Produs
    Cantitate: 10.5
    Pret: 99.99
    TVA: 19%
    """)

    while True:
        file_path = input("\nIntroduceti calea catre fisierul de validat (sau 'exit' pentru iesire): ")
        
        if file_path.lower() == 'exit':
            break

        results = validator.validate_file(file_path)
        print("\nRezultate validare:")
        for result in results:
            print(f"- {result}")

        print("\nDoriti sa validati alt fisier?")

if __name__ == "__main__":
    main()