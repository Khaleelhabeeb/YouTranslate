from elevenlabs import clone, generate, set_api_key, save, Voices
from apiKey import API_KEY

""" Function for recording the translated audio track.  

    Arguments:
        transcript --> The transcript to be used for voice-over
        output_file --> Path to the output file
    
    No return type
"""
def voiceOver(transcript, output_file):
    set_api_key(API_KEY)

    print("Generating a Voice Over...")

    voice = clone(
        name="YouTuber",
        files=["audios/sample.mp3"],
        model='eleven_multilingual_v1'
    )


    audio = generate(text=transcript, voice=voice)

    save(audio, output_file)
    
    voices = Voices.from_api()
    voices.delete