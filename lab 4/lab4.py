#class Animal(object):
#	def __init__(self,sound,name,age,favorite_color):
#		self.sound = sound
#		self.name = name
#		self.age = age
#		self.favorite_color = favorite_color
#	def eat(self,food):
#		print("yummy!!"+ self.name + "is eating" +food)
#	def description(self):
#		print(self.name + "is " + self.age +" years old and loves the color" 
#			+ self.favorite_color)
#	def make_sound(self):
#		print(self.sound*3)
#dog = Animal ("barks","Lucky","2","red")
#dog.eat("pizza")
#dog.description()
#dog.make_sound()

class person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city= city
		self.gender = gender
	def eat(self,food):
		print("eating " + food)
	def sports(self,sports):
		print("Im playing " + sports + " yaaaaaay")
j = person ("Tamara", 15, "Jerusalem", "female")
j.eat("pizza")
j.sports("soccer")
