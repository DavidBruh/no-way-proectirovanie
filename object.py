import json

class Client:
    def __init__(self, client_id, last_name, first_name, middle_name,
                 address, phone):

        self.__client_id = self.validate_client_id(client_id)
        self.__last_name = self.validate_name(last_name, "Фамилия")
        self.__first_name = self.validate_name(first_name, "Имя")
        self.__middle_name = self.validate_name(middle_name, "Отчество", required=False)
        self.__address = self.validate_address(address)
        self.__phone = self.validate_phone(phone)


    @classmethod
    def from_string(cls, client_id: int, data_str: str):
        parts = [part.strip() for part in data_str.split(",", 2)]

        if len(parts) != 3:
            raise ValueError("Строка должна содержать: ФИО, адрес, телефон")

        fio, address, phone = parts
        fio_parts = fio.split()

        if len(fio_parts) == 2:
            last, first = fio_parts
            middle = ""
        elif len(fio_parts) == 3:
            last, first, middle = fio_parts
        else:
            raise ValueError("ФИО должно содержать 2 или 3 слова")

        return cls(client_id, last, first, middle, address, phone)

    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise ValueError("from_dict ожидает словарь (dict)")
        return cls(
            data["client_id"],
            data["last_name"],
            data["first_name"],
            data.get("middle_name", ""),
            data["address"],
            data["phone"]
        )

    @classmethod
    def from_json(cls, json_string: str):
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON")
        return cls.from_dict(data)

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = self.validate_client_id(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.validate_name(value, "Фамилия")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.validate_name(value, "Имя")

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = self.validate_name(value, "Отчество", required=False)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = self.validate_address(value)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = self.validate_phone(value)

    def __str__(self):
        return (f"Клиент #{self.client_id}: "
                f"{self.last_name} {self.first_name} {self.middle_name}, "
                f"Адрес: {self.address}, Телефон: {self.phone}")

    def short(self):
        first_initial = self.first_name[0] + "." if self.first_name else ""
        middle_initial = self.middle_name[0] + "." if self.middle_name else ""
        return f"{self.last_name} {first_initial}{middle_initial} (ID={self.client_id})"

    def __repr__(self):
        return (f"Client(client_id={self.client_id!r}, "
                f"last_name={self.last_name!r}, "
                f"first_name={self.first_name!r}, "
                f"middle_name={self.middle_name!r}, "
                f"address={self.address!r}, "
                f"phone={self.phone!r})")

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.client_id == other.client_id

    @staticmethod
    def validate_client_id(client_id):
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("ID клиента должен быть положительным числом")
        return client_id

    @staticmethod
    def validate_name(name, field_name, required=True):
        if required and (not name or len(name.strip()) < 2):
            raise ValueError(f"{field_name} должна содержать минимум 2 символа")
        return name.strip() if name else ""

    @staticmethod
    def validate_address(address):
        if not address or not address.strip():
            raise ValueError("Адрес не может быть пустым")
        return address.strip()

    @staticmethod
    def validate_phone(phone):
        phone_digits = "".join(filter(str.isdigit, phone))
        if len(phone_digits) < 10:
            raise ValueError("Телефон введён неверно")
        return phone_digits
