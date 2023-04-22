# Real-Time-Audio-Effects
update pedalboard's AudioStream effects in realtime

### Setup
1. Install [pedalboard](https://github.com/spotify/pedalboard)
```
pip install pedalboard
```
2. Make sure you have at least one Audio Output working with your audio driver. For input, passing 
```allow_feedback = True``` into AudioStream allows no input to be required.
