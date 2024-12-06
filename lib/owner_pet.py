class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")

        self.pet_type = pet_type
        self.owner = owner

        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            owner.add_pet(self) 

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []  # List to store the owner's pets

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")

        self.pets_list.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
