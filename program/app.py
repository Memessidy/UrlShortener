import shelve


class UrlShortener:
    def __init__(self, domain, storage_name):
        self.domain = domain
        self.__break_word = 'off'
        self.storage = storage_name
        self.__links = []

    @property
    def links(self):
        if not self.__links:
            self.__all_links()
        return self.__links

    def __get_correct_link(self, link):
        if link.lower() == self.__break_word:
            return False
        while len(link.split('.')) < 2:
            print("Введіть будь ласка адресу сайту! Повинна бути крапка в посиланні!")
            link = input("Введіть посилання: ")
            if link.lower() == self.__break_word:
                return False
        return link

    def __write_data(self, full_name, shortname):
        with shelve.open(self.storage) as names:
            names[shortname] = full_name
        self.__links.clear()
        self.__all_links()

    def __get_shortname(self):
        shortname = input("Введіть скорочену назву для цього посилання: ")
        if shortname.lower() == self.__break_word:
            return False
        return shortname

    def add_link(self):
        link = shortname = False
        print(f"Щоб завершити, просто введіть: {self.__break_word}")
        print('Введіть посилання: ')
        link = input(">> ")
        link = self.__get_correct_link(link)
        if link:
            shortname = self.__get_shortname()
            if shortname:
                shortname += self.domain
                self.__write_data(full_name=link, shortname=shortname)
        if all([link, shortname]):
            return True
        else:
            return False

    def __all_links(self):
        with shelve.open(filename=self.storage) as file:
            for element in file.items():
                self.__links.append(f"Назва: {element[0]}; Посилання: {element[1]}")

    def get_link_by_shortname(self, shortname):
        if not shortname.endswith(self.domain):
            shortname += self.domain
        with shelve.open(filename=self.storage) as file:
            website_link = file.get(shortname, None)
        return website_link
