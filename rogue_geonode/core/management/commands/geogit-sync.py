from base64 import b64encode
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import json
import urllib
import urllib2


class Command(BaseCommand):
    help = 'Synchronizes a geogit repository using the Geoserver-Geogit api.'
    args = '<arg>'
    option_list = BaseCommand.option_list + (
        make_option('-u', '--url',
                    dest='url',
                    default='http://example.com',
                    help='The url to the repository you want to sync.'),
        make_option('-d', '--direction',
                    dest='direction',
                    default='duplex',
                    help='The direction that you want to sync in (push, pull, or duplex).'),
        make_option('-r', '--remote',
                    dest='remote',
                    default='origin',
                    help='The remote that you want to sync with. Defaults to origin.'),
        make_option('--remotebranch',
                    dest='remoteBranch',
                    default='master',
                    help='The remote branch to sync. Defaults to master.'),
        make_option('--localbranch',
                    dest='localBranch',
                    default='master',
                    help='The local branch to sync. Defaults to master.'),
        make_option('--username',
                    dest='username',
                    default=None,
                    help='The username to use for basic auth requests.'),
        make_option('--password',
                    dest='password',
                    default=None,
                    help='The password to use for basic auth requests.'),
    )

    def make_request(self, url, params, auth=None):
        """
        Prepares a request from a url, params, and optionally authentication.
        """
        req = urllib2.Request(url + urllib.urlencode(params))

        if auth:
            req.add_header('AUTHORIZATION', 'Basic ' + auth)

        return urllib2.urlopen(req)

    def handle(self, *args, **options):

        url = options.get('url')

        if (not (url is None)) or len(url)==0:
            raise CommandError("The url specified is either missing or blank.")

        index = url.rfind('/')

        if index != (len(url)-1):
            url += '/'

        direction = options.get('direction')

        if not (direction=="push" or direction=="pull" or direction=="duplex"):
            raise CommandError("The sync direction must be either: push, pull, or duplex.")

        remote = options.get('remote')
        remoteBranch = options.get('remoteBranch')
        localBranch = options.get('localBranch')
        username = options.get('username')
        password = options.get('password')
        auth = None

        if username and password:
            auth = b64encode('{0}:{1}'.format(username, password))

        params = {'output_format': 'JSON', 'remoteName': remote, 'ping': 'true'}
        request = self.make_request(url=url+'remote?', params=params, auth=auth)
        pingSuccess = False
        if request.getcode() != 200:
            raise CommandError("The server that you are trying to sync seems to be down at the moment, "
                               "try again later.")
        try:
            response = json.loads(request.read())
            if 'ping' in response['response']:
                if response['response']['ping']['success']:
                    pingSuccess = True
        except ValueError:
            pass
        if not pingSuccess:
            raise CommandError("The remote that you are trying to sync with seems to be down at the moment, try again "
                               "later.")

        def endTransaction(cancel, transactionId):
            params = {'output_format': 'JSON', 'cancel': cancel, 'transactionId': transactionId}
            request = self.make_request(url=url+'endTransaction?', params=params, auth=auth)

            if request.getcode() != 200:
                raise CommandError("EndTransaction failed: Status Code {0}".format(request.getcode()))

            response = json.loads(request.read())

            if not response['response']['success']:
                raise CommandError("An error occurred on endTransaction: {0}".format(response['response']['error']))

        params = {'output_format': 'JSON'}
        self.stdout.write('Starting transaction...')
        request = self.make_request(url=url+'beginTransaction?', params=params, auth=auth)

        if request.getcode() != 200:
            raise CommandError("BeginTransaction failed: Status Code {0}".format(request.getcode()))
        response = json.loads(request.read())

        if not response['response']['success']:
            raise CommandError("An error occurred on beginTransaction: {0}".format(response['response']['error']))

        self.stdout.write('Transaction started')
        transactionId = response['response']['Transaction']['ID']

        if direction=="pull" or direction=="duplex":
            params = {'output_format': 'JSON',
                      'remoteName': remote,
                      'ref': remoteBranch+':'+localBranch,
                      'transactionId': transactionId}

            self.stdout.write('Beginning pull...')
            request = self.make_request(url=url+'pull?', params=params, auth=auth)

            if request.getcode() != 200:
                endTransaction(True, transactionId)
                raise CommandError("Pull failed: Status Code {0}".format(request.getcode()))
            response = json.loads(request.read())
            if response['response']['success']:
                if 'Merge' in response['response']:
                    endTransaction(True, transactionId)
                    raise CommandError("There were conflicts on pull")
            else:
                endTransaction(True, transactionId)
                raise CommandError("An error occurred on pull: {0}".format(response['response']['error']))
            self.stdout.write('Pull completed')

        if direction=="push" or direction=="duplex":
            params = {'output_format': 'JSON',
                      'remoteName': remote,
                      'ref': localBranch+':'+remoteBranch,
                      'transactionId': transactionId}

            self.stdout.write('Beginning push...')
            request = self.make_request(url=url+'push?', params=params, auth=auth)

            if request.getcode() != 200:
                endTransaction(True, transactionId)
                raise CommandError("Push failed: Status Code {0}".format(request.getcode()))
            response = json.loads(request.read())

            if not response['response']['success']:
                endTransaction(True, transactionId)
                raise CommandError("An error occurred on push: {0}".format(response['response']['error']))

            self.stdout.write('Push completed')

        self.stdout.write('Finishing transaction...')
        endTransaction(False, transactionId)
        self.stdout.write('Transaction completed')
