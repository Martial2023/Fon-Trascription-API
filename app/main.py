from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from speechbrain.inference.ASR import EncoderASR
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API ASR Fongbé",
    description="Cette API permet de transcrire un fichier audio (.wav) en langue Fongbé en texte, à l'aide du modèle pré-entraîné SpeechBrain.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://16ee-41-85-162-123.ngrok-free.app",
        "https://gbe-ce.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Explicitly allow methods
    allow_headers=["*"],  # Allow all headers
)



# Chargement du modèle une fois au démarrage
asr_model = EncoderASR.from_hparams(
    source="speechbrain/asr-wav2vec2-dvoice-fongbe",
    savedir="pretrained_models/asr-wav2vec2-dvoice-fongbe"
)


@app.post("/api/transcribe", summary="Transcrire un fichier audio en Fongbé", tags=["ASR"])
async def transcribe_audio(audio: UploadFile = File(...)):
    """
    Transcrit un fichier .wav en texte Fongbé en utilisant le modèle speechbrain/asr-wav2vec2-dvoice-fongbe.

    - *file*: fichier audio au format .wav
    
    ### Exemple de requête avec curl :
    bash
    curl -X 'POST' 'http://127.0.0.1:8000/api/transcribe' \
        -F 'file=@mon_audio.wav' 
    
    """

    # if not audio.filename.endswith(".wav"):
    #     raise HTTPException(status_code=400, detail="Le fichier doit être au format .wav")

    # Sauvegarder temporairement le fichier
    temp_path = f"temp_{audio.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    try:
        # Transcription
        transcription = asr_model.transcribe_file(temp_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de transcription: {str(e)}")
    
    finally:
        # Nettoyer le fichier temporaire
        os.remove(temp_path)
        


    return JSONResponse(content={"transcription": transcription,
                                     "translation": "Les termes « traite négrière », « traite des nègres » et « traite des noirs » désignent le commerce d'esclaves noirs africains, phénomène historique qui concerne la déportation de dizaines de millions de victimes durant près de treize siècles."
                                     })