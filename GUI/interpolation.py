import time
class animation:
	def __init__(self,startTime,duration,startData,endData):
		self.startTime = startTime
		self.duration = duration
		self.startData = startData
		self.endData = endData
		self.factor = endData-startData
	def dataAtTime(self):
		timeSinceStart = ( time.time() - self.startTime)
		if timeSinceStart > self.duration:
			return self.endData
		mult = timeSinceStart/self.duration
		return self.startData + (self.factor*mult)
	def concluded(self):
		timeSinceStart = ( time.time() - self.startTime)
		if timeSinceStart > self.duration:
			return True
		else:
			return False
		
