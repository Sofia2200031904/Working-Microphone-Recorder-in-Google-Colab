from IPython.display import Audio, display, Javascript
from base64 import b64decode
import io
import numpy as np
import scipy.io.wavfile

# JavaScript to record audio from browser
def record(sec=5):
    display(Javascript("""
    const sleep = time => new Promise(resolve => setTimeout(resolve, time))
    const b2text = blob => new Promise(resolve => {
        const reader = new FileReader()
        reader.onloadend = () => resolve(reader.result)
        reader.readAsDataURL(blob)
    })

    async function record(sec) {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
        const recorder = new MediaRecorder(stream)
        const data = []

        recorder.ondataavailable = event => data.push(event.data)
        recorder.start()

        await sleep(sec * 1000)
        recorder.stop()

        await new Promise(resolve => recorder.onstop = resolve)
        const blob = new Blob(data)
        const b64data = await b2text(blob)
        google.colab.kernel.invokeFunction('notebook.save_audio', [b64data], {})
    }

    record(%d)
    """ % sec))

# Python function to receive the audio
def save_audio(data):
    header, b64 = data.split(',', 1)
    audio = b64decode(b64)
    with open('recorded.wav', 'wb') as f:
        f.write(audio)
    print("Saved audio to 'recorded.wav'")
    display(Audio('recorded.wav'))

# Register the function
from google.colab import output
output.register_callback('notebook.save_audio', save_audio)

# Record for 5 seconds
record(5)
