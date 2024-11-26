from chuck_norris_jokes import ChuckNorrisJokes


def run(start_test):
    # получить категорию от пользователя
    entered_category = input("Введите категорию, из которой хотите получить шутку\n>>> ")

    # убедиться, что данная категория существует
    # в ответе запроса и получить шутку из данной категории
    start_test.check_category_in_list_joke_categories(entered_category)


if __name__ == "__main__":
    base_url = "https://api.chucknorris.io/jokes"
    start_test = ChuckNorrisJokes(base_url)
    run(start_test)
