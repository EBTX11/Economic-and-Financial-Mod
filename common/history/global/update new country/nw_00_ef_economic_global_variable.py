import os

# Chemin complet vers le fichier source
chemin_source = 'C:/Users/Compte principal/Documents/Paradox Interactive/Victoria 3/mod/Economic-and-Financial-Mod/common/history/global/00_ef_economic_global_variable.txt'

# Chemin complet vers le fichier de destination
chemin_destination = 'C:/Users/Compte principal/Documents/Paradox Interactive/Victoria 3/mod/Economic-and-Financial-Mod/common/scripted_effects/10_new_country_var.txt'

# Balises dans le fichier source
balise_debut_source = "#begin_copy"
balise_fin_source = "#end_copy"

# Balises dans le fichier de destination
balise_debut_destination = "#begin_past_economy_event"
balise_fin_destination = "#end_past_economy_event"

# Ouvrir le fichier source en mode lecture en utilisant le codec 'utf-8'
with open(chemin_source, 'r', encoding='utf-8') as source_file:
    # Lire le contenu du fichier source
    contenu_source = source_file.read()

    # Trouver les positions des balises de début et de fin dans le fichier source
    debut_index_source = contenu_source.find(balise_debut_source)
    fin_index_source = contenu_source.find(balise_fin_source)

    # Extraire le texte entre les balises dans le fichier source
    texte_a_conserver = contenu_source[debut_index_source + len(balise_debut_source):fin_index_source].strip()

    # Vérifier si le texte à conserver n'est pas vide
    if texte_a_conserver:
        # Lire le contenu actuel du fichier de destination
        with open(chemin_destination, 'r', encoding='utf-8') as destination_file:
            contenu_destination = destination_file.read()

        # Trouver les positions des balises de début et de fin dans le fichier de destination
        debut_index_destination = contenu_destination.find(balise_debut_destination)
        fin_index_destination = contenu_destination.find(balise_fin_destination)

        # Remplacer le contenu entre les balises dans le fichier de destination par celui du fichier source
        contenu_destination_modifie = contenu_destination[:debut_index_destination + len(balise_debut_destination)] + "\n" + texte_a_conserver + "\n" + contenu_destination[fin_index_destination:].lstrip()

        # Écrire le contenu modifié dans le fichier de destination
        with open(chemin_destination, 'w', encoding='utf-8') as destination_file:
            destination_file.write(contenu_destination_modifie)

        print(f"Contenu copié du fichier source ({chemin_source}) vers le fichier de destination ({chemin_destination}).")

print("Copie terminée avec succès.")
