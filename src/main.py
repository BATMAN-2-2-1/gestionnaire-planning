import employe
import planning
from datetime import datetime

def afficher_menu():
    print("\n=== Gestionnaire de Planning ===")
    print("1. Ajouter un employé")
    print("2. Modifier l'intitulé de poste d'un employé")
    print("3. Ajouter un rendez-vous")
    print("4. Afficher le planning d'un employé")
    print("5. Afficher le planning de toute l'entreprise")
    print("6. Supprimer un employé")
    print("7. Gérer les congés")
    print("8. Quitter")

def afficher_liste_employes(employes):
    print("\nListe des employés :")
    for id_emp, info in employes.items():
        print(f"ID : {id_emp} | Nom : {info['prenom']} {info['nom']} | Poste : {info['poste']}")

def ajouter_employe_main(employes, planning_employes):
    nom = input("Nom de l'employé : ")
    prenom = input("Prénom de l'employé : ")
    poste = input("Intitulé du poste : ")
    id_employe = "id" + str(len(employes) + 1)
    employe.ajouter_employe(employes, id_employe, nom, prenom, poste)

    horaires_travail = {jour: [f"{heure:02d}:00" for heure in range(10, 18)] for jour in ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]}
    planning_employes[id_employe] = horaires_travail

    print(f"Employé {prenom} {nom} ajouté avec le poste : {poste}.")

def modifier_poste_main(employes):
    if not employes:
        print("Aucun employé enregistré.")
        return
    afficher_liste_employes(employes)
    id_employe = input("Entrez l'ID de l'employé à modifier : ")
    if id_employe in employes:
        nouveau_poste = input("Entrez le nouveau poste : ")
        employes[id_employe]["poste"] = nouveau_poste
        print(f"Poste de {employes[id_employe]['prenom']} {employes[id_employe]['nom']} modifié en : {nouveau_poste}")
    else:
        print("Employé non trouvé.")

def afficher_disponibilites_employe(planning_employes, id_employe):
    print(f"Disponibilités de {id_employe}:")
    for jour, horaires in planning_employes[id_employe].items():
        print(f"{jour.capitalize()} : {', '.join(horaires)}")

def ajouter_rendez_vous_main(planning_employes, employes):
    if not employes:
        print("Aucun employé enregistré.")
        return
    afficher_liste_employes(employes)
    id_employe = input("Entrez l'ID de l'employé pour ajouter un rendez-vous : ")
    if id_employe in employes:
        afficher_disponibilites_employe(planning_employes, id_employe)

        jour = input("Jour du rendez-vous (ex: lundi) : ").lower()
        heure_debut = input("Heure de début (ex: 10:00) : ")
        heure_fin = input("Heure de fin (ex: 11:00) : ")

        if heure_debut >= heure_fin:
            print("Erreur : L'heure de fin doit être après l'heure de début.")
            return

        description = input("Description de la tâche ou rendez-vous : ")

        if planning.ajouter_rendez_vous(planning_employes, employes, id_employe, jour, heure_debut, heure_fin, description):
            print(f"Rendez-vous ajouté pour {id_employe} : {jour} de {heure_debut} à {heure_fin} -> {description}.")
        else:
            print("Erreur : Impossible d'ajouter le rendez-vous (conflit ou indisponibilité).")
    else:
        print("Employé non trouvé.")

def afficher_planning_employe_main(planning_employes, employes):
    if not employes:
        print("Aucun employé enregistré.")
        return
    afficher_liste_employes(employes)
    id_employe = input("Entrez l'ID de l'employé : ")
    if id_employe in planning_employes:
        afficher_disponibilites_employe(planning_employes, id_employe)
    else:
        print("Employé non trouvé.")

def afficher_planning_entreprise_main(planning_employes, employes):
    print("\nPlanning de toute l'entreprise :")
    for id_employe in employes:
        afficher_disponibilites_employe(planning_employes, id_employe)
        print("-" * 30)

def supprimer_employe_main(employes, planning_employes):
    if not employes:
        print("Aucun employé enregistré.")
        return
    afficher_liste_employes(employes)
    id_employe = input("Entrez l'ID de l'employé à supprimer : ")
    if id_employe in employes:
        del employes[id_employe]
        if id_employe in planning_employes:
            del planning_employes[id_employe]
        print(f"Employé {id_employe} supprimé avec succès.")
    else:
        print("Employé non trouvé.")

def verifier_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def gerer_conges(employes):
    if not employes:
        print("Aucun employé enregistré.")
        return

    print("\nGestion des congés :")
    print("1. Ajouter un congé")
    print("2. Afficher les congés")
    print("3. Modifier un congé")
    print("4. Supprimer un congé")
    print("5. Retour")

    choix = input("Choisissez une option (1-5) : ")

    if choix == "1":
        afficher_liste_employes(employes)
        id_employe = input("ID employé : ")
        debut = input("Date de début du congé (YYYY-MM-DD) : ")
        fin = input("Date de fin du congé (YYYY-MM-DD) : ")
        if not verifier_date(debut) or not verifier_date(fin):
            print("Erreur : Format de date invalide.")
            return
        if debut > fin:
            print("Erreur : la date de début doit être avant la date de fin.")
            return
        if employe.ajouter_conge(employes, id_employe, debut, fin):
            print("Congé ajouté.")
        else:
            print("Erreur lors de l'ajout.")

    elif choix == "2":
        afficher_liste_employes(employes)
        id_employe = input("ID employé : ")
        conges = employe.afficher_conges(employes, id_employe)
        if conges:
            for debut, fin in conges:
                print(f"Du {debut} au {fin}")
        else:
            print("Aucun congé trouvé.")

    elif choix == "3":
        afficher_liste_employes(employes)
        id_employe = input("ID employé : ")
        ancien_debut = input("Ancienne date de début : ")
        ancien_fin = input("Ancienne date de fin : ")
        nouveau_debut = input("Nouvelle date de début : ")
        nouveau_fin = input("Nouvelle date de fin : ")
        if not all(map(verifier_date, [ancien_debut, ancien_fin, nouveau_debut, nouveau_fin])):
            print("Erreur : Format de date invalide.")
            return
        if nouveau_debut > nouveau_fin:
            print("Erreur : la nouvelle date de début doit être avant la nouvelle date de fin.")
            return
        if employe.modifier_conge(employes, id_employe, ancien_debut, ancien_fin, nouveau_debut, nouveau_fin):
            print("Congé modifié.")
        else:
            print("Erreur lors de la modification.")

    elif choix == "4":
        afficher_liste_employes(employes)
        id_employe = input("ID employé : ")
        debut = input("Date de début du congé à supprimer : ")
        fin = input("Date de fin du congé à supprimer : ")
        if not verifier_date(debut) or not verifier_date(fin):
            print("Erreur : Format de date invalide.")
            return
        if employe.supprimer_conge(employes, id_employe, debut, fin):
            print("Congé supprimé.")
        else:
            print("Erreur lors de la suppression.")

    elif choix == "5":
        return
    else:
        print("Option invalide.")

def main():
    employes = {}
    planning_employes = {}

    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-8) : ")

        if choix == "1":
            ajouter_employe_main(employes, planning_employes)
        elif choix == "2":
            modifier_poste_main(employes)
        elif choix == "3":
            ajouter_rendez_vous_main(planning_employes, employes)
        elif choix == "4":
            afficher_planning_employe_main(planning_employes, employes)
        elif choix == "5":
            afficher_planning_entreprise_main(planning_employes, employes)
        elif choix == "6":
            supprimer_employe_main(employes, planning_employes)
        elif choix == "7":
            gerer_conges(employes)
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Essayez encore.")

if __name__ == "__main__":
    main()
