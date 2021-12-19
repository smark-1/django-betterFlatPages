from django.test import TestCase
from .models import FlatPage
from django.contrib.auth.models import User
# Create your tests here.
class views_Test(TestCase):
    def test_registration_required(self):
        # create page
        page=FlatPage.objects.create(url="/test/",title='testing page',
                                     content='testing content',
                                     meta='testing meta',
                                     registration_required=True)
        page.sites.add(1)
        # get response
        response = self.client.get(page.get_absolute_url())

        # test
        self.assertEqual(response.status_code,302)

    def logged_in_user_can_access_registration_required_page(self):
        # create page
        page = FlatPage.objects.create(url="/test/", title='testing page',
                                       content='testing content',
                                       meta='testing meta',
                                       registration_required=True)
        page.sites.add(1)

        # login user
        user=User.objects.create_user('testuser',password='testpassword')
        self.client.login(username='testuser',password='testpassword')

        # get response
        response = self.client.get(page.get_absolute_url())

        # test
        self.assertEqual(response.status_code, 200)

    def test_registration_not_required(self):
        # create page
        page = FlatPage.objects.create(url="/test/", title='testing page',
                                       content='testing content',
                                       meta='testing meta',
                                       registration_required=False)
        page.sites.add(1)
        # get response
        response = self.client.get(page.get_absolute_url())

        # test
        self.assertEqual(response.status_code, 200)

    def test_try_to_render_custom_template(self):
        # create page
        page = FlatPage.objects.create(url="/test/", title='testing page',
                                       content='testing content',
                                       meta='testing meta',
                                       registration_required=False,template_name='betterFlatPages/contact_page.html')
        page.sites.add(1)
        # get response
        response = self.client.get(page.get_absolute_url())

        self.assertIn('betterFlatPages/base.html',(t.name for t in response.templates))

class views_api_Test(TestCase):
    def test_registration_required(self):
        # create page
        page=FlatPage.objects.create(url="/test/",title='testing page',
                                     content='testing content',
                                     meta='testing meta',
                                     registration_required=True)
        page.sites.add(1)
        # get response
        response = self.client.get('/api/pages/test/')

        # test
        self.assertEqual(response.status_code,403)

    def logged_in_user_can_access_registration_required_page(self):
        # create page
        page = FlatPage.objects.create(url="/test/", title='testing page',
                                       content='testing content',
                                       meta='testing meta',
                                       registration_required=True)
        page.sites.add(1)

        # login user
        user=User.objects.create_user('testuser',password='testpassword')
        self.client.login(username='testuser',password='testpassword')

        # get response
        response = self.client.get('/api/pages/test/')

        # test
        self.assertEqual(response.status_code, 200)

    def test_registration_not_required(self):
        # create page
        page = FlatPage.objects.create(url="/test/", title='testing page',
                                       content='testing content',
                                       meta='testing meta',
                                       registration_required=False)
        page.sites.add(1)
        # get response
        response = self.client.get('/api/pages/test/')

        # test
        self.assertEqual(response.status_code, 200)

