import copy


class Virus:
    def __init__(self, name, virus_type, weight, age):
        self.name = name
        self.virus_type = virus_type
        self.weight = weight
        self.age = age
        self.children = []

    def add_child(self, child_virus):
        self.children.append(child_virus)

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    grandparent = Virus("Corona_Gen1", "RNA", 0.05, 10)

    parent1 = Virus("Corona_Gen2_A", "RNA", 0.04, 5)
    parent2 = Virus("Corona_Gen2_B", "RNA", 0.04, 4)
    grandparent.add_child(parent1)
    grandparent.add_child(parent2)

    child1 = Virus("Corona_Gen3_A1", "RNA", 0.03, 1)
    parent1.add_child(child1)

    cloned_grandparent = grandparent.clone()

    print("Original grandparent name:", grandparent.name)
    print("Cloned grandparent name:", cloned_grandparent.name)

    print("\nAre original and cloned grandparent the same object?:", grandparent is cloned_grandparent)
    print("Are their children arrays the same object?:", grandparent.children is cloned_grandparent.children)
    print("Are the first children identical objects?:", grandparent.children[0] is cloned_grandparent.children[0])