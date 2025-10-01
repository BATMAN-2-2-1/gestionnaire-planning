# On importe le module unittest pour pouvoir écrire des tests unitaires
import unittest

# On importe notre module employe (celui qu'on veut tester)
import employe

class TestEmploye(unittest.TestCase):
    """Classe de tests pour toutes les fonctions du module employe."""

    def setUp(self):
        """Méthode exécutée avant chaque test : elle initialise un dictionnaire vide d'employés."""
        self.employes = {}

    def test_ajouter_employe(self):
        """Teste l'ajout d'un nouvel employé."""
        employe.ajouter_employe(self.employes, "id1", "Dupont", "Alice", "Manager")

        # On vérifie que l'employé a bien été ajouté dans le dictionnaire
        self.assertIn("id1", self.employes)

        # On vérifie que les informations de l'employé sont correctes
        self.assertEqual(self.employes["id1"]["nom"], "Dupont")
        self.assertEqual(self.employes["id1"]["prenom"], "Alice")
        self.assertEqual(self.employes["id1"]["poste"], "Manager")
        self.assertEqual(self.employes["id1"]["disponibilites"], [])  # Disponibilités vide au départ

    def test_supprimer_employe(self):
        """Teste la suppression d'un employé existant."""
        # D'abord on ajoute un employé pour pouvoir le supprimer
        employe.ajouter_employe(self.employes, "id2", "Martin", "Bob", "Technicien")

        # On supprime l'employé
        resultat = employe.supprimer_employe(self.employes, "id2")

        # Le résultat doit être True (la suppression a réussi)
        self.assertTrue(resultat)

        # L'employé ne doit plus être dans le dictionnaire
        self.assertNotIn("id2", self.employes)

    def test_supprimer_employe_inexistant(self):
        """Teste la suppression d'un employé qui n'existe pas."""
        # On essaie de supprimer un employé qui n'est pas dans le dictionnaire
        resultat = employe.supprimer_employe(self.employes, "id3")

        # Le résultat doit être False (car l'employé n'existe pas)
        self.assertFalse(resultat)

    def test_modifier_poste(self):
        """Teste la modification du poste d'un employé existant."""
        employe.ajouter_employe(self.employes, "id4", "Durand", "Claire", "Secrétaire")

        # On modifie le poste de l'employé
        resultat = employe.modifier_poste(self.employes, "id4", "Responsable RH")

        # La modification doit réussir
        self.assertTrue(resultat)

        # Le poste doit avoir été mis à jour
        self.assertEqual(self.employes["id4"]["poste"], "Responsable RH")

    def test_modifier_poste_inexistant(self):
        """Teste la modification du poste d'un employé qui n'existe pas."""
        # On essaie de modifier un employé qui n'existe pas
        resultat = employe.modifier_poste(self.employes, "id5", "Directeur")

        # Cela doit échouer (False)
        self.assertFalse(resultat)

    def test_ajouter_disponibilite(self):
        """Teste l'ajout d'une disponibilité à un employé."""
        employe.ajouter_employe(self.employes, "id6", "Petit", "Luc", "Agent")

        # On ajoute une disponibilité
        resultat = employe.ajouter_disponibilite(self.employes, "id6", "lundi", "09:00-12:00")

        # Cela doit réussir
        self.assertTrue(resultat)

        # La disponibilité doit apparaître dans la liste
        self.assertIn(("lundi", "09:00-12:00"), self.employes["id6"]["disponibilites"])

    def test_supprimer_disponibilite(self):
        """Teste la suppression d'une disponibilité existante."""
        employe.ajouter_employe(self.employes, "id7", "Lemoine", "Sophie", "Comptable")
        employe.ajouter_disponibilite(self.employes, "id7", "mardi", "14:00-17:00")

        # On supprime la disponibilité
        resultat = employe.supprimer_disponibilite(self.employes, "id7", "mardi", "14:00-17:00")

        # Cela doit réussir
        self.assertTrue(resultat)

        # La disponibilité ne doit plus être dans la liste
        self.assertNotIn(("mardi", "14:00-17:00"), self.employes["id7"]["disponibilites"])

    def test_supprimer_disponibilite_inexistante(self):
        """Teste la suppression d'une disponibilité qui n'existe pas."""
        employe.ajouter_employe(self.employes, "id8", "Moreau", "Julien", "Analyste")

        # On essaie de supprimer une disponibilité qui n'existe pas
        resultat = employe.supprimer_disponibilite(self.employes, "id8", "mercredi", "10:00-12:00")

        # Cela doit échouer
        self.assertFalse(resultat)
    def test_ajouter_conge(self):
        """Teste l'ajout d'un congé pour un employé."""
        employe.ajouter_employe(self.employes, "id9", "Blanc", "Nina", "Assistante")
        
        # On ajoute un congé
        resultat = employe.ajouter_conge(self.employes, "id9", "2025-06-01", "2025-06-10")
        
        # Cela doit réussir
        self.assertTrue(resultat)

        # Le congé doit apparaître dans la liste
        self.assertIn(("2025-06-01", "2025-06-10"), self.employes["id9"]["conges"])

    def test_afficher_conges(self):
        """Teste l'affichage des congés d'un employé."""
        employe.ajouter_employe(self.employes, "id10", "Roux", "Paul", "Développeur")
        employe.ajouter_conge(self.employes, "id10", "2025-07-15", "2025-07-20")
        
        # On récupère la liste des congés
        conges = employe.afficher_conges(self.employes, "id10")
        
        # Elle doit contenir la bonne période
        self.assertEqual(conges, [("2025-07-15", "2025-07-20")])

    def test_modifier_conge(self):
        """Teste la modification d'un congé existant."""
        employe.ajouter_employe(self.employes, "id11", "Noir", "Léa", "Designer")
        employe.ajouter_conge(self.employes, "id11", "2025-08-01", "2025-08-05")
        
        # On modifie le congé
        resultat = employe.modifier_conge(
            self.employes,
            "id11",
            "2025-08-01", "2025-08-05",
            "2025-08-10", "2025-08-15"
        )
        
        # La modification doit réussir
        self.assertTrue(resultat)

        # Le congé doit avoir été modifié
        self.assertIn(("2025-08-10", "2025-08-15"), self.employes["id11"]["conges"])
        self.assertNotIn(("2025-08-01", "2025-08-05"), self.employes["id11"]["conges"])

    def test_supprimer_conge(self):
        """Teste la suppression d'un congé existant."""
        employe.ajouter_employe(self.employes, "id12", "Vert", "Tom", "Chef de projet")
        employe.ajouter_conge(self.employes, "id12", "2025-09-01", "2025-09-10")
        
        # On supprime le congé
        resultat = employe.supprimer_conge(self.employes, "id12", "2025-09-01", "2025-09-10")
        
        # La suppression doit réussir
        self.assertTrue(resultat)

        # Le congé ne doit plus être dans la liste
        self.assertNotIn(("2025-09-01", "2025-09-10"), self.employes["id12"]["conges"])

    def test_supprimer_conge_inexistant(self):
        """Teste la suppression d'un congé qui n'existe pas."""
        employe.ajouter_employe(self.employes, "id13", "Bleu", "Anna", "Comptable")
        
        # On essaie de supprimer un congé qui n'existe pas
        resultat = employe.supprimer_conge(self.employes, "id13", "2025-10-01", "2025-10-05")
        
        # Cela doit échouer
        self.assertFalse(resultat)

# Ce code permet de lancer tous les tests si ce fichier est exécuté directement
if __name__ == "__main__":
    unittest.main()
