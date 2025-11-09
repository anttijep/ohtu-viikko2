from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        obj = tomli.loads(content)
        poetry = obj["tool"]["poetry"]
        name = poetry.get("name", "")
        desc = poetry.get("description", "")
        deps = list(poetry.get("dependencies", {}).keys())
        dev_deps = list(poetry.get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        license = poetry.get("license", None)
        authors = poetry.get("authors", [])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, deps, dev_deps, license, authors)
