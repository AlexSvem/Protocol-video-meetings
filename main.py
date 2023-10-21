from pydub import AudioSegment
from vosk import KaldiRecognizer, Model, SetLogLevel
import os
import json
import subprocess

SetLogLevel(0)

if not os.path.exists("model"):
    print("Please download")


