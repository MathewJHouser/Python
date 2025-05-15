import time

def get_class_instantiation_time(self):
    return self.class_instantiation_time

class CleanCodeGuard(type):
    classes_created = []

    def __new__(mcs, name, bases, dictionary):
        if 'get_class_instantiation_time' not in dictionary:
            dictionary['get_class_instantiation_time'] = get_class_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.class_instantiation_time = time.time()
        CleanCodeGuard.classes_created.append(name)
        time.sleep(1)
        return obj

class My_Class1(metaclass=CleanCodeGuard):
    pass

class My_Class2(metaclass=CleanCodeGuard):
    pass

my_object1 = My_Class1()
print(my_object1.get_class_instantiation_time())

my_object2 = My_Class2()
print(my_object2.get_class_instantiation_time())

print(CleanCodeGuard.classes_created)
