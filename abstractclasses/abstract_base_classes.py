__author__ = 'charles'

import abc


class AbstractBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self):
        pass


class ConcreteClass(AbstractBase):

    def __init__(self):
        self.things = []

    def do_something(self):
        print('concrete')

if __name__ == '__main__':
    #c1 = AbstractBase()
    c2 = ConcreteClass()
    c2.do_something()