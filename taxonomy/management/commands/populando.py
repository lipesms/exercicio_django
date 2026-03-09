from django.core.management.base import BaseCommand, CommandError
from taxonomy.models import Category, Tag

class Command(BaseCommand):
    help = "A comand to feed the database with a sort of data."

    def handle(self, *args, **options):

        tec = Category.objects.get(id=1)
        print(tec.slug)
        categorias = Category.objects.all()[:2]
        print(categorias)


# basta mudar o diretorio management para um app especifico
