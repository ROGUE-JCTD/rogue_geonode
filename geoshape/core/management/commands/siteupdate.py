from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(BaseCommand):
    help = 'Updates a Site object.'
    args = '<site id>'
    option_list = BaseCommand.option_list + (
        make_option('-s', '--site-id',
                    dest='site',
                    default='1',
                    help='The site id to update.  Defaults to 1.'),
        make_option('-d', '--domain',
                    dest='domain',
                    default='http://example.com',
                    help='The site\'s domain.  http://example.com'),
        make_option('-n', '--display-name',
                    dest='name',
                    default='example.com',
                    help='The display name of the site.'),
    )

    def handle(self, *args, **options):

        site_id = options.get('site')
        domain = args[0] if args else options.get('domain')
        name = options.get('name')

        site, created = Site.objects.get_or_create(pk=int(site_id), defaults=dict(domain=domain, name=name))

        if not created:
            site.domain = domain
            site.name = name

        site.save()
        Site.objects.clear_cache()

        self.stdout.write('Successfully updated site {0} to: {1}.'.format(site_id, site.domain))
