from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Luekee tiedoston merkkijonomuotoisen sisällön
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        # Hakee tarvittavat tiedot pyproject.toml:sta
        poetry_data = data.get("tool", {}).get("poetry", {})

        name = poetry_data.get("name", "")
        description = poetry_data.get("description", "")
        license_ = poetry_data.get("license", "")
        authors = poetry_data.get("authors", [])

        # Muodostaa listan riippuvuuksista
        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(
            poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys()
        )

        #Muodostaa Project-olion
        return Project(name, description, license_, authors, dependencies, dev_dependencies)