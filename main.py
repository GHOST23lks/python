from bibliotheque import Bibliotheque
from livre import Livre
from utilisateur import Utilisateur

def menu():
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Lister les livres")
    print("4. Ajouter un utilisateur")
    print("5. Supprimer un utilisateur")
    print("6. Lister les utilisateurs")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Sauvegarder les données")
    print("10. Charger les données")
    print("0. Quitter")

def main():
    biblio = Bibliotheque()
    while True:
        menu()
        choix = input("Choisissez une option: ")
        if choix == '1':
            id = input("ID du livre: ")
            titre = input("Titre du livre: ")
            auteur = input("Auteur du livre: ")
            genre = input("Genre du livre: ")
            livre = Livre(id, titre, auteur, genre)
            biblio.ajouter_livre(livre)
        elif choix == '2':
            id = input("ID du livre à supprimer: ")
            biblio.supprimer_livre(id)
        elif choix == '3':
            livres = biblio.lister_livres()
            for livre in livres:
                print(f"{livre.id} - {livre.titre} par {livre.auteur} ({livre.genre}) - {'Disponible' if livre.disponible else 'Emprunté'}")
        elif choix == '4':
            id = input("ID de l'utilisateur: ")
            nom = input("Nom de l'utilisateur: ")
            email = input("Email de l'utilisateur: ")
            utilisateur = Utilisateur(id, nom, email)
            biblio.ajouter_utilisateur(utilisateur)
        elif choix == '5':
            id = input("ID de l'utilisateur à supprimer: ")
            biblio.supprimer_utilisateur(id)
        elif choix == '6':
            utilisateurs = biblio.lister_utilisateurs()
            for utilisateur in utilisateurs:
                print(f"{utilisateur.id} - {utilisateur.nom} ({utilisateur.email})")
        elif choix == '7':
            id_livre = input("ID du livre à emprunter: ")
            id_utilisateur = input("ID de l'utilisateur: ")
            if biblio.emprunter_livre(id_livre, id_utilisateur):
                print("Livre emprunté avec succès.")
            else:
                print("Livre non disponible.")
        elif choix == '8':
            id_livre = input("ID du livre à retourner: ")
            if biblio.retourner_livre(id_livre):
                print("Livre retourné avec succès.")
            else:
                print("Erreur lors du retour du livre.")
        elif choix == '9':
            biblio.sauvegarder_donnees()
            print("Données sauvegardées.")
        elif choix == '10':
            biblio.charger_donnees()
            print("Données chargées.")
        elif choix == '0':
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()


