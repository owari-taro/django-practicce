from django.core.management.base import BaseCommand
from posts.models import Post

class Command(BaseCommand):
    help = "テストコマンド"

    def handle(self, *args, **options):
        print(options["name"])
        print(options)
        print(Post.objects.all())
    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', nargs='+', type=str)
        parser.add_argument('-i', '--id', nargs='+',
                            type=int, help='なんかidを指定してください')
