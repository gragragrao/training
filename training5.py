# クラス


class Scout:
    def __init__(self, name, worker_type, skills, candidates):
        self.name = name
        self.worker_type = worker_type
        self.skills = skills
        candidates = [person for person in Person]

    def add_skill(self, skill):
        if a not in self.skills:
            self.skills.append(skill)
        return self.skills

    def add_candidate(self, person):




class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


# 問題 1

scout1 = Scout("Python Engineer", "Intern", ["Python", "Django"])

print(scout1.skills[0])
print(scout1.name)



# 問題 2

scout1.add_skill("Django")
print(scout1.skills)

scout1.add_skill("Flask")
print(scout1.skills)


# 問題 3

person1 = Person(name = "Shimada Hiroki", skills = ["Python", "Artificial Intelligence"])
person2 = Person(name = "Ito Shogo", skills = ["Ruby", "AWS"])

print(person1.name)
print(person2.skills)


# 問題 4
print(candidates)
