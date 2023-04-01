# 1) реализовать дескрипторы для любых двух классов





class Grade:
    def __init__(self, name):
        # Для данного подхода необходимо сформировать отдельное имя атрибута
        self.name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return "*{}*".format(getattr(instance, self.name))

    def __set__(self, instance, value):
        if not (1 <= value <= 100):
            raise ValueError("Балл ЕГЭ должен быть от 1 до 100")
        setattr(instance, self.name, value)

class Exam():
    ''' Комплексный экзамен, на котором оцениваются разные критерии. '''
    # Для обновленного Grade нужно добавить строковые имена
    math_grade = Grade('math_grade')
    writing_grade = Grade('writing_grade')
    science_grade = Grade('science')

math_exam = Exam()
math_exam.grade = 3
language_exam = Exam()
language_exam.grade = 5

print("  Проверим результаты: ")
print("Первый экзамен ", math_exam.grade, " — верно?")
print("Второй экзамен ", language_exam.grade, " — верно?")
print('Потому что... ')
print('math_exam.grade is language_exam.grade =', math_exam.grade is language_exam.grade)
