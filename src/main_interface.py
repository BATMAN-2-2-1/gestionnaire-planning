import tkinter as tk
from tkinter import messagebox
import employe
import planning
from datetime import datetime

# Données
donnees_employes = {}
planning_employes = planning.creer_planning()

# Fonctions Utilitaires
def verifier_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Fonctions GUI
def ajouter_employe_gui():
    def valider():
        nom = entry_nom.get()
        prenom = entry_prenom.get()
        poste = entry_poste.get()
        if nom and prenom and poste:
            id_emp = "id" + str(len(donnees_employes) + 1)
            employe.ajouter_employe(donnees_employes, id_emp, nom, prenom, poste)
            # Ajout de disponibilités standard (lundi-vendredi, 10h-18h)
            for jour in ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]:
                employe.ajouter_disponibilite(donnees_employes, id_emp, jour, "10:00-18:00")
            messagebox.showinfo("Succès", f"Employé {prenom} {nom} ajouté.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")

    fenetre = tk.Toplevel(root)
    fenetre.title("Ajouter un Employé")
    tk.Label(fenetre, text="Nom :").pack()
    entry_nom = tk.Entry(fenetre)
    entry_nom.pack()
    tk.Label(fenetre, text="Prénom :").pack()
    entry_prenom = tk.Entry(fenetre)
    entry_prenom.pack()
    tk.Label(fenetre, text="Poste :").pack()
    entry_poste = tk.Entry(fenetre)
    entry_poste.pack()
    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)

def modifier_poste_gui():
    def valider():
        id_emp = entry_id.get()
        nouveau_poste = entry_poste.get()
        if id_emp in donnees_employes and nouveau_poste:
            employe.modifier_poste(donnees_employes, id_emp, nouveau_poste)
            messagebox.showinfo("Succès", "Poste modifié.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Données invalides.")

    fenetre = tk.Toplevel(root)
    fenetre.title("Modifier un Poste")
    tk.Label(fenetre, text="ID Employé :").pack()
    entry_id = tk.Entry(fenetre)
    entry_id.pack()
    tk.Label(fenetre, text="Nouveau Poste :").pack()
    entry_poste = tk.Entry(fenetre)
    entry_poste.pack()
    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)

def ajouter_rendez_vous_gui():
    def valider():
        id_emp = entry_id.get()
        jour = entry_jour.get().lower()
        debut = entry_debut.get()
        fin = entry_fin.get()
        desc = entry_desc.get()
        if id_emp in donnees_employes and jour and debut and fin and desc:
            if planning.ajouter_rendez_vous(planning_employes, donnees_employes, id_emp, jour, debut, fin, desc):
                messagebox.showinfo("Succès", "Rendez-vous ajouté.")
                fenetre.destroy()
            else:
                messagebox.showerror("Erreur", "Impossible d'ajouter (conflit ou indisponible).")
        else:
            messagebox.showerror("Erreur", "Données invalides.")

    fenetre = tk.Toplevel(root)
    fenetre.title("Ajouter un Rendez-vous")
    tk.Label(fenetre, text="ID Employé :").pack()
    entry_id = tk.Entry(fenetre)
    entry_id.pack()
    tk.Label(fenetre, text="Jour :").pack()
    entry_jour = tk.Entry(fenetre)
    entry_jour.pack()
    tk.Label(fenetre, text="Heure Début (ex: 10:00) :").pack()
    entry_debut = tk.Entry(fenetre)
    entry_debut.pack()
    tk.Label(fenetre, text="Heure Fin (ex: 11:00) :").pack()
    entry_fin = tk.Entry(fenetre)
    entry_fin.pack()
    tk.Label(fenetre, text="Description :").pack()
    entry_desc = tk.Entry(fenetre)
    entry_desc.pack()
    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)

def afficher_planning_employe_gui():
    def valider():
        id_emp = entry_id.get()
        if id_emp in donnees_employes:
            fenetre_resultat = tk.Toplevel(root)
            fenetre_resultat.title(f"Planning de {donnees_employes[id_emp]['prenom']} {donnees_employes[id_emp]['nom']}")
            if id_emp in planning_employes and planning_employes[id_emp]:
                for rdv in planning_employes[id_emp]:
                    jour, debut, fin, description = rdv
                    tk.Label(fenetre_resultat, text=f"{jour.capitalize()} : {debut}-{fin} -> {description}").pack()
            else:
                tk.Label(fenetre_resultat, text="Aucun rendez-vous.").pack()
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Employé non trouvé.")

    fenetre = tk.Toplevel(root)
    fenetre.title("Afficher Planning Employé")
    tk.Label(fenetre, text="ID Employé :").pack()
    entry_id = tk.Entry(fenetre)
    entry_id.pack()
    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)

def afficher_planning_entreprise_gui():
    fenetre = tk.Toplevel(root)
    fenetre.title("Planning Entreprise")
    for id_emp in donnees_employes:
        infos = donnees_employes[id_emp]
        tk.Label(fenetre, text=f"{infos['prenom']} {infos['nom']} ({infos['poste']})").pack()
        if id_emp in planning_employes and planning_employes[id_emp]:
            for rdv in planning_employes[id_emp]:
                jour, debut, fin, description = rdv
                tk.Label(fenetre, text=f"{jour.capitalize()} : {debut}-{fin} -> {description}").pack()
        else:
            tk.Label(fenetre, text="Aucun rendez-vous.").pack()
        tk.Label(fenetre, text="-----------------").pack()

def supprimer_employe_gui():
    def valider():
        id_emp = entry_id.get()
        if id_emp in donnees_employes:
            del donnees_employes[id_emp]
            if id_emp in planning_employes:
                del planning_employes[id_emp]
            messagebox.showinfo("Succès", "Employé supprimé.")
            fenetre.destroy()
        else:
            messagebox.showerror("Erreur", "Employé non trouvé.")

    fenetre = tk.Toplevel(root)
    fenetre.title("Supprimer un Employé")
    tk.Label(fenetre, text="ID Employé :").pack()
    entry_id = tk.Entry(fenetre)
    entry_id.pack()
    tk.Button(fenetre, text="Valider", command=valider).pack(pady=10)
def gerer_conges_gui():
    fen_conges = tk.Toplevel(root)
    fen_conges.title("Gérer les Congés")

    def ajouter_conge():
        def valider():
            id_emp = entry_id.get()
            debut = entry_debut.get()
            fin = entry_fin.get()
            if id_emp in donnees_employes and verifier_date(debut) and verifier_date(fin) and debut <= fin:
                employe.ajouter_conge(donnees_employes, id_emp, debut, fin)
                messagebox.showinfo("Succès", "Congé ajouté.")
                fenetre_ajouter.destroy()
            else:
                messagebox.showerror("Erreur", "Données invalides.")

        fenetre_ajouter = tk.Toplevel(fen_conges)
        fenetre_ajouter.title("Ajouter un Congé")
        tk.Label(fenetre_ajouter, text="ID Employé :").pack()
        entry_id = tk.Entry(fenetre_ajouter)
        entry_id.pack()
        tk.Label(fenetre_ajouter, text="Date Début (YYYY-MM-DD) :").pack()
        entry_debut = tk.Entry(fenetre_ajouter)
        entry_debut.pack()
        tk.Label(fenetre_ajouter, text="Date Fin (YYYY-MM-DD) :").pack()
        entry_fin = tk.Entry(fenetre_ajouter)
        entry_fin.pack()
        tk.Button(fenetre_ajouter, text="Valider", command=valider).pack(pady=10)

    def afficher_conges():
        fenetre_afficher = tk.Toplevel(fen_conges)
        fenetre_afficher.title("Afficher les Congés")
        for id_emp, infos in donnees_employes.items():
            tk.Label(fenetre_afficher, text=f"{infos['prenom']} {infos['nom']} ({infos['poste']})").pack()
            conges = employe.afficher_conges(donnees_employes, id_emp)
            if conges:
                for debut, fin in conges:
                    tk.Label(fenetre_afficher, text=f"Du {debut} au {fin}").pack()
            else:
                tk.Label(fenetre_afficher, text="Aucun congé.").pack()
            tk.Label(fenetre_afficher, text="-----------------").pack()

    def modifier_conge():
        def valider():
            id_emp = entry_id.get()
            ancien_debut = entry_ancien_debut.get()
            ancien_fin = entry_ancien_fin.get()
            nouveau_debut = entry_nouveau_debut.get()
            nouveau_fin = entry_nouveau_fin.get()
            if id_emp in donnees_employes and all(map(verifier_date, [ancien_debut, ancien_fin, nouveau_debut, nouveau_fin])) and nouveau_debut <= nouveau_fin:
                if employe.modifier_conge(donnees_employes, id_emp, ancien_debut, ancien_fin, nouveau_debut, nouveau_fin):
                    messagebox.showinfo("Succès", "Congé modifié.")
                    fenetre_modifier.destroy()
                else:
                    messagebox.showerror("Erreur", "Ancien congé non trouvé.")
            else:
                messagebox.showerror("Erreur", "Données invalides.")

        fenetre_modifier = tk.Toplevel(fen_conges)
        fenetre_modifier.title("Modifier un Congé")
        tk.Label(fenetre_modifier, text="ID Employé :").pack()
        entry_id = tk.Entry(fenetre_modifier)
        entry_id.pack()
        tk.Label(fenetre_modifier, text="Ancienne Date Début :").pack()
        entry_ancien_debut = tk.Entry(fenetre_modifier)
        entry_ancien_debut.pack()
        tk.Label(fenetre_modifier, text="Ancienne Date Fin :").pack()
        entry_ancien_fin = tk.Entry(fenetre_modifier)
        entry_ancien_fin.pack()
        tk.Label(fenetre_modifier, text="Nouvelle Date Début :").pack()
        entry_nouveau_debut = tk.Entry(fenetre_modifier)
        entry_nouveau_debut.pack()
        tk.Label(fenetre_modifier, text="Nouvelle Date Fin :").pack()
        entry_nouveau_fin = tk.Entry(fenetre_modifier)
        entry_nouveau_fin.pack()
        tk.Button(fenetre_modifier, text="Valider", command=valider).pack(pady=10)

    def supprimer_conge():
        def valider():
            id_emp = entry_id.get()
            debut = entry_debut.get()
            fin = entry_fin.get()
            if id_emp in donnees_employes and verifier_date(debut) and verifier_date(fin):
                if employe.supprimer_conge(donnees_employes, id_emp, debut, fin):
                    messagebox.showinfo("Succès", "Congé supprimé.")
                    fenetre_supprimer.destroy()
                else:
                    messagebox.showerror("Erreur", "Congé non trouvé.")
            else:
                messagebox.showerror("Erreur", "Données invalides.")

        fenetre_supprimer = tk.Toplevel(fen_conges)
        fenetre_supprimer.title("Supprimer un Congé")
        tk.Label(fenetre_supprimer, text="ID Employé :").pack()
        entry_id = tk.Entry(fenetre_supprimer)
        entry_id.pack()
        tk.Label(fenetre_supprimer, text="Date Début :").pack()
        entry_debut = tk.Entry(fenetre_supprimer)
        entry_debut.pack()
        tk.Label(fenetre_supprimer, text="Date Fin :").pack()
        entry_fin = tk.Entry(fenetre_supprimer)
        entry_fin.pack()
        tk.Button(fenetre_supprimer, text="Valider", command=valider).pack(pady=10)

    # Boutons de la fenêtre \"Gérer les congés\"
    tk.Button(fen_conges, text="Ajouter un Congé", command=ajouter_conge).pack(fill='x')
    tk.Button(fen_conges, text="Afficher les Congés", command=afficher_conges).pack(fill='x')
    tk.Button(fen_conges, text="Modifier un Congé", command=modifier_conge).pack(fill='x')
    tk.Button(fen_conges, text="Supprimer un Congé", command=supprimer_conge).pack(fill='x')
    tk.Button(fen_conges, text="Retour", command=fen_conges.destroy).pack(fill='x', pady=10)
# Fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de Planning")

# Menu Principal
tk.Button(root, text="Ajouter un Employé", command=ajouter_employe_gui).pack(fill='x')
tk.Button(root, text="Modifier Poste Employé", command=modifier_poste_gui).pack(fill='x')
tk.Button(root, text="Ajouter Rendez-vous", command=ajouter_rendez_vous_gui).pack(fill='x')
tk.Button(root, text="Afficher Planning Entreprise", command=afficher_planning_entreprise_gui).pack(fill='x')
tk.Button(root, text="Afficher Planning Employé", command=afficher_planning_employe_gui).pack(fill='x')
tk.Button(root, text="Supprimer Employé", command=supprimer_employe_gui).pack(fill='x')
tk.Button(root, text="Gérer les Congés", command=gerer_conges_gui).pack(fill='x')
tk.Button(root, text="Quitter", command=root.destroy).pack(fill='x', pady=10)

# Boucle
def main():
    root.mainloop()

if __name__ == "__main__":
    main()
