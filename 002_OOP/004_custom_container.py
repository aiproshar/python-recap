"""
The Properties needed to be qualified as a container
 len(CustomContainerClass)
 Iterable, for items in CustomContainerClass -> Needs to be satisfied
"""

#TODO: Implement later, skipping now
class CustomContainer:
    def __init__(self):
        self.tags = list()

    def add_tag(self, tag):
        self.tags.append(tag)
        sorted(self.tags)

    def delete_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise ValueError("Tag does not exist")
