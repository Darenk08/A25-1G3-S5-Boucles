import pytest #importer le module pytest pour faire nos tests unitaires
from ExDebug1 import environnement_optimal # importer la fonction de notre autre fichier
#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    #Arrange : préparer les variables d'entrée et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "tout est sous contrôle!"

    #act : appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #assert: vérifier le résultat
    assert resultat_attendu == resultat_attendu
