import requests


class ChuckNorrisJokes:
    def __init__(self, base_url):
        self.base_url = base_url
        self.list_joke_categories = self.get_list_joke_categories()

    # получение всех категорий
    def get_list_joke_categories(self):
        path_to_categories = "/categories"
        full_path_to_categories = self.base_url + path_to_categories
        return requests.get(full_path_to_categories).json()

    # убедиться, что данная категория есть в ответе запроса
    def check_category_in_list_joke_categories(self, entered_category):
        if entered_category in self.list_joke_categories:
            print(
                f"Шутка из категории \"{entered_category}\":\n"
                f"{self.get_joke_from_category(entered_category)}"
            )
        else:
            print(f"Категория \"{entered_category}\" не существует.")

    # получить шутку из категории
    def get_joke_from_category(self, entered_category):
        full_path_to_joke_from_category = self.base_url + "/random?category=" + entered_category
        result_response = requests.get(full_path_to_joke_from_category).json()
        joke_from_category = result_response["value"]
        return joke_from_category
