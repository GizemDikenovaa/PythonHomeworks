class student:
    def __init__(self, name, surname, classroom):
        self.name = name
        self.surname = surname
        self.classroom = classroom

    def show_info(self):
        print("""Name: {} \nSurname: {} \nClassroom: {}""".format(self.name, self.surname, self.classroom))


class question:
    def __init__(self, true, false):
        self.true = true
        self.false = false

    def net_n(self):
        if self.false >= 4:
            false_d = self.false // 4
            net_true = self.true - false_d
            return net_true

        else:
            return self.true

    def calculate(self, net_true):
        net = net_true * 2
        print("Toplam puan:  {} ".format(net))

s1 = student("Gizem", "Dikenova", "50")
s1.show_info()
exam = question(64, 11)
net_number = exam.net_n()
print("Net number: {}".format(net_number))
exam.calculate(net_number)