class User:

    def __init__(self, name, sex, play_hours, character):
        self.name = name
        self.sex = True if sex == "девушка" else False
        self.play_hours = int(play_hours)
        self.character = character