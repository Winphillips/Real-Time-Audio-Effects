from pedalboard import Pedalboard, Chorus, Compressor, Convolution, Gain, Reverb, Phaser, Delay, PitchShift
from pedalboard.io import AudioStream
import random
import time

# Set initial delay time
initial_delay_seconds = 0.5
initial_pitch_shift = 0.5

input_device_name = AudioStream.input_device_names[0]
output_device_name = AudioStream.output_device_names[0]
print(input_device_name, output_device_name)

with AudioStream(input_device_name, output_device_name, allow_feedback=True) as stream:
    # Set initial delay time
    seconds = initial_delay_seconds
    pitch = initial_pitch_shift
    # Create empty pedalboard
    pedalboard = Pedalboard()
    # Add plugins to the pedalboard
    pedalboard.append(Compressor(threshold_db=-50, ratio=25))
    pedalboard.append(Gain(gain_db=30))
    pedalboard.append(Chorus())
    pedalboard.append(Phaser())
    pedalboard.append(Convolution("./demo.wav", 1.0))
    pedalboard.append(Reverb(room_size=0.25))
    delay_plugin = Delay(delay_seconds=seconds)
    pedalboard.append(delay_plugin)
    pitch_plugin = PitchShift(semitones=pitch)
    pedalboard.append(pitch_plugin)
    
    # Set the pedalboard as plugins in the audio stream
    stream.plugins = pedalboard
    
    # Loop for updating delay time during audio playback
    while True:
        # Update delay time randomly
        seconds = random.uniform(0.1, 2.0)
        pitch = random.uniform(0.0, 24.0)
        # Update delay time in the delay plugin
        delay_plugin.delay_seconds = seconds
        pitch_plugin.semitones = pitch
        # Sleep for some time
        print(seconds, pitch, pedalboard)
        time.sleep(5.0)
