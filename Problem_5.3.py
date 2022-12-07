#Jose Lopez
#12/4/2022

#Problem 5: A function that checks with your game character has all the items they've picked out.

class Book:
    def __init__(self, supply, pages, thought, mind_process):
        self.supply = supply
        self.pages = pages
        self.thought = thought
        self.mind_process = mind_process

    def story_requirements(self):
        return self.supply, self.pages, self.thought

    def process_requirement(self):
        return self.mind_process

write_book = Book('Pen', 'Paper', 'Idea', 'Confusion')
for book in write_book.story_requirements():
    print("To write a book you need:", book)
print("While writing the book you cannot have:", write_book.process_requirement())