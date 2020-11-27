import os
import re


class Search:

    def __init__(self, path):
        # Дерриктория с котрой начинается поиск
        self.path = path
        # Тип искомого файла

    def pdf_remove(self):
        pattern = '.*.pdf'
        tree = os.walk(self.path)
        for couple in tree:
            for file_name in couple[2]:
                if re.search(f'{pattern}', file_name) is not None:
                    try:
                        os.replace(
                            f'{couple[0]}/{file_name}',
                            f'{self.path}/PDF/{file_name}'
                        )
                    except FileNotFoundError:
                        os.makedirs(f'{self.path}/PDF/')
                        os.replace(
                            f'{couple[0]}/{file_name}',
                            f'{self.path}/PDF/{file_name}'
                        )


test1 = Search('C:/Users/Михаил/Downloads')
test1.pdf_remove()
