from dz9.program.app import UrlShortener
from dz9.program.user_choice import get_user_choice

domain = '.hello.ua'
storage_name = 'my_storage'
shortener = UrlShortener(domain=domain, storage_name=storage_name)

question_string = 'Чого бажаєте?' \
                  '\n1. Записати нове посилання' \
                  '\n2. Вивести на екран список посилань' \
                  '\n3. Знайти посилання за скороченою назвою' \
                  '\n4. Вийти'


def interface():
    while True:
        print(question_string)
        user_input = get_user_choice(question_string, parse_string=True)

        match user_input:
            case "1":
                added = shortener.add_link()
                if added:
                    print("Записано")
            case "2":
                if not shortener.links:
                    print("Ще не записане не одне посилання")
                else:
                    print("Всі посилання: ")
                    for link in shortener.links:
                        print(link)
                print()
            case "3":
                shortname = input('Введіть скорочену назву(shortname): ')
                link = shortener.get_link_by_shortname(shortname)
                if link:
                    print(f"Повне посилання: {link}")
                else:
                    print("Посилання за такою назвою не знайдено")
            case "4":
                print("До побачення")
                return


if __name__ == '__main__':
    interface()
