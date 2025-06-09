import faster_whisper



def whisper_transcript(audio_path):
    model = faster_whisper.WhisperModel('ivrit-ai/faster-whisper-v2-d4')
    segs, _ = model.transcribe(audio_path, language='he')

    texts = [s.text for s in segs]

    transcribed_text = ' '.join(texts)
    print(f'Transcribed text: {transcribed_text}')
    return transcribed_text