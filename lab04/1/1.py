import time


class Ticket:

    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket:", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print("     createDate: ", time.asctime(self.createDate))
        print("     owner: ", self.owner)
        print("     deadline:", time.asctime(self.deadline))


# создание объекта класса

ticket1 = Ticket(time.localtime(), "Ivan Ivanov",
time.strptime("28.02.2021", "%d.%m.%Y"))

# вызов метода

ticket1.display()

#получение значения атрибута

print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))

# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))

# установка значения атрибута
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)

# удаление значения атрибута
delattr(ticket1, "owner")
if hasattr(ticket1, "owner"):
    print("delattr: ", ticket1.owner)

# удаление объекта
#del ticket1
#print(ticket1)

# удаленый объект нельзя вывести

t = time.localtime()
print("Current time:", time.asctime(t))