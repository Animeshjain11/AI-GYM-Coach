from io import BytesIO
from gtts import gTTS


class TextToSpeech:
    def __init__(self):
        pass

    def speak(self, text, lang="en"):
        try:
            if not text:
                return None

            buffer = BytesIO()

            gTTS(
                text=str(text),
                lang=lang,
                slow=False
            ).write_to_fp(buffer)

            buffer.seek(0)

            return buffer.read()

        except Exception as e:
            print("TTS ERROR:", e)
            return None