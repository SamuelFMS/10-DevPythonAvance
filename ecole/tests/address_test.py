from daos.address_dao import AddressDao
from models.address import Address


def tests():
    print("Executing tests for Address")
    address_dao = AddressDao()

    # Creation d'un cours
    address = Address(city="Bayonne", street="10 rue",postal_code=64100)
    new_address_id = address_dao.create(address)
    assert new_address_id != 0
    assert address.id == new_address_id

    #Recuperation du cours dans la base de donnée
    read_address:Address|None = address_dao.read(new_address_id)
    assert read_address is not None
    assert read_address.id == new_address_id
    assert read_address.id is not None
    assert read_address.city == "Bayonne"
    assert read_address.street == "10 rue"
    assert read_address.postal_code == 64100

    #Edition de l'address
    read_address.city = "Anglet"
    read_address.street = "20 rue de"
    read_address.postal_code = 64600
    assert address_dao.update(read_address)
    edited_address = address_dao.read(read_address.id)
    assert edited_address.city == "Anglet"
    assert edited_address.street == "20 rue de"
    assert edited_address.postal_code == 64600

    #Suppression du cours que nous venons de créer
    assert address_dao.delete(read_address)


if __name__ == '__main__':
    # tests unitaires
    tests()