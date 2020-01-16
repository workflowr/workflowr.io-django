from django.test import Client
from django.test import TestCase

from projects.models import Author, Platform, Project, Publication, Tag


class UrlTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        aut1 = Author.objects.create(
            name="author_1", email="email_1@example.com")
        aut2 = Author.objects.create(
            name="author_2", email="email_2@example.com")
        aut3 = Author.objects.create(
            name="author_3", email="email_3@example.com")

        tag1 = Tag.objects.create(name="tag_1")
        tag2 = Tag.objects.create(name="tag_2")
        tag3 = Tag.objects.create(name="tag_3")

        pub1 = Publication.objects.create(
            doi="10.1000/1", title="publication 1")
        pub2 = Publication.objects.create(
            doi="10.1000/2", title="publication 2")
        pub3 = Publication.objects.create(
            doi="10.1000/3", title="publication 3")

        plat1 = Platform.objects.create(
            name="GitHub", url="https://github.com/")
        plat2 = Platform.objects.create(
            name="GitLab", url="https://gitlab.com/")

        proj1 = Project.objects.create(
            name="project_1",
            url="https://example.com/1",
            author=Author.objects.get(id=1),
            platform=Platform.objects.get(name="GitHub"))
        proj2 = Project.objects.create(
            name="project_2",
            url="https://example.com/2",
            author=Author.objects.get(id=2),
            platform=Platform.objects.get(name="GitHub"))
        proj3 = Project.objects.create(
            name="project_3",
            url="https://example.com/3",
            author=Author.objects.get(id=3),
            platform=Platform.objects.get(name="GitLab"))

        proj1.publications.add(pub1)
        proj2.publications.add(pub2)
        proj3.publications.add(pub3)

        proj1.tags.add(tag1, tag2)
        proj2.tags.add(tag3)

    def setUp(self):
        self.client = Client()

    def test_navigate_to_projects(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list"]), 3)

    def test_navigate_to_projects_platform(self):
        response = self.client.get("/projects/GitHub/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list_for_platform"]), 2)

        response = self.client.get("/projects/GitLab/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list_for_platform"]), 1)

    def test_navigate_to_projects_platform_author(self):
        response = self.client.get("/projects/GitHub/author_1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list_for_author"]), 1)

        response = self.client.get("/projects/GitHub/author_2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list_for_author"]), 1)

        response = self.client.get("/projects/GitHub/author_3/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get("/projects/GitLab/author_3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["project_list_for_author"]), 1)

    def test_navigate_to_projects_platform_author_project(self):
        response = self.client.get("/projects/GitHub/author_1/project_1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["project"].name, "project_1")

        response = self.client.get("/projects/GitHub/author_2/project_2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["project"].name, "project_2")

        response = self.client.get("/projects/GitHub/author_3/project_3/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get("/projects/GitLab/author_3/project_3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["project"].name, "project_3")

    def test_navigate_to_authors(self):
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["author_list"]), 3)

    def test_navigate_to_tags(self):
        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tag_list"]), 3)

    def test_navigate_to_tagdetail(self):
        response = self.client.get("/tag/tag_1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"].name, "tag_1")

        response = self.client.get("/tag/tag_2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"].name, "tag_2")

        response = self.client.get("/tag/tag_3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["tag"].name, "tag_3")

        response = self.client.get("/tag/tag_4")
        self.assertEqual(response.status_code, 404)

    def test_navigate_to_publications(self):
        response = self.client.get("/publications/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["publication_list"]), 3)
