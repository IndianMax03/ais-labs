class Character:
    COLOR = '\033[35m'

    def __init__(self, name, sex, spouse, parents, children, labels):
        self.name = name
        self.sex = sex == "woman"
        self.spouse = spouse
        self.parents = parents
        self.children = children
        self.labels = labels

    def print_character_info(self):
        print(f"{self.COLOR}---> {self.name}")
        if self.sex:
            if len(self.labels) != 0:
                print(f"--> Великая убийца, перенявшая навыки: {self.labels} от своих предков!")
            else:
                print(f"--> Прекрасная женщина, способствовавшая развитию рода ассассинов!")
            if len(self.parents) != 0:
                print(f"--> Её родителями были: {self.parents}")
            else:
                print(f"--> О её родителях совсем ничего не известно..")
            if len(self.children) != 0:
                if (self.spouse is not None):
                    print(f"--> Вместе с {self.spouse} они родили: {self.children}")
                else:
                    print(f"--> Данные о её муже утеряны, но среди её детей: {self.children}")
            else:
                print(f"--> К несчастью, она оказалась бездетной!")
        else:
            if len(self.labels) != 0:
                print(f"--> Искусный боец, унаследовавший навыки: {self.labels}!")
            else:
                print(f"--> Совершенно обычный человек, ставший ассассином по исключительным обстоятельствам!")
            if len(self.parents) != 0:
                print(f"--> Его воспитали {self.parents}")
            else:
                print(f"--> Он вырос совсем один!")
            if self.spouse == None:
                print(f"--> Он был волком-одиночкой! Никакие женщины ему не понадобились!")
            else:
                print(f"--> Его супрогой стала {self.spouse}")
            if len(self.children) != 0:
                print(f"--> Сам же он стал отцом для: {self.children}")
            else:
                print(f"--> Продлить род ассассинов ему так и не удалось...")
