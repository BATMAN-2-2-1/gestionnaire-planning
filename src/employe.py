def ajouter_employe(employes, id_employe, nom, prenom, poste):
    """
    Ajoute un nouvel employé au dictionnaire des employés.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        nom (str): Le nom de l'employé.
        prenom (str): Le prénom de l'employé.
        poste (str): L'intitulé du poste de l'employé.

    Returns:
        None
    """
    employes[id_employe] = {
        "nom": nom,
        "prenom": prenom,
        "poste": poste,
        "disponibilites": [],
        "conges": []  # ➔ AJOUT d'un champ pour gérer les congés
    }

def supprimer_employe(employes, id_employe):
    """
    Supprime un employé du dictionnaire des employés.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé à supprimer.

    Returns:
        bool: True si l'employé a été supprimé, False sinon.
    """
    if id_employe in employes:
        del employes[id_employe]
        return True
    return False

def modifier_poste(employes, id_employe, nouveau_poste):
    """
    Modifie l'intitulé du poste d'un employé existant.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        nouveau_poste (str): Le nouveau poste de l'employé.

    Returns:
        bool: True si le poste a été modifié, False sinon.
    """
    if id_employe in employes:
        employes[id_employe]["poste"] = nouveau_poste
        return True
    return False

def ajouter_disponibilite(employes, id_employe, jour, plage_horaire):
    """
    Ajoute une disponibilité à un employé.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        jour (str): Le jour de la disponibilité (ex: "lundi").
        plage_horaire (str): La plage horaire (ex: "09:00-12:00").

    Returns:
        bool: True si la disponibilité a été ajoutée, False sinon.
    """
    if id_employe in employes:
        employes[id_employe]["disponibilites"].append((jour, plage_horaire))
        return True
    return False

def supprimer_disponibilite(employes, id_employe, jour, plage_horaire):
    """
    Supprime une disponibilité d'un employé.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        jour (str): Le jour de la disponibilité à supprimer.
        plage_horaire (str): La plage horaire à supprimer.

    Returns:
        bool: True si la disponibilité a été supprimée, False sinon.
    """
    if id_employe in employes:
        disponibilite = (jour, plage_horaire)
        if disponibilite in employes[id_employe]["disponibilites"]:
            employes[id_employe]["disponibilites"].remove(disponibilite)
            return True
    return False

# =============================
# Gestion des congés (AJOUTS)
# =============================

def ajouter_conge(employes, id_employe, date_debut_conge, date_fin_conge):
    """
    Ajoute une période de congé pour un employé.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        date_debut_conge (str): La date de début de congé (ex: "2025-05-10").
        date_fin_conge (str): La date de fin de congé (ex: "2025-05-15").

    Returns:
        bool: True si le congé a été ajouté, False sinon.
    """
    if id_employe in employes:
        employes[id_employe]["conges"].append((date_debut_conge, date_fin_conge))
        return True
    return False

def afficher_conges(employes, id_employe):
    """
    Affiche la liste des congés d'un employé sous forme de périodes.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.

    Returns:
        list: Liste des périodes de congé (avec date de début et de fin), ou None si l'employé n'existe pas.
    """
    if id_employe in employes:
        return employes[id_employe]["conges"]
    return None

def modifier_conge(employes, id_employe, ancien_debut_conge, ancien_fin_conge, nouveau_debut_conge, nouveau_fin_conge):
    """
    Modifie une période de congé pour un employé.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        ancien_debut_conge (str): La date de début de congé à modifier.
        ancien_fin_conge (str): La date de fin de congé à modifier.
        nouveau_debut_conge (str): La nouvelle date de début de congé.
        nouveau_fin_conge (str): La nouvelle date de fin de congé.

    Returns:
        bool: True si le congé a été modifié, False sinon.
    """
    if id_employe in employes:
        for i, (debut, fin) in enumerate(employes[id_employe]["conges"]):
            if debut == ancien_debut_conge and fin == ancien_fin_conge:
                employes[id_employe]["conges"][i] = (nouveau_debut_conge, nouveau_fin_conge)
                return True
    return False

def supprimer_conge(employes, id_employe, date_debut_conge, date_fin_conge):
    """
    Supprime une période de congé d'un employé.

    Args:
        employes (dict): Le dictionnaire des employés existants.
        id_employe (str): L'identifiant unique de l'employé.
        date_debut_conge (str): La date de début de congé à supprimer.
        date_fin_conge (str): La date de fin de congé à supprimer.

    Returns:
        bool: True si le congé a été supprimé, False sinon.
    """
    if id_employe in employes:
        congé = (date_debut_conge, date_fin_conge)
        if congé in employes[id_employe]["conges"]:
            employes[id_employe]["conges"].remove(congé)
            return True
    return False
