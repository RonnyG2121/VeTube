import logging
from functools import partial
from pathlib import Path
from sound_lib import stream
from sound_lib import output
from . import Piper
o = output.Output()

class piperSpeak:
	def __init__(self, model_path):
		self.model_path = model_path
		self.speaker_id = None
		self.length_scale = 1
		self.noise_scale = 0.667
		self.noise_w = 0.8
		self.synthesize = None
		self.voice = None
		self.audio_stream=None

	def load_model(self):
		if self.voice:
			return self.voice
		self.voice = Piper(self.model_path)
		self.audio_stream=stream.PushStream(freq=self.voice.config.sample_rate, chans=1)

	def set_rate(self, new_scale):
		self.length_scale = new_scale

	def set_speaker(self, sid):
		self.speaker_id = sid

	def is_multispeaker(self):
		return self.voice.config.num_speakers > 1

	def list_speakers(self):
		if self.is_multispeaker():
			return self.voice.config.speaker_id_map
		else:
			raise Exception("This is not a multispeaker model!")

	def speak(self, text):
		self.synthesize = self.load_model()
		if self.speaker_id is None and self.is_multispeaker():
			self.set_speaker(0)
		audio_norm, sample_rate = self.voice.synthesize(
			text,
			self.speaker_id,
			self.length_scale,
			self.noise_scale,
			self.noise_w
		)
		self.audio_stream.stop()
		self.audio_stream.push(audio_norm)
		self.audio_stream.play()