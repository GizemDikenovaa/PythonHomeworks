class Person:
    def __init__(self, name, surname, age, country, city, talent):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city
        self.talent = talent

    def personal_info(self):
        return "Name: {} \nSurname:{} \nAge:{} \nCountry: {} \nCity: {} \nTalent:{}"\
            .format(self.name, self.surname, self.age, self.country, self.city, self.talent)

    def talent_add(self, enter_talent):
        self.talent.append(enter_talent)


p1 = Person("Gizem", "Dikenova", 25, "Turkey", "Istanbul", "QA Tester")
print(p1.personal_info())
p1.talent_add(input('Enter the talent: '))
print(p1.personal_info())
