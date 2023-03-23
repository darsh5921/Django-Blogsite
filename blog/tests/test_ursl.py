
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import PostList,UserList,about,DraftListView,PostCreate,post_publish

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url =   reverse('home')
        self.assertEqual(resolve(url).func.__name__,PostList.__name__)
    def test_about_url_is_resolved(self):
        url =   reverse('about')
        self.assertEqual(resolve(url).func.__name__,about.__name__)
    def test_post_draft_list_url_is_resolved(self):
        url =   reverse('post-draft-list')
        self.assertEqual(resolve(url).func.__name__,DraftListView.__name__)
    def test_post_create_url_is_resolved(self):
        url =   reverse('post-create')
        self.assertEqual(resolve(url).func.__name__,PostCreate.__name__)
    def test_post_publish_url_is_resolved(self):
        url =   reverse('post-publish',args=["post/1/publish"])
        self.assertEqual(resolve(url).func.__name__,post_publish.__name__)
