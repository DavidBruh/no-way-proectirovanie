class Client:
    def __init__(self, client_id, last_name, first_name, middle_name, address, phone):
        self.__client_id = self.validate_client_id(client_id)
        self.__last_name = self.validate_name(last_name, "Фамилия")
        self.__first_name = self.validate_name(first_name, "Имя")
        self.__middle_name = self.validate_name(middle_name, "Отчество", required=False)
        self.__address = self.validate_address(address)
        self.__phone = self.validate_phone(phone)

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
