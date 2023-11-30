# Projet OSINT Usercheck Github Compte

[![OSINT](https://img.shields.io/badge/OSINT-Training-blue)](https://ozint.eu) [![Python Version](https://img.shields.io/badge/Python-Latest%20Version-yellow)](https://www.python.org/downloads/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/lou-j/) [![License: MIT](https://img.shields.io/badge/License-MIT-magenta.svg)](license) [![GitHub stars](https://img.shields.io/github/stars/0xho4ng/usercheck-github.svg?style=social&label=Star&maxAge=2592000)](https://github.com/0xho4ng/usercheck-github/stargazers/)





Ce projet vise à créer un outil simple de vérification de présence d'un nom d'utilisateur sur les réseaux sociaux, en utilisant l'OSINT (Open Source Intelligence). Il utilise l'API GitHub pour récupérer des informations sur un utilisateur. C'était un projet crée pour un TP Open-Source.

![Image d'illustration](images/usercheck.png)
## Installation de l'environnement Python avec pyenv

1. **Installation de pyenv :**
   ```bash
   curl https://pyenv.run | bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv virtualenv-init -)"
   exec "$SHELL" 
   pyenv install 3.8.12
   pyenv local 3.8.12
   pip install -r requirements.txt ```

2. **Utilisation**
    Exécutez le script avec le nom d'utilisateur GitHub que vous voulez vérifier

   ``` bash 
   python usercheck.py https://github.com/utilisateur 
   python3 nomdufichier
   

![Image d'illustration](images/usercheck-demo.png)


3. Le programme affiche les informations sur l'utilisateur si le nom d'utilisateur est trouvé, sinon, il affiche un message indiquant que le nom d'utilisateur n'a pas été trouvé. 


4. **Update**

Demande à l'utisateur de rentrer son username de github pour avoir directement ses informations par rapport à son github.
![Image d'illustration](images/usercheck-enter-username.png)
![Image d'illustration](images/usercheck-enter-username-fonctionnement.png)
