import math
class pos:
	def __init__(self,*args):
		self.points = []
		#self.x = None
		#self.y = None
		if len(args) == 1 and hasattr(args[0], '__iter__'):
			for item in args[0]:
				self.points.append(item)
		else:
			for arg in args:
				self.points.append(arg)
	def __add__(self, L):
		Points_for_new = []
		for index,point in enumerate(self.points):
			Points_for_new.append( point + L.points[index] )
		return pos(Points_for_new)
	def __sub__(self, L):
		Points_for_new = []
		for index,point in enumerate(self.points):
			Points_for_new.append( point - L.points[index] )
		return pos(Points_for_new)
	def __mul__(self, L):
		Points_for_new = []
		for index,point in enumerate(self.points):
			Points_for_new.append( point * L )
		return pos(Points_for_new)
	def __truediv__(self,L):
		Points_for_new = []
		for index,point in enumerate(self.points):
			Points_for_new.append( point / L )
		return pos(Points_for_new)
		
	@property
	def x(self): return self.points[0]
	@property
	def y(self): return self.points[1]
	@x.setter
	def x(self,val): self.points[0] = val
	@y.setter
	def y(self,val): self.points[1] = val
		
	def AsTuple(self):
		return (self.x,self.y)
	def OnCircle(ang):
		return pos(math.cos(ang),math.sin(ang))
