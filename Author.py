# Define the Author class in author.py
class Author:
    def __init__(self, id, name, bio):
        self.id = id
        self.name = name
        self.bio = bio

    def __str__(self):
        return f"Author ID: {self.id}\nName: {self.name}\nBio: {self.bio}"

