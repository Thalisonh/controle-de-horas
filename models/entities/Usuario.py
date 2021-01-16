class Usuario:
    _nome = None
    _email = None
    _cpf = None
    _data_nascimento = None
    _senha = None

    def __init__(self):
        self._nome
        self._email
        self._cpf
        self._data_nascimento
        self._senha

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_data_nascimento(self):
        return self._data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        self._senha = senha