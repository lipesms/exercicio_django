from django.core.management.base import BaseCommand, CommandError
from taxonomy.models import Category, Tag

class Command(BaseCommand):
    help = "A comand to feed the database with a sort of data."

    def handle(self, *args, **options):
        categoria = Category(name="tecnologia", slug="artigos-de-tecnologia")
        categoria.save()

# basta mudar o diretorio management para um app especifico
