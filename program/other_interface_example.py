from dz9.program.app import UrlShortener

domain = '.hello.ua'
storage_name = 'my_storage'
shortener = UrlShortener(domain=domain, storage_name=storage_name)

question_string = 'Чого бажаєте?' \
                  '\n1. Записати нове посилання' \
                  '\n2. Відобразити всі посилання'


def interface():
    print(question_string)
    ui = input(">> ")
    if ui == "1":
        shortener.add_link()
    elif ui == '2':
        for link in shortener.links:
            print(link)
