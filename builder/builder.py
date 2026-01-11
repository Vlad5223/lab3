class Product:
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass
    @abstractmethod
    def build_part_b(self):
        pass
    @abstractmethod
    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()
    def build_part_a(self):
        self.product.add("PartA")
    def build_part_b(self):
        self.product.add("PartB")
    def get_result(self):
        return self.product

class Director:
    def construct(self, builder: Builder):
        builder.build_part_a()
        builder.build_part_b()

builder = ConcreteBuilder()
director = Director()
director.construct(builder)
product = builder.get_result()
print(product.list_parts())