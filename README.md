# API ASR Fongbé

Cette API permet de transcrire un fichier audio (.wav) en langue Fongbé en texte, à l'aide du modèle pré-entraîné SpeechBrain.

## Fonctionnalités

- Transcription de fichiers audio `.wav` en texte Fongbé.
- Basé sur le modèle pré-entraîné `speechbrain/asr-wav2vec2-dvoice-fongbe`.
- Supporte les requêtes via HTTP POST.

## Prérequis

- Python 3.12 ou supérieur
- Les dépendances listées dans `requirements.txt`

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Martial2023/Fon-Trascription-API.git
   cd app
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Assurez-vous que le modèle pré-entraîné est téléchargé automatiquement dans le dossier `pretrained_models`.

## Utilisation

1. Lancez le serveur FastAPI :
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

2. Accédez à la documentation interactive Swagger :
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Exemple de requête avec `curl` :
   ```bash
   curl -X 'POST' 'http://127.0.0.1:8000/api/transcribe' \
        -F 'file=@mon_audio.wav'
   ```

## Hébergement sur Render.com

1. Créez un compte sur [Render.com](https://render.com/).

2. Ajoutez un nouveau service web :
   - Connectez votre dépôt GitHub contenant ce projet.
   - Configurez les paramètres :
     - **Build Command** : `pip install -r requirements.txt`
     - **Start Command** : `uvicorn app.main:app --host 0.0.0.0 --port 8000`
     - **Environment** : Python 3.8 ou supérieur.

3. Déployez le service.

4. Une fois déployé, l'API sera accessible via l'URL fournie par Render.com.

## Configuration CORS

L'API est configurée pour autoriser les origines suivantes :
- `http://localhost:3000`
- `https://16ee-41-85-162-123.ngrok-free.app`
- `https://gbe-ce.vercel.app/`

Vous pouvez modifier ces paramètres dans le fichier `main.py` si nécessaire.

## Structure du Projet

```
API_Docker/
├── app/
│   ├── main.py          # Fichier principal de l'API
│   ├── ...
├── requirements.txt     # Liste des dépendances
├── Dockerfile           # Fichier Docker pour le déploiement
└── README.md            # Documentation du projet
```

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour signaler des problèmes.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
