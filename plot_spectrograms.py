import scipy
import os
from pydub import AudioSegment
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy.io import wavfile
from tempfile import mktemp


def get_wav_path(mp3_name: str) -> str:
    mp3_path = f"data/MP3/{mp3_name}"
    wav_path = f"data/WAV/{mp3_name[:-4]}.wav"
    if os.path.exists(wav_path):
        os.remove(wav_path)
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    return wav_path


def plot_spectrogram(mp3_name: str, title: str) -> None:
    wav_path = get_wav_path(mp3_name)
    FS, data = wavfile.read(wav_path)  # read wav file
    plt.figure()
    plt.specgram(data, Fs=FS, cmap="inferno")  # plot
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title(title)
    plt.colorbar()
    plt.savefig(f"figures/{title}.png")


plot_spectrogram(mp3_name="serverMicCalibration.mp3", title="Mic Calibration")
plot_spectrogram(mp3_name="ServerTransient0(gain).mp3", title="Startup (0 deg)")
plot_spectrogram(mp3_name="ServerTransient60.mp3", title="Startup (60 deg)")
plot_spectrogram(mp3_name="ServerTransient120.mp3", title="Startup (120 deg)")
plot_spectrogram(mp3_name="ServerTransient180.mp3", title="Startup (180 deg)")
plot_spectrogram(mp3_name="ServerTransient240.mp3", title="Startup (240 deg)")
plot_spectrogram(mp3_name="ServerTransient300.mp3", title="Startup (300 deg)")
plot_spectrogram(mp3_name="ServerTransientAbove.mp3", title="Startup (above)")