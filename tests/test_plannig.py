# On importe unittest pour créer les tests
import unittest

# On importe les modules qu'on veut tester
import planning
import employe  # on a besoin des employés pour tester les plannings

class TestPlanning(unittest.TestCase):
    """Classe de tests pour les fonctions du module planning."""

    def setUp(self):
        """Méthode exécutée avant chaque test : prépare des employés et un planning vide."""
        self.employes = {}
        self.planning = planning.creer_planning()

        # Ajouter un employé pour les tests
        employe.ajouter_employe(self.employes, "id1", "Durand", "Alice", "Manager")
        employe.ajouter_disponibilite(self.employes, "id1", "lundi", "09:00-17:00")

    def test_ajouter_rendez_vous_ok(self):
        """Teste l'ajout d'un rendez-vous sans conflit."""
        resultat = planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "lundi", "10:00", "11:00", "Réunion équipe")
        
        self.assertTrue(resultat)  # Doit réussir
        self.assertEqual(len(self.planning["id1"]), 1)  # 1 rendez-vous ajouté
        self.assertEqual(self.planning["id1"][0][3], "Réunion équipe")  # Vérifie la description

    def test_ajouter_rendez_vous_conflit(self):
        """Teste l'ajout d'un rendez-vous en conflit avec un autre existant."""
        # Premier rendez-vous ajouté
        planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "lundi", "10:00", "11:00", "Réunion 1")

        # Deuxième rendez-vous qui chevauche le premier => doit échouer
        resultat = planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "lundi", "10:30", "11:30", "Réunion 2")
        
        self.assertFalse(resultat)  # Conflit détecté

    def test_ajouter_rendez_vous_pas_dispo(self):
        """Teste l'ajout d'un rendez-vous hors des disponibilités de l'employé."""
        # L'employé est dispo que le lundi de 09:00 à 17:00
        resultat = planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "mardi", "10:00", "11:00", "Client meeting")

        self.assertFalse(resultat)  # Pas disponible le mardi

    def test_afficher_planning_employe(self):
        """Teste l'affichage du planning d'un seul employé (ne teste pas le print, juste que ça ne plante pas)."""
        planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "lundi", "10:00", "11:00", "Réunion équipe")

        # On appelle juste la fonction pour vérifier qu'elle s'exécute (pas d'erreur)
        planning.afficher_planning_employe(self.planning, self.employes, "id1")

    def test_afficher_planning_entreprise(self):
        """Teste l'affichage du planning de toute l'entreprise (ne teste pas le print, juste que ça ne plante pas)."""
        planning.ajouter_rendez_vous(self.planning, self.employes, "id1", "lundi", "10:00", "11:00", "Réunion équipe")

        # On appelle juste la fonction pour vérifier qu'elle s'exécute
        planning.afficher_planning_entreprise(self.planning, self.employes)

# Permet d'exécuter les tests si on lance directement ce fichier
if __name__ == "__main__":
    unittest.main()
