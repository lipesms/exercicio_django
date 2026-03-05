from django.core.management.base import BaseCommand, CommandError
from taxonomy.models import Category, Tag

class command(BaseCommand):
    help = "A comand to feed the database with a sort of data."