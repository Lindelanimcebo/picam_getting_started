from picamera import PiCamera
from time import sleep

class picam_iot:
	
	def __init__(self, img_dir, vid_dir):
		self.camera = PiCamera()
		self.img_dir = img_dir
		self.vid_dir = vid_dir
	
	def capture(self, name):
		self.camera.start_preview()
		sleep(5)
		self.camera.capture(self.img_dir+name)
		self.camera.stop_preview()
		
	def take_vid(self, name):
		self.camera.start_preview()
		self.camera.start_recording(self.vid_dir+name)
		sleep(5)
		self.camera.stop_recording()
		self.camera.stop_preview()
