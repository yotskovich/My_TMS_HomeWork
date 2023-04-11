import random

class Mystery():

    def __init__(self, player_name, question, answer, choices):
        self.player_name = player_name
        self.question = question
        self.answer = answer
        self.choices = choices

    def quiz(self):
        print(f'Приветствуем тебя, {self.player_name}, удачи в игре!')
        print(f"И так вопрос:\n {self.question}")
        for index, el in enumerate(self.choices):
            print(f"\t{index}. {el}")

        try:
            choice_user = int(input("Ваш ответ:"))
        except ValueError:
            print("Ошибка: некорректный ввод")
        else:
            if self.choices[choice_user] == self.answer:
                print("Это правильный ответ!")
            else:
                print("К сожалению, это неправильно!")

dict_questions = {
    "В каком городе находится Тадж-Махал?": "Агра",
    "В каком городе находится Нотр-Дам де Пари?": "Париж",
    "Какой город является столицей Японии?": "Токио",
    "В каком городе находится Красная площадь?": "Москва",
    "Какой город является столицей Греции?": "Афины",
    "Какой город является столицей Испании?": "Мадрид",
    "В каком городе находится Таймс-сквер?": "Нью-Йорк",
    "Какой город является столицей Турции?": "Анкара",
    "В каком городе находится оперный театр Сиднея?": "Сидней",
    "Какой город является столицей Италии?": "Рим",
    "В каком городе находится Золотой мост?": "Янгон",
    "Какой город является столицей Австралии?": "Канберра",
    "В каком городе находится Колизей?": "Рим",
    "Какой город является столицей Южной Кореи?": "Сеул",
    "В каком городе находится Галерея Уффици?": "Флоренция",
    "В каком городе находится Базилика Сакре-Кёр?": "Париж",
    "В каком городе находится Версальский дворец?": "Версаль",
    "В каком городе находится Национальный музей Китая?": "Пекин",
    "В каком городе находится монастырь Корвинианум?": "Будапешт",
    "В каком городе находится Будда-бар?": "Париж",
    "В каком городе находится здание Главпочтамта?": "Москва",
    "В каком городе находится Мост Владивосток-Хасан?": "Владивосток",
    "В каком городе находится Статуя Христа-Искупителя?": "Рио-де-Жанейро",
    "В каком городе находится Айфелева башня?": "Париж",
    "В каком городе находится Бурдж-Халифа?": "Дубай",
    "В каком городе находится музей Эрмитаж?": "Санкт-Петербург",
    "В каком городе находится Гуггенхайм-музей?": "Нью-Йорк",
    "В каком городе находится Венецианский карнавал?": "Венеция",
    "В каком городе находится Монте-Карло?": "Монако",
    "В каком городе находится Тауэрский мост?": "Лондон",
    "В каком городе находится Башня телевидения?": "Берлин",
    "В каком городе находится Площадь Испании?": "Мадрид",
    "В каком городе находится Музей Лувр?": "Париж",
    "В каком городе находится Кампидоглио?": "Рим",
    "В каком городе находится Площадь Святого Петра?": "Ватикан",
    "В каком городе находится Колокол свободы?": "Филадельфия",
    "В каком городе находится Мост Миллениум?": "Лондон",
    "В каком городе находится Большой театр?": "Москва",
    "В каком городе находится Храм Ват Арун?": "Бангкок",
    "В каком городе находится Башня Остенде?": "Брюгге",
    "В каком городе находится Градчански театр?": "Скопье",
    "В каком городе находится Восточная Галерея?": "Лондон",
    "В каком городе находится Музей современного искусства?": "Сидней",
    "В каком городе находится Замок Гулливера?": "Киев",
    "В каком городе находится Дом книги?": "Санкт-Петербург",
    "В каком городе находится Башня Пиза?": "Пиза",
    "В каком городе находится Мост Торренте?": "Сараево",
    "В каком городе находится Главная почта?": "Мадрид",
    "В каком городе находится Швейцарский парламент?": "Берн",
    "В каком городе находится Белый дом?": "Вашингтон",
    "В каком городе находится Мост Траяна?": "Рим",
    "В каком городе находится Тауэр?": "Лондон",
}
cities = ['Женева', 'Никосия', 'Порт-о-Пренс', 'Шимла', 'Таллин', 'Шпейер', 'Киото', 'Каракас',
          'Хасавюрт', 'Мускат', 'Тирана', 'Могилев', 'Тбилиси', 'Харбин', 'Рабат', 'Нагпур', 'Мехико','Калуга',
          'Триполи', 'Тарту', 'Пекин', 'Салоники', 'Майами', 'Тунис', 'Владивосток', 'Лилль',
          'Калуга', 'Пардубице', 'Валенсия', 'Донецк', 'Тель-Авив', 'Мадрид', 'Гаага', 'Мерсин', 'Пушкино',
          'Алжир', 'Тула', 'Чебоксары', 'Шри-Джаяварденепура-Котте', 'Рига', 'Александрия', 'Дубай', 'Плоешти',
          'Калининград', 'Кабул', 'Будапешт', 'Смоленск', 'Галле', 'Бруссель', 'Тамбов', 'Манила', 'Мехико',
          'Генуя', 'Кингстон', 'Архангельск', 'Бухарест', 'Вильнюс', 'Буэнос-Айрес', 'Гамбург', 'Шымкент',
          'Калькутта', 'Тбилиси', 'Ош', 'Лас-Пальмас-де-Гран-Канария', 'Сиэтл', 'Краснодар', 'Ханты-Мансийск',
          'Ренн', 'Кудус', 'Дар-эс-Салам', 'Флоренция', 'Токио', 'Сен-Дени', 'Великий Новгород', 'Роттердам',
          'Нью-Йорк', 'Салерно', 'Анкара', 'Анадырь', 'Харьков', 'Вавилон', 'Куала-Лумпур', 'Джакарта',
          'Петрозаводск', 'Таганрог', 'Гельсингборг', 'Шри-Ланка','Минск', 'Кейптаун', 'Кишинев',
          'Хуэйхуэ', 'Гамбург', 'Милан', 'Душанбе', 'Форт-де-Франс','Гуанчжоу', 'Кабардино-Балкария',
          'Новый Орлеан']
list_questions = list(dict_questions.keys())
computer_choice = random.choice(list_questions)
list_questions.remove(computer_choice)
choice_for_player = random.choices(cities, k=3)
choice_for_player.insert(random.randint(1,4), dict_questions[computer_choice])

player_1 = Mystery('Elena Golovach', computer_choice, dict_questions[computer_choice], choice_for_player)
player_1.quiz()