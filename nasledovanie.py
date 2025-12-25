class ClientShort:
    def __init__(self, client_id, last_name, first_name, middle_name, phone):
        self.client_id = client_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name or ""
        self.phone = phone


    def full_fio(self):
        if self.middle_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        return f"{self.last_name} {self.first_name}"

    def short_fio(self):
        f = self.first_name[0] + "." if self.first_name else ""
        m = self.middle_name[0] + "." if self.middle_name else ""
        return f"{self.last_name} {f}{m}"


    def __str__(self):
        return f"[{self.client_id}] {self.short_fio()}, тел: {self.phone}"

    def __repr__(self):
        return f"ClientShort(id={self.client_id}, fio='{self.short_fio()}', phone='{self.phone}')"


    def __eq__(self, other):
        return isinstance(other, (ClientShort, Client)) and self.client_id == other.client_id

    @classmethod
    def from_string(cls, client_id, data_str: str):
        parts = [part.strip() for part in data_str.split(",", 1)]  

        if len(parts) < 2:
            raise ValueError("Некорректная строка для ClientShort (ожидается ФИО, телефон)")

        fio_str, phone = parts
        fio = fio_str.split()

        if len(fio) == 2:
            last, first = fio
            middle = ""
        elif len(fio) == 3:
            last, first, middle = fio
        else:
            raise ValueError("ФИО должно содержать 2 или 3 слова")

        return cls(client_id, last, first, middle, phone)


class Client(ClientShort):
    def __init__(self, client_id, last_name, first_name, middle_name, address, phone):
        super().__init__(client_id, last_name, first_name, middle_name, phone)

        self.address = address


    def __str__(self):
        return f"[{self.client_id}] {self.full_fio()}, адрес: {self.address}, тел: {self.phone}"

    def __repr__(self):
        return f"Client(id={self.client_id}, fio='{self.full_fio()}', address='{self.address}', phone='{self.phone}')"


    @classmethod
    def from_string(cls, client_id, data_str: str):
        fio_str, address, phone = [part.strip() for part in data_str.split(",", 2)]
        fio = fio_str.split()

        if len(fio) == 2:
            last, first = fio
            middle = ""
        elif len(fio) == 3:
            last, first, middle = fio
        else:
            raise ValueError("ФИО должно содержать 2 или 3 слова")

        return cls(client_id, last, first, middle, address, phone)