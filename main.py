
taches = []


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        tache = {
            "numero": len(taches) + 1,
            "titre": titre
        }

        taches.append(tache)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche disponible.")
    else:
        print("\n=== LISTE DES TÂCHES ===")

        for tache in taches:
            print(tache["numero"], "-", tache["titre"])


def rechercher_tache():
    mot_cle = input("Mot-clé à rechercher : ").strip().lower()

    trouve = False

    for tache in taches:
        if mot_cle in tache["titre"].lower():
            print(tache["numero"], "-", tache["titre"])
            trouve = True

    if not trouve:
        print("Aucune tâche trouvée.")


def menu():
    while True:
        print("\n=== GESTION DES TÂCHES ===")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Rechercher une tâche")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_tache()

        elif choix == "2":
            afficher_taches()

        elif choix == "3":
            rechercher_tache()

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Erreur : option invalide.")


menu()
