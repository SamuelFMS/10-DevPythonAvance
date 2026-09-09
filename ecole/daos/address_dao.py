from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.address import Address


@dataclass
class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        with Dao.connection.cursor() as cursor:
            sql = ("INSERT INTO address(street, city, postal_code) VALUES(%s, %s, %s)")
            cursor.execute(sql, (address.street, address.city, address.postal_code))
            id_address = cursor.lastrowid
            Dao.connection.commit()
        if id_address is not None:
            address.id = id_address
            return id_address
        else:
            return 0

    def read(self, id_address: int) -> Optional[Address]:
        """Renvoit l'addresse' correspondant à l'entité dont l'id est id_address
           (ou None s'il n'a pu être trouvé)"""
        address: Optional[Address]

        with Dao.connection.cursor() as cursor:
            sql = ("SELECT * "
                   "FROM address "
                   "WHERE id_address = %s")
            cursor.execute(sql, (id_address))
            record = cursor.fetchone()
        return self.parse(record)

    def update(self, address: Address) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = ("UPDATE address "
                   "SET street=%(street)s, "
                   "city=%(city)s, "
                   "postal_code=%(postal_code)s "
                   "WHERE id_address=%(id_address)s")

            cursor.execute(sql, {"street": address.street, "city": address.city, "postal_code": address.postal_code,
                "id_address": address.id})
            if (cursor.rowcount == 1):
                Dao.connection.commit()
                return True
            else:
                return False

    def delete(self, address: Address) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = ("DELETE FROM address WHERE id_address=%s")
            cursor.execute(sql, (address.id))
            if cursor.rowcount == 1:
                Dao.connection.commit()
                return True
            else:
                return False

    def get_all(self) -> Optional[list[Address]]:
        list_address: Optional[list[Address]] = None
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address"
            cursor.execute(sql)
            record = cursor.fetchall()
            if record is not None:
                list_address = []
                for course in record:
                    address_object: Optional[Address] = self.parse(course)
                    if(address_object is not None):
                        list_address.append(address_object)
        return list_address

    def parse(self, record) -> Optional[Address]:
        address: Optional[Address]
        if record is not None:
            address = Address(street=record['street'], city=record['city'], postal_code=record['postal_code'])
            address.id = record['id_address']
        else:
            address = None
        return address
