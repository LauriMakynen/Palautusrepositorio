class Project:
    def __init__(self, name, description, license_, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license_
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n" + "\n".join(f"- {x}" for x in dependencies) if len(dependencies) > 0 else "-"

    def _stringify_authors(self, authors):
        return "\n" + "\n".join(f"- {x}" for x in authors) if len(authors) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_authors(self.authors)}"
            f"\n\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )