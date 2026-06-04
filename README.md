#  Notes Privées

Une application web moderne de prise de notes personnelles avec authentification utilisateur sécurisée.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

##  Fonctionnalités

- ✅ **Authentification sécurisée** - Inscription et connexion avec hashing Werkzeug
- ✅ **CRUD Complet** - Créer, lire, modifier, supprimer vos notes
- ✅ **Espace utilisateur personnel** - Gestion de compte et affichage des statistiques
- ✅ **Interface responsive** - Design moderne et adapté à tous les appareils
- ✅ **Isolation des données** - Chaque utilisateur voit uniquement ses notes
- ✅ **Protection des routes** - Décorateur `@login_required` pour les routes protégées

##  Stack Technologique

| Composant | Technologie |
|-----------|-------------|
| **Backend** | Python 3.8+ |
| **Framework Web** | Flask 2.3+ |
| **Base de données** | SQLite 3 |
| **Sécurité** | Werkzeug (hashing passwords) |
| **Frontend** | HTML5 + CSS3 + JavaScript |

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

```bash
# 1. Cloner le repository
git clone https://github.com/ChaibiP/App_Notes_privees.git
cd App_Notes_privees

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Initialiser la base de données (si nécessaire)
python db_init.py

# 4. Lancer l'application
python app.py
```

Accédez ensuite à **http://localhost:5000** dans votre navigateur.

## 🚀 Utilisation

### Inscription
1. Cliquez sur "Créer un compte"
2. Entrez un nom d'utilisateur unique
3. Créez un mot de passe fort
4. Confirmez votre inscription

### Gestion des notes
- **Créer** : Cliquez sur "Nouvelle note" et remplissez le formulaire
- **Consulter** : Cliquez sur une note dans la liste pour la voir en détail
- **Modifier** : Ouvrez une note et cliquez sur "Éditer"
- **Supprimer** : Ouvrez une note et cliquez sur "Supprimer"

### Gestion du compte
- Accédez à votre profil via "Mon Compte"
- Changez votre nom d'utilisateur si nécessaire

## Architecture du projet

```
App_Notes_privees/
├── app.py                 # Routes principales et logique applicative
├── db.py                  # Fonctions d'accès à la base de données
├── db_init.py            # Initialisation de la base de données
├── requirements.txt       # Dépendances Python
├── templates/            # Fichiers HTML (Jinja2)
│   ├── index.html        # Page d'accueil
│   ├── login.html        # Connexion
│   ├── register.html     # Inscription
│   ├── addnote.html      # Créer une note
│   ├── note.html         # Afficher une note
│   ├── update.html       # Modifier une note
│   ├── myaccount.html    # Profil utilisateur
│   └── updateaccount.html # Modifier le profil
├── static/
│   └── css/
│       ├── style.css     # Feuille de styles principale
│       └── images/       # Images et backgrounds
│           ├── background.png
│           └── background2.png
└── notes.db              # Base de données SQLite (généré automatiquement)
```

## Sécurité

L'application implémente plusieurs mesures de sécurité :

- **Hashing des mots de passe** - Utilisation de Werkzeug `generate_password_hash()` et `check_password_hash()`
- **Sessions sécurisées** - Gestion des sessions avec Flask
- **Authentification obligatoire** - Décorateur `@login_required` sur les routes sensibles
- **Vérification de propriété** - Les utilisateurs ne peuvent modifier/supprimer que leurs propres notes
- **Paramètres liés** - Utilisation de requêtes SQL paramétrées pour prévenir les injections SQL

## 🎓 Points d'apprentissage

Ce projet m'a permis de maîtriser :

- ✨ **Framework Flask** - Création d'une application web full-stack
- ✨ **Authentification** - Gestion sécurisée des utilisateurs et sessions
- ✨ **Base de données** - Conception SQLite et requêtes SQL
- ✨ **Architecture MVC** - Séparation des routes, données et templates
- ✨ **Responsive Design** - Interface adaptable à tous les écrans
- ✨ **Gestion des sessions** - Maintien d'état utilisateur
- ✨ **Sécurité web** - Hashing, validation de propriété, protection des routes

## 📋 Fonctionnalités futures

- [ ] Recherche et filtrage avancés des notes
- [ ] Catégories et tags pour les notes
- [ ] Partage de notes (en lecture seule)
- [ ] Exportation des notes (PDF, JSON)
- [ ] Thème sombre/clair
- [ ] Authentification à deux facteurs (2FA)

## 🤝 Contribution

Les suggestions et améliorations sont bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](./LICENSE) pour plus de détails.

## 👤 Auteur

**Chaibi P.**  
[GitHub](https://github.com/ChaibiP) | [Profil](https://github.com/ChaibiP)

---

**Dernier update** : Juin 2026  
**Status** : En développement actif ✨
