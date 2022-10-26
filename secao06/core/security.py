import imp
from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def vericar_senha(senha: str, hash_senha: str)  -> bool:
    """
    Função para verifivcar se a senha esta correta, comparando a senha em texto puro,
     informada pelo usuario, e o hash da senha que estarra salvo no abnco de dados durante a criação da conta.
    """

    return CRIPTO.verify(senha, hash_senha)

def gerar_has_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """

    return CRIPTO.hash(senha)