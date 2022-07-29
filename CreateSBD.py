class CreateSBD(object):
	"""docstring for CreateSBD"""
	def __init__(self,idTinh,number):
		super(CreateSBD, self).__init__()
		self.idTinh = idTinh
		self.number = number
		
	def numberOfnumber(self,number):
		count = 0
		while (number>0):
			count += 1
			number //= 10
		return count

	def create(self):
		SBD = ""
		count = self.numberOfnumber(self.idTinh)
		SBD += (2-count)*"0"+str(self.idTinh)
		count = self.numberOfnumber(self.number)
		SBD += (6-count)*"0"+str(self.number)
		return SBD


