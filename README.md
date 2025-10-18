🤖 Agent IA de Génération de Rapports PDF
Ce projet est un agent intelligent en Python qui automatise la création de rapports PDF professionnels à partir de données structurées au format JSON. L'agent utilise un modèle de langage avancé pour générer le contenu textuel et applique une identité visuelle personnalisée via des templates HTML/CSS.

✨ Fonctionnalités
Conversion JSON vers PDF : Transforme des données brutes en un rapport PDF élégant.

Génération de Contenu par IA : Utilise un grand modèle de langage pour rédiger des paragraphes pertinents et bien écrits à partir de points clés.

Branding Personnalisable : Applique facilement une identité visuelle (couleurs, polices, logo) via une feuille de style CSS.

Moteur de Template Robuste : Utilise des templates HTML pour une mise en page flexible et facile à maintenir.

🚀 Démarrage Rapide
Pour lancer le projet sur votre machine, suivez ces étapes.

1. Prérequis
Assurez-vous d'avoir Python 3.9 ou une version plus récente installée.

Ce projet utilise WeasyPrint, qui a des dépendances système. Sous Windows, vous devez installer GTK+.

Suivez le guide d'installation de MSYS2 pour installer GTK3.

N'oubliez pas d'ajouter le dossier bin de votre installation GTK au PATH de votre système.

2. Installation
Clonez le dépôt

bash
git clone https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_NOM_PROJET.git
cd VOTRE_NOM_PROJET
Installez les dépendances Python
Toutes les bibliothèques nécessaires sont listées dans requirements.txt.

bash
pip install -r requirements.txt
3. Configuration
Créez un fichier .env
À la racine du projet, créez un fichier nommé .env.

Ajoutez votre clé d'API
Ouvrez le fichier .env et ajoutez votre clé d'API de modèle de langage. Le script est configuré pour lire la variable suivante :

text
PERPLEXITY_API_KEY="votre_cle_api_ici"
4. Lancement de l'agent
Une fois l'installation et la configuration terminées, lancez le script principal :

bash
python main.py
Le script s'exécutera et générera le rapport rapport_ia_sante_2025.pdf dans le même dossier.

🛠️ Technologies Utilisées
Ce projet a été construit avec les outils suivants :

Technologie	Rôle
Python	Langage principal du projet
OpenAI SDK	Client pour interagir avec l'API du modèle de langage
Jinja2	Moteur de template pour générer le HTML
WeasyPrint	Bibliothèque de conversion HTML/CSS vers PDF
Dotenv	Gestion des variables d'environnement (clés API)
