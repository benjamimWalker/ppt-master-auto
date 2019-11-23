import wikipedia
from google_images_download import google_images_download


class Resources:

    def __init__(self, assunto):
        self.assunto = assunto

    @classmethod
    def add_breakline(cls, text):

        lista = text.split('.')

        while ' ' in lista:
            lista.remove(' ')

        while '' in lista:
            lista.remove('')

        return lista

    def get_images(self, limit):
        response = google_images_download.googleimagesdownload()

        arguments = {
            "keywords": self.assunto,
            "limit": limit,
            'format': 'jpg',
            'output_directory': 'Images/',
            '–safe_search': True,
            '–print_urls': True
        }

        response.download(arguments)

    def get_text(self):
        wikipedia.set_lang('pt')
        return self.add_breakline(wikipedia.summary(self.assunto))
