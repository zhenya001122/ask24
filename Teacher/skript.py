from learning_module import *


lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)
pety.take(lesson[3])

print(vasy.knowledge)

print(pety.knowledge)
pety.forget()
print(pety.knowledge)


