from re import sub
from User import User


class AI:
    emoji = "\U0001F916"
    NAME_POSITION = 0
    SEX_POSITION = 1
    PLAY_HOURS_POSITION = 2
    CHARACTER_POSITION = 3

    def __init__(self):
        self.user = None

    def showInputFormat(self):
        print(
            f"{self.emoji} Формат строки: Меня зовут <Имя>, я <мужчина/девушка>, я играю <n> часов, хочу узнать о <Имя_Персонажа>")

    def greet(self):
        print(
            f"{self.emoji} Привет! Я искусственный интеллект, который помогает начинающим игрокам в Assassin's creed =)")
        print(
            f"{self.emoji} Расскажи мне, как тебя зовут, твой пол, сколько часов ты наиграл(-а) и о каком персонаже хочешь узнать!")
        self.showInputFormat()

    def receive_data(self):
        input_line = input("> ")
        if (not self.parse_input_line(input_line)):
            self.receive_data()
        else:
            self.user_welcome()


    def parse_input_line(self, input_line):
        separated_input = sub(' +', ' ', input_line.strip()).split(",")

        if len(separated_input) != 4:
            print(f"{self.emoji} Ох! Кажется, твоя строка не соответствует формату.. Попробуй еще раз!")
            return False
        else:
            sub_name = sub(' +', ' ', separated_input[self.NAME_POSITION].strip()).split(" ")
            if len(sub_name) != 3:
                print(
                    f"{self.emoji} Блин! Не могу понять, как тебя зовут.. Проверь, что твоя строка соответствует формату!")
                return False
            sub_sex = sub(' +', ' ', separated_input[self.SEX_POSITION].strip()).split(" ")
            if len(sub_sex) != 2:
                print(f"{self.emoji} Ешки-матрёшки! Не могу понять твой пол! Давай еще раз!")
                return False
            sub_play_hours = sub(' +', ' ', separated_input[self.PLAY_HOURS_POSITION].strip()).split(" ")
            if len(sub_play_hours) != 4:
                print(f"{self.emoji} ОМГ! Не получается оценить твой скилл по количеству часов! Повтори, пожалуйста!")
                return False
            sub_character = sub(' +', ' ', separated_input[self.CHARACTER_POSITION].strip()).split(" ")
            if len(sub_character) != 4:
                print(f"{self.emoji} Прости! Не могу обнаружить имя персонажа... Напиши строку снова!")
                return False
            name = sub_name[2]
            sex = sub_sex[1]
            allowed_sex = ["мужчина", "девушка"]
            if not allowed_sex.__contains__(sex):
                print(f"{self.emoji} {name}, впервые слышу о таком поле! Выбери один из двух!")
                return False
            if not sub_play_hours[2].isdigit():
                print(f"{self.emoji} Ой-ой-ой, {name}, кажется, количество сыгранных часов - не число! Попробуй снова!")
                return False
            play_hours = sub_play_hours[2]
            character = sub_character[3]
            self.user = User(name, sex, play_hours, character)
            return True

    def user_welcome(self):
        if (self.user.sex):
            print(f"{self.emoji} Рад приветствовать, прекрасная {self.user.name}, {'ты уже так много играешь! Ассассинка-ветеран, получается!' if self.user.play_hours >= 40 else ' смотрю ты начинающая ассассинка! Не беспокойся, всё впереди!'}")
        else:
            print(
                f"{self.emoji} Моё почтение, смелый {self.user.name}, {'ты наверняка уже много повидал в опасном мире скрытных убийц!' if self.user.play_hours >= 40 else 'ты готов отправиться в очень опасное путешествие?'}")
        print(f"{self.emoji} Сейчас я расскажу тебе всё, что знаю о {self.user.character}")