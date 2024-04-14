
class great_software_developer:
    def __init__(self, developer_id):
        self.traits = []
        self.developer_id = developer_id
        
    def add_trait(self, trait):
        self.traits.append(trait)
        
    def print_traits(self):
        print(f"Traits of developer {self.developer_id}:")
        for trait in self.traits:
            print("-",trait)
            


developer = great_software_developer(1)
traits_dev_1 = [
    "Maintaining a neutral standpoint.",
    "Indepth knowledge of software fundementals",
    "Adaptability"
    ]
for trait in traits_dev_1:
    developer.add_trait(trait)    
developer.print_traits()