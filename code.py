from adafruit_circuitplayground.express import cpx
import time
import audiocore
import board

cpx.pixels.brightness = 0.5

class MusicPlayer:
    def __init__(self, cpx):
        self.cpx = cpx
        self.audio = None
        self.wavefile = None

    def start_file(self, file_name: str):
        self.cpx.stop_tone()
        self.cpx._speaker_enable.value = True
        self.audio = self.cpx._audio_out(board.SPEAKER)
        self.wavefile = audiocore.WaveFile(open(file_name, "rb"))
        self.audio.play(self.wavefile)

    def stop_file(self):
        self.cpx._speaker_enable.value = False
        self.audio.deinit()
        self.wavefile.deinit()

music = MusicPlayer(cpx)

def lights_countdown():
    if cpx.light < 10:
        # starts playing the audio
        music.start_file("Cantina(20).wav")
        # light the pixels one by one
        for i in range(10):
            cpx.pixels[i] = 0, 0, 255
            time.sleep(2)
        # wait until the audio has finished playing
        while music.audio.playing:
            time.sleep(0.05)
        # deinit the audio setup
        music.stop_file()
        # turn the pixels off
        cpx.pixels.fill((0, 0, 0))

while True:
    lights_countdown()
