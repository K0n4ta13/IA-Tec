import json
import os
import sys

PROP_FILE_PATH = "proposiciones.json"
RULES_FILE_PATH = "reglas.json"


def load_propositions():
    if os.path.exists(PROP_FILE_PATH):
        with open(PROP_FILE_PATH, "r") as f:
            return json.load(f)
    else:
        print("El archivo de proposiciones no existe. El programa se cerrará.")
        sys.exit(1)


def load_rules():
    if os.path.exists(RULES_FILE_PATH):
        with open(RULES_FILE_PATH, "r") as f:
            rules_data = json.load(f)
            return [
                (set(rule["requisitos"]), rule["conclusion"]) for rule in rules_data
            ]
    else:
        print("El archivo de reglas no existe. El programa se cerrará.")
        sys.exit(1)


def save_rules(rules):
    with open(RULES_FILE_PATH, "w") as f:
        rules_data = [
            {"requisitos": list(reqs), "conclusion": concl} for reqs, concl in rules
        ]
        json.dump(rules_data, f, indent=4)


propositions = load_propositions()
rules = load_rules()


def show_propositions():
    print("\n--- Proposiciones Disponibles ---")
    for key, value in sorted(propositions.items()):
        print(f"{key}: {value}")
    print("0: Salir")


def get_selection():
    selection = input(
        "\nEscriba las letras de las proposiciones observadas, separadas por comas (ej: A,B,C), o 0 para salir:\n> "
    ).strip()
    if selection == "0":
        print("Programa finalizado.")
        sys.exit(0)
    return {
        p.strip().upper()
        for p in selection.split(",")
        if p.strip().upper() in propositions
    }


def evaluate_rules(selected):
    conclusions = []
    for requirements, conclusion in rules:
        if requirements.issubset(selected):
            conclusions.append(conclusion)
    return conclusions


def add_new_rule(selected):
    print("\n--- No se encontró ninguna regla que coincida con estas proposiciones ---")
    add = (
        input("¿Desea agregar una nueva regla basada en esta combinación? (s/n): ")
        .strip()
        .lower()
    )
    if add == "s":
        description = input(
            "Escriba una descripción/conclusión para esta nueva regla:\n> "
        )
        rules.append((selected, description))
        save_rules(rules)
        print("Nueva regla agregada.")
    else:
        print("No se agregó ninguna regla nueva.")


def main():
    print("Sistema Experto: Diagnóstico de Plantas")
    try:
        while True:
            show_propositions()
            selection = get_selection()
            print("\n--- Proposiciones seleccionadas ---")
            for p in selection:
                print(f"{p}: {propositions[p]}")
            print("\n--- Diagnóstico ---")
            result = evaluate_rules(selection)
            if result:
                for r in result:
                    print(r)
            else:
                print("No se cumple ninguna condición.")
                add_new_rule(selection)
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
        sys.exit(0)


if __name__ == "__main__":
    main()
