import pprint
import requests 

from django.core.management.base import BaseCommand
from django.utils import timezone
from creatorz.models import PlayError

pp = pprint.PrettyPrinter(indent=4)

class Command(BaseCommand):
    help = 'Allows to manage PlayError entries'

    def add_arguments(self, parser):
        parser.add_argument('error_id', nargs='?', type=int)
        parser.add_argument(
            '--list',
            action='store_true',
            dest='list',
            help='List PlayError entries',
        )
        parser.add_argument(
            '--sync',
            action='store_true',
            dest='sync',
            help='Sync PlayError entries',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete PlayError entries',
        )


    def handle(self, *args, **kwargs):
        if kwargs['list']:
            self.handle_list(kwargs['error_id'])
        if kwargs['sync']:
            self.handle_sync(kwargs['error_id'])
        if kwargs['delete']:
            self.handle_delete(kwargs['error_id'])
                

    def handle_list(self, error_id):
        for e in self.get_errors(error_id): 
            pp.pprint(e.__dict__) if len(self.get_errors(error_id)) > 0 else self.stdout.write('No PlayError entry to display.')

    def handle_sync(self, error_id):
        for e in self.get_errors(error_id): 
            try:
                response = requests.post(e.remote_url, json=e.playback.serialize(), timeout=1)
                if response.status_code == 201:
                    self.stdout.write(self.style.SUCCESS('Successfully synchronized PlayError with id "%s".' % e.id))
                    self.delete_error(e.id)
                else:
                    self.stdout.write(self.style.ERROR('Could not synchronized PlayError with id "%s". An error occured, please try again later.' % e.id))
            except Exception as er:
                print(er)
                self.stdout.write(self.style.WARNING('Could not synchronized PlayError with id "%s". Timeout from remote, please try again later.' % e.id))

    def handle_delete(self, error_id):
        for e in self.get_errors(error_id): 
            self.delete_error(e.id)

    def get_errors(self, error_id):
        return PlayError.objects.filter(id=error_id) if error_id else PlayError.objects.all()
    
    def delete_error(self, error_id):
        self.stdout.write('Now deleting PlayError with id "%s".' % error_id)
        PlayError.objects.filter(id=error_id).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted PlayError with id "%s".' % error_id))