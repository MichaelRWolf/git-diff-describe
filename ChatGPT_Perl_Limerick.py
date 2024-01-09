from gtts import gTTS
import IPython.display as ipd

# Limerick text
limerick = """
In a world of code both bold and neat,
ChatGPT and Perl had a feat,
To tidy up notes with flair,
In a way that seemed quite rare,
Making messy files obsolete and sweet!
"""

# Convert text to speech
tts = gTTS(limerick, lang="en", tld="co.uk")

# Save to a file
audio_file = "ChatGPT_Perl_Limerick.mp3"
tts.save(audio_file)

# Provide link to the audio file
audio_file

