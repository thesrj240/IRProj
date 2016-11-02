class remdup:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __eq__(self,other):
		return self.a==other.a and self.b==other.b
	def __hash__(self):
		return hash(('a',self.a,'b',self.b))	

A = remdup(1,0)
B = remdup(1,0)
X = [A,B]
X = list(set(X))
print(A.__hash__())
print(len(X))
if A==B:
	print(1)

