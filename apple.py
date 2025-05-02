import os
from collections import Counter

# Couleurs ANSI
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"

history = {}
count = {str(i): 0 for i in range(1, 6)}

def clear():
    os.system("clear")

def logo_pomme():
    print(f"""{RED}
      ,--./,-.
     /        \\
    |SOLITAIRE|
     \ HACK   /
      `._,._.'
{RESET}""")

def show_menu():
    clear()
    logo_pomme()
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║     SOLITAIRE HACK • APPLE PREDICTOR      ║
╚════════════════════════════════════════════╝{RESET}
{GREEN}1.{RESET} Entrer un bon emplacement
{GREEN}2.{RESET} Prédire le prochain coup global
{GREEN}3.{RESET} Voir les statistiques générales
{GREEN}4.{RESET} Mode Expert : prédire par niveau
{GREEN}5.{RESET} Tutoriel
{GREEN}6.{RESET} Mode d'emploi
{GREEN}99.{RESET} À propos
{GREEN}0.{RESET} Quitter
""")

def show_about():
    clear()
    logo_pomme()
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║                  À PROPOS                 ║
╚════════════════════════════════════════════╝{RESET}
Développé par   : {GREEN}SOLITAIRE HACK{RESET}
Projet          : Apple Predictor
Version         : 1.0
Langage         : Python 3
Plateforme      : Termux / Linux / Android

Ce script permet de suivre les positions gagnantes
et de prédire les choix optimaux à faire dans le jeu.

{CYAN}Contact : t.me/solitaire_hack{RESET}
""")
    input("Appuie sur Entrée pour revenir au menu...")

def show_tutoriel():
    clear()
    logo_pomme()
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║                  TUTORIEL                 ║
╚════════════════════════════════════════════╝{RESET}
{YELLOW}Comment utiliser APPLE PREDICTOR :{RESET}

1. Joue une partie dans Apple of Fortune
2. Note le niveau atteint (ex: x1.54)
3. Note la bonne position (1 à 5)
4. Ajoute ces infos via l'option 1 du menu
5. Utilise l'option 2 ou 4 pour prédire ton prochain clic

{CYAN}Conseil :{RESET}
Plus tu joues, plus le script apprend et devient précis !
""")
    input("Entrée pour continuer...")

def show_mode_emploi():
    clear()
    logo_pomme()
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║              MODE D’EMPLOI                ║
╚════════════════════════════════════════════╝{RESET}
{GREEN}PRÉREQUIS :{RESET}
- Avoir Python 3 installé (Termux : pkg install python)
- Ouvrir le script avec : python solitaire.py

{GREEN}COMMANDES :{RESET}
{YELLOW}1.{RESET} Entrer les données après chaque partie gagnée
{YELLOW}2.{RESET} Voir la prédiction globale la plus fiable
{YELLOW}3.{RESET} Afficher toutes les données collectées
{YELLOW}4.{RESET} Prédire pour un niveau spécifique (mode expert)
{YELLOW}5.{RESET} Voir le tutoriel
{YELLOW}6.{RESET} Voir ce mode d'emploi
{YELLOW}99.{RESET} Voir les infos sur le script

{GREEN}ASTUCE :{RESET}
Entraîne ton script avec de vraies données pour de meilleures prédictions.
""")
    input("Appuie sur Entrée pour revenir au menu...")

while True:
    show_menu()
    choice = input(f"{YELLOW}Choix : {RESET}").strip()

    if choice == "1":
        level = input("Niveau (ex: x1.54) : ").strip()
        pos = input("Position gagnante (1 à 5) : ").strip()
        if pos not in ["1", "2", "3", "4", "5"]:
            print(f"{RED}Position invalide.{RESET}")
            input("Entrée pour continuer...")
            continue
        history.setdefault(level, []).append(pos)
        count[pos] += 1
        print(f"{GREEN}✔ Enregistré : {level} -> {pos}{RESET}")
        input("Entrée pour continuer...")

    elif choice == "2":
        total = sum(count.values())
        if total < 5:
            print(f"{RED}Pas assez de données pour prédire. (Minimum : 5 entrées){RESET}")
        else:
            print(f"\n{CYAN}>> PRÉDICTION GLOBALE (sur {total} coups) :{RESET}")
            for pos in ["1", "2", "3", "4", "5"]:
                pct = (count[pos] / total) * 100
                print(f" - Position {pos} : {pct:.1f}%")
            best = max(count, key=count.get)
            print(f"\n{GREEN}>>> Meilleure position estimée : {best}{RESET}")
            print(f"{CYAN}~ Analyse signée SOLITAIRE HACK ~{RESET}")
        input("Entrée pour continuer...")

    elif choice == "3":
        print(f"\n{CYAN}=== STATISTIQUES GÉNÉRALES ==={RESET}")
        for k in sorted(history):
            print(f"{k} : {' | '.join(history[k])}")
        total = sum(count.values())
        print(f"\nTotal : {total} entrées")
        for pos in ["1", "2", "3", "4", "5"]:
            print(f"  - {pos} : {count[pos]}")
        input("Entrée pour continuer...")

    elif choice == "4":
        niveau = input("Entrer le niveau à analyser (ex: x1.54) : ").strip()
        if niveau not in history:
            print(f"{RED}Aucune donnée pour {niveau}.{RESET}")
        else:
            data = Counter(history[niveau])
            frequent = data.most_common(1)[0][0]
            print(f"{CYAN}>> PRÉDICTION POUR {niveau} : Position {frequent}{RESET}")
            print(f"{YELLOW}Détails : {dict(data)}{RESET}")
            print(f"{CYAN}~ Prédiction experte signée SOLITAIRE HACK ~{RESET}")
        input("Entrée pour continuer...")

    elif choice == "5":
        show_tutoriel()

    elif choice == "6":
        show_mode_emploi()

    elif choice == "99":
        show_about()

    elif choice == "0":
        print(f"{GREEN}Merci d'avoir utilisé APPLE PREDICTOR - by SOLITAIRE HACK{RESET}")
        break

    else:
        print(f"{RED}Choix invalide.{RESET}")
        input("Entrée pour continuer...")