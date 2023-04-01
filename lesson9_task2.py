# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
# Первый способ сохранить данные — просто в атрибуте объекта дескриптора.
class DocMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class MyClass(metaclass = DocMeta):
    pass
obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)