class Test():

    def __init__(self, name):
        self.name = name

    def decorator(method):
        def wrapper(self, *args, **kwargs):
            print(self.name)
            method(self, *args, **kwargs)

        return wrapper

    @decorator
    def method1(self):
        print("Instance name: {0}".format(self.name))


a = Test("Bob")
a.method1()
