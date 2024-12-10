class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = "unprocessableEntity"
        self.status_code = 422

try:
    print("Estou no bloco try")
    raise HttpUnprocessableEntityError("Estou lançando a Exception")
except Exception as exception:
    print("Estou no tratamento de erro")
    print(exception.name)
    print(exception.status_code)
    print(exception.message)
