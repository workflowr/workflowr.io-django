from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

from .models import Tag
from . import views

class TagListViewTests(TestCase):

    def setUp(self):
        Tag.objects.create(name = "tag_1")
        Tag.objects.create(name = "tag_2")
        Tag.objects.create(name = "tag_3")

    def test_tag_list_view_contains_all_tags(self):
        response = self.client.get(reverse('projects:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['tag_list'],
            ['<Tag: tag_1>', '<Tag: tag_2>', '<Tag: tag_3>'],
            ordered=False
        )

    def test_tag_list_url_maps_to_view(self):
        view = resolve('/tags/')
        self.assertEquals(view.func.__name__, views.TagList.as_view().__name__)

    def test_tag_list_with_no_tags(self):
        Tag.objects.all().delete()
        response = self.client.get(reverse('projects:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['tag_list'],
            [],
            ordered=False
        )
        self.assertContains(response, 'No tags have been defined.')

class TagDetailViewTests(TestCase):

    def setUp(self):
        Tag.objects.create(name = "tag_1")
        Tag.objects.create(name = "tag_2")
        Tag.objects.create(name = "tag_3")

    def test_tag_detail_view_contains_single_tag(self):
        url = reverse('projects:tag_detail', kwargs={'name': 'tag_2'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        object_expected = Tag.objects.get(name = 'tag_2')
        object_observed = response.context['tag']
        self.assertEquals(object_observed, object_expected)
        self.assertContains(response, 'tag_2')

    def test_tag_detail_url_maps_to_view(self):
        view = resolve('/tag/tag_2')
        self.assertEquals(view.func.__name__, views.TagDetail.as_view().__name__)

    def test_404_for_missing_tag(self):
        url = reverse('projects:tag_detail', kwargs={'name': 'does_not_exist'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class IndexTests(TestCase):

    def test_index_url_maps_to_view(self):
        view = resolve('/')
        self.assertEquals(view.func, views.index)

