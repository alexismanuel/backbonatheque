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
        """ Global handle function calling sub functions """
        if kwargs['list']:
            self.handle_list(kwargs['error_id'])
        if kwargs['sync']:
            self.handle_sync(kwargs['error_id'])
        if kwargs['delete']:
            self.handle_delete(kwargs['error_id'])
                

    def handle_list(self, error_id):
        """ List PlayError entry for correpsonding id or all of them if none is provided"""
        errors = self.get_errors(error_id)
        if len(errors) <= 0:
            self.stdout.write('No PlayError entry to display.')
        else:
            for e in errors: 
                pp.pprint(e.__dict__)

    def handle_sync(self, error_id):
        """ Try to synchronize a PlayBack by calling remote server for a given PlayError id (or all of them if none)"""
        for e in self.get_errors(error_id): 
            try:
                print(e.id)
                response = requests.post(e.remote_url, json=e.playback.serialize(), timeout=1)
                if response.status_code == 201:
                    # Successful syncing handling    
                    self.stdout.write(self.style.SUCCESS('Successfully synchronized PlayError with id "%s".' % e.id))
                    self.delete_error(e.id)
                else:
                    self.stdout.write(self.style.ERROR('Could not synchronized PlayError with id "%s". An error occured, please try again later.' % e.id))
            except Exception as er:
                print(er)
                self.stdout.write(self.style.WARNING('Could not synchronized PlayError with id "%s". Timeout from remote, please try again later.' % e.id))

    def handle_delete(self, error_id):
        """ Iterate on PlayError entry corresponding to given id (or all of them if none given) """
        for e in self.get_errors(error_id): 
            self.delete_error(e.id)

    def get_errors(self, error_id):
        """ Returns a PlayError with corresponding id or all PlayError entries if no id is given"""
        return PlayError.objects.filter(id=error_id) if error_id else PlayError.objects.all()
    
    def delete_error(self, error_id):
        """ Function deleting on PlayError given its id """
        self.stdout.write('Now deleting PlayError with id "%s".' % error_id)
        PlayError.objects.filter(id=error_id).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted PlayError with id "%s".' % error_id))