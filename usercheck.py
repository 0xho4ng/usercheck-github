import requests
import re

def get_github_user_info(username):
    try:
        user_url = f'https://api.github.com/users/{username}?scope=email'
        response = requests.get(user_url)

        if response.status_code == 200:
            user_data = response.json()

            print(f"Nom d'utilisateur: {user_data['login']}")
            print(f"Nom complet: {user_data['name']}")
            print(f"Biographie: {user_data['bio']}")
            print(f"Société: {user_data.get('company', 'Non spécifiée')}")
            print(f"Image de profil: {user_data['avatar_url']}")
            print(f"Localisation: {user_data.get('location', 'Non spécifiée')}")
            print(f"Adresse e-mail: {user_data.get('email', 'Non spécifiée')}")
            print(f"Date de création du compte: {user_data['created_at']}")
            print(f"Nombre de followers: {user_data['followers']}")
            print(f"Nombre d'abonnements: {user_data['following']}")
            print(f"Nombre de repos: {user_data['public_repos']}")

            if user_data['public_repos'] > 0:
                
                show_repos = input("Voulez-vous voir les noms et descriptions des dépôts ? (Oui/Non): ")

                if show_repos.lower() == 'oui':
                    repos_url = f'https://api.github.com/users/{username}/repos'
                    repos_response = requests.get(repos_url)

                    if repos_response.status_code == 200:
                        repos_data = repos_response.json()

                        print("\nListe des dépôts:")
                        for repo in repos_data:
                            print(f"\nNom du dépôt: {repo['name']}")
                            print(f"Description: {repo['description'] or 'Aucune description disponible'}\n")
                    else:
                        print(f"Erreur lors de la récupération des dépôts : Code de réponse {repos_response.status_code}")
            else:
                print("L'utilisateur n'a aucun dépôt public.")

        else:
            print(f"Erreur : Code de réponse {response.status_code}")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")




def extract_github_username(github_url):
    try:
        match = re.search(r'https://github\.com/(\S+)', github_url)

        if match:
            return match.group(1)
        else:
            raise ValueError("Format de lien GitHub invalide")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'extraction du nom d'utilisateur : {e}")
        return None

# Demander à l'utilisateur son nom d'utilisateur GitHub
user_input = input("Entrez votre nom d'utilisateur GitHub : ")
github_url = f'https://github.com/{user_input}'

# Extraire le nom d'utilisateur à partir du lien
github_username = extract_github_username(github_url)

if github_username:
    get_github_user_info(github_username)
else:
    print("Impossible d'extraire le nom d'utilisateur du lien GitHub.")
