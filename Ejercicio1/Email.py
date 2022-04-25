class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasena = ''

    def __init__(self, idCuenta, dominio, tipoDominio, contrasena):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena

    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio)

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, mail, contrasena):
        str1 = mail.split('@', 1)       # divide el email en idCuenta y dominio.tipoDominio
        str2 = str1[1].split('.', 1)    # divide el dominio y el tipoDominio
        self.__idCuenta = str1[0]
        self.__dominio = str2[0]
        self.__tipoDominio = str2[1]
        self.__contrasena = contrasena

    def cambiarContrasena(self, nuevaContra):
        self.__contrasena = nuevaContra

    def getContrasena(self):
        return self.__contrasena
