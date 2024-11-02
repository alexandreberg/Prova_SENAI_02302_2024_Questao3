from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def descriptografar_mensagem(mensagem_criptografada, chave):
    """
    Descriptografa uma mensagem usando a chave fornecida.
    """
    # Converte a chave de string para bytes
    chave = chave.encode()

    # Deriva uma chave de criptografia a partir da senha
    salt = b'\x00' * 16  # Pode ser um salt aleatório
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    chave_derivada = kdf.derive(chave)

    # Cria um objeto Fernet com a chave derivada
    f = Fernet(chave_derivada)

    # Descriptografa a mensagem
    mensagem_descriptografada = f.decrypt(mensagem_criptografada.encode())

    # Decodifica a mensagem de bytes para string
    return mensagem_descriptografada.decode()

# Mensagem criptografada
mensagem_criptografada = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"

# Chave de criptografia
chave = "thisisasecretkey"

# Descriptografa a mensagem
mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, chave)

# Imprime a mensagem descriptografada
print("Mensagem descriptografada:", mensagem_descriptografada)