from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return "ProductA1"
    def create_product_b(self):
        return "ProductB1"

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return "ProductA2"
    def create_product_b(self):
        return "ProductB2"

factory = ConcreteFactory1()
print(factory.create_product_a())
print(factory.create_product_b())