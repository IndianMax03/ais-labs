import owlready2 as ow
from Character import Character


class OntologyManager:

    def __init__(self):
        self.character = None
        self.onto = ow.get_ontology("main.owl")
        self.onto.load()
        ow.sync_reasoner()
        self.individuals = list(self.onto.individuals())
        self.object_properties = list(self.onto.object_properties())
        self.data_properties = list(self.onto.data_properties())
        self.valid_labels = {"Mage", "Pirate", "Assassin"}

    def print_all(self):
        for i in range(len(self.individuals)):
            print(f"{i + 1}) {self.individuals[i].name}")

    def find(self, character_name):
        return len(self.onto.search(iri=f"*{character_name}")) != 0

    def validate(self, character_name):
        flag = False

        for individual in self.individuals:
            if individual.name == character_name:
                flag = True
                break

        return flag

    def generate_character_info(self, character_name):
        individual = self.onto[character_name]
        spouse = None
        sex = None
        parents = []
        children = []
        labels = []

        for prop in self.data_properties:
            if sex is not None:
                break
            relations = list(prop.get_relations())
            for relation in relations:
                if relation[0].name == character_name:
                    sex = prop.name
                    break

        for prop in self.object_properties:
            relations = list(prop.get_relations())
            for relation in relations:
                if prop.name == "parent" and relation[0] == individual:
                    children.append(relation[1].name)
                if prop.name == "spouse" and spouse is None:
                    if relation[0] == individual:
                        spouse = relation[1].name
                    elif relation[1] == individual:
                        spouse = relation[0].name
                if prop.name == "childOf" and relation[0] == individual:
                    parents.append(relation[1].name)

        for individual_property in individual.is_a:
            if self.valid_labels.__contains__(individual_property.name):
                labels.append(individual_property.name)

        self.character = Character(character_name, sex, spouse, parents, children, labels)

    def print_character_info(self):
        self.character.print_character_info()
