# olist_data_platform

Projet dbt configuré pour la production.

## 🚀 Démarrage rapide

1. Configurez votre fichier `profiles.yml` dans `~/.dbt/`
2. Installez les dépendances :
   ```bash
   dbt deps
   ```
3. Lancez le projet :
   ```bash
   dbt build
   ```

## 📂 Structure
- `models/staging/` : Nettoyage et typage (Vues).
- `models/intermediate/` : Logique métier transverse (Éphémère).
- `models/marts/` : Tables finales pour la BI (Tables/Incrémental).
