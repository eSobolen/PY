class Worker:
    '''doc class Worker'''
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)


class Animal:
    '''doc class Animal'''
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1
        self.id = Animal.count

    def display(self):
        print("Animal:")
        print("Name: {} ID: {} Age: {}".format(self.name, self.id, self.age))


lynx = Animal('Harry', 2)
dog = Animal('Sharky', 3)
cat = Animal('Molly', 10)

lynx.display()
dog.display()
cat.display()