from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.address import Address


@dataclass
class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        with Dao.connection.cursor() as cursor:
            sql = (
                "INSERT INTO address(street, city, postal_code) VALUES(%s, %s, %s)"
            )
            cursor.execute(sql, (address.street, address.city, address.postal_code))
            id_address = cursor.lastrowid
            Dao.connection.commit()
        if id_address is not None:
            return id_address
        else:
            return 0

    def read(self, id_address: int) -> Optional[Address]:
        """Renvoit l'addresse' correspondant à l'entité dont l'id est id_address
           (ou None s'il n'a pu être trouvé)"""
        address: Optional[Address]

        with Dao.connection.cursor() as cursor:
            sql = (
                "SELECT * "
                "FROM address "
                "WHERE id_address = %s"
            )
            cursor.execute(sql, (id_address))
            record = cursor.fetchone()
        if record is not None:
            address = Address(
                street=record['street'],
                city=record['city'],
                postal_code=record['postal_code'])
        else:
            address = None

        return address


    def update(self, address: Address) -> bool:
        return True

    def delete(self, address: Address) -> bool:
        return True
