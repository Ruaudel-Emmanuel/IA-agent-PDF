# main.py
# Agent IA de génération de rapports PDF - Version Finale Robuste
# Date : 2025-10-18

import os
import sys
import json
import openai
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def main():
    """
    Fonction principale de l'agent de génération de rapport.
    """
    print("--- Initialisation de l'agent de génération de rapport ---")

    # --- Étape 1: Configuration des chemins et chargement des secrets ---
    try:
        # Définir le chemin absolu du répertoire du script AVANT TOUTE CHOSE
        # Cette méthode est la plus fiable.
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Plan B si __file__ n'est pas défini (par ex. dans certains terminaux interactifs)
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    print(f"Répertoire du projet détecté : {script_dir}")

    # Charger les variables d'environnement depuis le fichier .env situé dans ce répertoire
    dotenv_path = os.path.join(script_dir, '.env')
    if not os.path.exists(dotenv_path):
        print(f"ERREUR CRITIQUE : Le fichier .env est introuvable à l'emplacement : {dotenv_path}")
        print("Veuillez vous assurer que le fichier .env existe et se trouve à côté de main.py.")
        return
        
    load_dotenv(dotenv_path=dotenv_path)

    # Récupérer la clé API Perplexity et vérifier sa présence
    perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
    if not perplexity_api_key:
        raise ValueError("Clé API Perplexity (PERPLEXITY_API_KEY) non trouvée dans le fichier .env. Vérifiez le nom de la variable et le contenu du fichier.")

    print("Clé API Perplexity chargée.")

    # Créer un client compatible OpenAI mais pointant vers l'API Perplexity
    client = openai.OpenAI(
        api_key=perplexity_api_key,
        base_url="https://api.perplexity.ai"
    )

    # --- Étape 2: Configuration et chargement des fichiers ---
    env = Environment(loader=FileSystemLoader(script_dir))
    template = env.get_template("template.html")
    print("Template HTML chargé.")

    chemin_data_json = os.path.join(script_dir, 'data.json')
    with open(chemin_data_json, 'r', encoding='utf-8') as f:
        donnees_rapport = json.load(f)
    print("Fichier de données data.json chargé.")

    # --- Étape 3: Génération du contenu par l'IA ---
    print("\n--- Démarrage de la génération de contenu par l'IA ---")
    
    for i, section in enumerate(donnees_rapport['sections']):
        print(f"Génération de la section {i+1}/{len(donnees_rapport['sections'])}: '{section['titre_section']}'...")
        
        points_a_developper = "\n- ".join(section['points_cles'])
        prompt = (
            f"Tu es un expert rédacteur. En te basant sur les points clés suivants, rédige un texte détaillé et bien structuré "
            f"pour la section intitulée '{section['titre_section']}'. Adopte un ton professionnel et informatif.\n\n"
            f"Points clés à développer :\n- {points_a_developper}\n\n"
            f"Instruction spécifique pour cette section : {section['instructions_generation']}"
        )

        try:
            # Appel à l'API Perplexity avec le modèle Pro par défaut
            response = client.chat.completions.create(
                model="sonar-pro", # <-- Le modèle Pro par défaut, notre meilleure chance
                messages=[{"role": "user", "content": prompt}]
            )
            section['contenu_genere'] = response.choices[0].message.content
        except openai.APIError as e:
            print(f"ERREUR API : L'appel a échoué. Message : {e}")
            return
    
    print("\nContenu généré avec succès pour toutes les sections.")

    # --- Étape 4: Assemblage du rapport et génération du PDF ---
    print("\n--- Assemblage du rapport final et création du PDF ---")
    html_out = template.render(data=donnees_rapport)

    pdf_path = os.path.join(script_dir, 'rapport_ia_sante_2025.pdf')
    HTML(string=html_out, base_url=script_dir).write_pdf(pdf_path)
    
    print(f"\n🎉 Rapport PDF généré avec succès ! Retrouvez-le ici : {pdf_path}")

if __name__ == "__main__":
    main()
