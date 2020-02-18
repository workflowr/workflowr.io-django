import django
import github
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from projects.models import Author, Platform, Project, Publication, Tag

gh_token = os.environ['GH_TOKEN']
gh = github.Github(gh_token)
gh_me = gh.get_user()
sys.stderr.write("Logged into GitHub as %s\n"%(gh_me.login))

# https://github.com/jdblischak/singlecell-qtl
repo = gh.get_repo("jdblischak/singlecell-qtl")
aut, created = Author.objects.get_or_create(name=repo.owner.login, email="jdblischak@email.com")
repo.get_topics()
pub, created = Publication.objects.get_or_create(
    doi="10.1371/journal.pgen.1008045",
    title="Discovery and characterization of variance QTLs in human induced pluripotent stem cells."
)
proj, created = Project.objects.get_or_create(
    name=repo.name,
    url=repo.html_url,
    author=aut,
    platform=Platform.objects.get(name="GitHub")
)

proj.publications.add(pub)

# https://github.com/jdblischak/fucci-seq
repo = gh.get_repo("jdblischak/fucci-seq")
tags = repo.get_topics()
proj, created = Project.objects.get_or_create(
    name=repo.name,
    url=repo.html_url,
    author=aut,
    platform=Platform.objects.get(name="GitHub")
)
for tag in tags:
    tag_model, created = Tag.objects.get_or_create(name=tag)
    proj.tags.add(tag)

# https://github.com/stephenslab/wflow-divvy
repo = gh.get_repo("stephenslab/wflow-divvy")
aut, created = Author.objects.get_or_create(name=repo.owner.login, email="stephenslab@email.com")
repo.get_topics()
proj, created = Project.objects.get_or_create(
    name=repo.name,
    url=repo.html_url,
    author=aut,
    platform=Platform.objects.get(name="GitHub")
)


