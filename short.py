class ClientShort:
    def __init__(self, client: Client):
        self._client_id = client.client_id
        self._phone = client.phone
        self._short_name = self._format_short_name(client)

    def _format_short_name(self, client: Client) -> str:
        first_initial = f"{client.first_name[0]}." if client.first_name else ""
        middle_initial = f"{client.middle_name[0]}." if client.middle_name else ""
        return f"{client.last_name} {first_initial}{middle_initial}"

    @property
    def client_id(self):
        return self._client_id

    @property
    def short_name(self):
        return self._short_name

    @property
    def phone(self):
        return self._phone

    def __str__(self):
        return f"{self.short_name} [ID: {self.client_id}]"

    def __repr__(self):
        return f"ClientShort(id={self.client_id}, name={self.short_name})"