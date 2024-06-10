class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all_pets = []

    def __init__(self, name, pet_type, owner=None) -> None:
        self.name = name
        self.pet_type = pet_type.lower()
        self.owner = owner
        if self.pet_type not in self.PET_TYPES:  
            raise ValueError(f"Invalid pet type: {pet_type}. Allowed types are {', '.join(self.PET_TYPES)}")
        Pet.all_pets.append(self)  

    def pet_name(self):
        return self.name


class Owner:
    def __init__(self, name) -> None:
        self.name = name

    def add_pet(self, pet):
        pet.owner = self  
        Pet.all_pets.append(pet)

    def pets(self):
        return [pet for pet in Pet.all_pets if pet.owner == self]

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

# Test cases
def test_pet_has_all():
    
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")
    assert pet1 in Pet.all_pets
    assert pet2 in Pet.all_pets

def test_owner_adds_pets():
   
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)
    assert pet.owner == owner
    assert pet in owner.pets()

test_pet_has_all()
test_owner_adds_pets()
