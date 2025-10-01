def creer_planning():
    """
    Crée un dictionnaire vide pour stocker le planning.
    Clé = identifiant employé
    Valeur = liste de tuples (jour, heure_debut, heure_fin, description de la tâche)
    """
    return {}

def ajouter_rendez_vous(planning, employes, id_employe, jour, heure_debut, heure_fin, description):
    """
    Attribue un rendez-vous ou une tâche à un employé.

    - Vérifie que l'employé existe.
    - Vérifie qu'il n'y a pas de conflit avec d'autres rendez-vous.
    - Vérifie que l'employé est disponible sur ce créneau.
    
    Retourne :
    - True si le rendez-vous est ajouté.
    - False sinon (exemple : conflit, employé inexistant, pas dispo).
    """

    # Vérifie que l'employé existe
    if id_employe not in employes:
        return False

    # Vérifie que l'employé est disponible à ce moment-là
    disponibilites = employes[id_employe]["disponibilites"]
    disponible = False
    for jour_dispo, horaire_dispo in disponibilites:
        if jour_dispo == jour:
            debut_dispo, fin_dispo = horaire_dispo.split('-')
            if debut_dispo <= heure_debut and heure_fin <= fin_dispo:
                disponible = True
                break

    if not disponible:
        return False

    # Initialiser la liste de planning pour l'employé si elle n'existe pas
    if id_employe not in planning:
        planning[id_employe] = []

    # Vérifie les conflits avec les rendez-vous existants
    for rdv in planning[id_employe]:
        jour_rdv, debut_rdv, fin_rdv, _ = rdv
        if jour_rdv == jour:
            if not (heure_fin <= debut_rdv or heure_debut >= fin_rdv):
                return False  # Conflit détecté

    # Ajoute le rendez-vous
    planning[id_employe].append((jour, heure_debut, heure_fin, description))
    return True

def afficher_planning_employe(planning, employes, id_employe):
    """
    Affiche le planning d'un employé donné.
    """

    if id_employe not in employes:
        print("Employé non trouvé.")
        return

    print(f"Planning de {employes[id_employe]['prenom']} {employes[id_employe]['nom']} :")

    if id_employe not in planning or not planning[id_employe]:
        print("Aucun rendez-vous.")
        return

    for rdv in sorted(planning[id_employe]):
        jour, debut, fin, description = rdv
        print(f"{jour} : {debut} - {fin} -> {description}")

def afficher_planning_entreprise(planning, employes):
    """
    Affiche le planning de toute l'entreprise.
    """
    print("Planning de l'entreprise :")
    for id_employe in employes:
        afficher_planning_employe(planning, employes, id_employe)
        print("-" * 30)
