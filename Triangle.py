class Triangle(object):

	b = 0
	cout = 0
	cashe = 0

	def __init__(self):
		b = int(input())

	def counter(self):
		for i in range(2):
			a = int(input())
			if a == self.b or (a == self.cashe and a != self.b):
				self.cout += 1
			self.cashe = a

	def raz(self):
		return "Разносторонний"
	def raw(self):
		return "Равносторонний"
	def rawb(self):
		return "Равнобедренный"

#blyat = Pizdos()
#blyat.counter()

#swich = {
#	"1": blyat.rawb,
#	"2": blyat.raw
#}

#print(swich.get(str(blyat.cout), blyat.raz)())

#if cout == 1:
#	print("Равнобедренный")
#elif cout == 2:
#	print("Равносторонний")
#else:
#	print("Разносторонний")

#counter(b)




