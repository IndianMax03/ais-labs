from re import sub
from User import User
from OntologyManager import OntologyManager


class AI:
    emoji = "\U0001F916"
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    WHITE = '\33[37m'
    NAME_POSITION = 0
    SEX_POSITION = 1
    PLAY_HOURS_POSITION = 2
    CHARACTER_POSITION = 3

    def __init__(self):
        self.user = None
        self.ontology_manager = OntologyManager()

    def show_input_format(self):
        print(
            f"{self.OK}{self.emoji} Формат строки: Меня зовут <Имя>, я <мужчина/девушка>, я играю <n> часов, хочу узнать о <Имя_Персонажа>")

    def greet(self):
        print(
            f"{self.OK}{self.emoji} Привет! Я искусственный интеллект, который помогает начинающим игрокам в Assassin's creed =)")
        print(
            f"{self.OK}{self.emoji} Расскажи мне, как тебя зовут, твой пол, сколько часов ты наиграл(-а) и о каком персонаже хочешь узнать!")
        self.show_input_format()
        print(
            f"{self.OK}{self.emoji} Чтобы тебе было проще, я выведу список всех персонажей, о которых известно системе:")
        self.ontology_manager.print_all()

    def receive_data(self):
        input_line = input(f"{self.WHITE}> ")
        if not self.parse_input_line(input_line):
            self.receive_data()
        else:
            self.user_welcome()

    def continue_receive_data(self):
        print(f"{self.OK}{self.emoji} Рад, что ты остаешься со мной, {self.user.name}!")
        print(f"{self.OK}{self.emoji} Для продолжения работы просто введи мне имя персонажа!")
        self.user.character = input(f"{self.WHITE}> ").strip()

    def parse_input_line(self, input_line):
        separated_input = sub(' +', ' ', input_line.strip()).split(",")

        if len(separated_input) != 4:
            print(f"{self.WARNING}{self.emoji} Ох! Кажется, твоя строка не соответствует формату.. Попробуй еще раз!")
            return False
        else:
            sub_name = sub(' +', ' ', separated_input[self.NAME_POSITION].strip()).split(" ")
            if len(sub_name) != 3:
                print(
                    f"{self.WARNING}{self.emoji} Блин! Не могу понять, как тебя зовут.. Проверь, что твоя строка соответствует формату!")
                return False
            sub_sex = sub(' +', ' ', separated_input[self.SEX_POSITION].strip()).split(" ")
            if len(sub_sex) != 2:
                print(f"{self.WARNING}{self.emoji} Ешки-матрёшки! Не могу понять твой пол! Давай еще раз!")
                return False
            sub_play_hours = sub(' +', ' ', separated_input[self.PLAY_HOURS_POSITION].strip()).split(" ")
            if len(sub_play_hours) != 4:
                print(
                    f"{self.WARNING}{self.emoji} ОМГ! Не получается оценить твой скилл по количеству часов! Повтори, пожалуйста!")
                return False
            sub_character = sub(' +', ' ', separated_input[self.CHARACTER_POSITION].strip()).split(" ")
            if len(sub_character) != 4:
                print(f"{self.WARNING}{self.emoji} Прости! Не могу обнаружить имя персонажа... Напиши строку снова!")
                return False
            name = sub_name[2]
            sex = sub_sex[1]
            allowed_sex = ["мужчина", "девушка"]
            if not allowed_sex.__contains__(sex):
                print(f"{self.WARNING}{self.emoji} {name}, впервые слышу о таком поле! Выбери один из двух!")
                return False
            if not sub_play_hours[2].isdigit():
                print(
                    f"{self.WARNING}{self.emoji} Ой-ой-ой, {name}, кажется, количество сыгранных часов - не число! Попробуй снова!")
                return False
            play_hours = sub_play_hours[2]
            character = sub_character[3]
            self.user = User(name, sex, play_hours, character)
            return True

    def user_welcome(self):
        if self.user.sex:
            print(
                f"{self.OK}{self.emoji} Рад приветствовать, прекрасная {self.user.name}, {'ты уже так много играешь! Ассассинка-ветеран, получается!' if self.user.play_hours >= 40 else ' смотрю ты начинающая ассассинка! Не беспокойся, всё впереди!'}")
        else:
            print(
                f"{self.OK}{self.emoji} Моё почтение, смелый {self.user.name}, {'ты наверняка уже много повидал в опасном мире скрытных убийц!' if self.user.play_hours >= 40 else 'ты готов отправиться в очень опасное путешествие?'}")
        print(f"{self.OK}{self.emoji} Сейчас я расскажу тебе всё, что знаю о {self.user.character}")

    def give_info(self):
        if not self.ontology_manager.find(self.user.character):
            print(f"{self.WARNING}{self.emoji} Вот незадача! Персонажа с именем '{self.user.character}' не существует!")
            return False
        if not self.ontology_manager.validate(self.user.character):
            print(
                f"{self.FAIL}{self.emoji} Ах ты {'обманщица!' if self.user.sex else 'обманщик!'} '{self.user.character}' - не имя персонажа! Я не дам себя взломать!!!")
            return False

        self.ontology_manager.generate_character_info(self.user.character)
        self.ontology_manager.print_character_info()

        return True

    def ask_for_exit(self):
        print(f"{self.OK}{self.emoji} Хочешь выйти? д/н")
        ans = input(f"{self.WHITE}> ").strip()
        return ans == "д"

    def say_bye(self):
        print(f"{self.OK}{self.emoji} Прощай, {self.user.name}! Надеюсь, еще увидимся!")
