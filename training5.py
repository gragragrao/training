# クラス


class Scout:
    def __init__(self, name, worker_type, skills):
        self.name = name
        self.worker_type = worker_type
        self.skills = skills
        self.candidates = []


    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
        return self.skills


    def add_candidate(self, person):
        return self.candidates.append(person)

    def get_candidate_name_list(self):
        return [person.name for person in self.candidates]

    def search_candidate_or(self):
        candidates_or = []
        for person in self.candidates:
            for skill in person.skills:
                if skill in self.skills:
                    candidates_or.append(person)
        return list(set([person.name for person in candidates_or]))

    def search_candidate_and(self):
        candidates_and = []
        for person in self.candidates:
            if set(self.skills + person.skills) == set(person.skills):
                candidates_and.append(person)
        return [person.name for person in candidates_and]


'''
合格！！
'''





class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


# 問題 1

scout1 = Scout("Python Engineer", "Intern", ["Python", "Django"])

print(scout1.skills[0])
# >>> Python

print(scout1.name)
# >>> Python Engineer



# 問題 2

scout1.add_skill("Django")
print(scout1.skills)
# >>> ['Python', 'Django']

scout1.add_skill("Flask")
print(scout1.skills)
# >>> Shimada Hiroki


# 問題 3

person1 = Person(name = "Shimada Hiroki", skills = ["Python", "Artificial Intelligence"])
person2 = Person(name = "Ito Shogo", skills = ["Ruby", "AWS"])
person3 = Person(name = "SuperMan", skills = ["Ruby", "AWS", "Python", "Django", "Flask"])

print(person1.name)
# >>> Shimada Hiroki

print(person2.skills)
# >>> ['Ruby', 'AWS']


# 問題 4

scout1.add_candidate(person1)
scout1.add_candidate(person2)
scout1.add_candidate(person3)

print(scout1.candidates[0].name)
# >>> Shimada Hiroki

# 問題 5

print(scout1.get_candidate_name_list())

# 問題 6

print(scout1.search_candidate_or())

# 問題 7

print(scout1.search_candidate_and())




####
