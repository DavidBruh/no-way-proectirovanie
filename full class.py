
class Client:
    def __init__(self, client_id, last_name, first_name, middle_name, address, phone):
        self.__client_id = client_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__address = address
        self.__phone = phone

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if value <= 0:
            raise ValueError("ID клиента должен быть положительным числом")
        self.__client_id = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value or len(value) < 2:
            raise ValueError("Фамилия должна содержать минимум 2 символа")
        self.__last_name = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value or len(value) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        self.__first_name = value

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Адрес не может быть пустым")
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not value or len(value) < 10:
            raise ValueError("Телефон введён неверно")
        self.__phone = value

client = Client(
    client_id=1,
    last_name="Иванов",
    first_name="Иван",
    middle_name="Иванович",
    address="г. Москва, ул. Ленина",
    phone="89995553322"
)

print(client.first_name)
client.phone = "89990001122"  # изменяем телефон
print(client.phone)