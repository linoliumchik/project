class Triangle(object):

	b = 0
	cout = 0
	cashe = 0

	# def __init__(self):
	# 	b = int(input())

	def counter(self, arr):
		# if arr[0] == arr[1] or arr[0] == [2] or arr[1] == arr[2]:
		# 	self.cout +=1
		# elif arr[0] == arr[1] and == arr[2]:
		# 	self.cout +=2
		# else:
		# 	self.cout = 0
		self.cout = 0
		for i in range(len(arr)):
			print(self.cout)
			if i == 0:
				pass
			else:
				if arr[i] == arr[0] or (arr[i] == self.cashe and arr[i] != arr[0]):
					self.cout = self.cout + 1
			if i != 0:	
				self.cashe = arr[i]

	def raz(self):
		return "Разносторонний"
	def raw(self):
		return "Равносторонний"
	def rawb(self):
		return "Равнобедренный"

# blyat = Pizdos()
# blyat.counter()

# swich = {
# 	"1": blyat.rawb,
# 	"2": blyat.raw
# }

# print(swich.get(str(blyat.cout), blyat.raz)())

# if cout == 1:
# 	print("Равнобедренный")
# elif cout == 2:
# 	print("Равносторонний")
# else:
# 	print("Разносторонний")

# counter(b)




