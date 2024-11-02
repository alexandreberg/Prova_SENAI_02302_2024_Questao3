# Importando as bibliotecas
from Crypto.Cipher import AES           #importa biblioteca Crypto.Cipher com módulo AES
from Crypto.Util.Padding import unpad   #importa bilioteca Crypto.Util.Padding com módulo unpad

# Funçã opara descriptografar a mensagem: mensagem_criptografada com a chave: chave
def descriptografa_mensagem_aes(mensagem_criptografada, chave):
  
  """
  Descriptografa uma mensagem AES em modo ECB com chave de 128 bits.
  """
  
  # Converte a chave de string para bytes
  chave = chave.encode()

  # Converte a mensagem criptografada (hexadecimal) para bytes
  mensagem_criptografada = bytes.fromhex(mensagem_criptografada)

  # Cria um objeto AES no modo ECB
  cifra = AES.new(chave, AES.MODE_ECB)

  # Descriptografa a mensagem
  mensagem_descriptografada = cifra.decrypt(mensagem_criptografada)

  # Remove o padding (se houver)
  mensagem_descriptografada = unpad(mensagem_descriptografada, AES.block_size)

  # Decodifica a mensagem de bytes para string
  return mensagem_descriptografada.decode()


# Mensagem criptografada
mensagem_criptografada = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"

# Chave de criptografia
chave = "thisisasecretkey"

# Descriptografa a mensagem
mensagem_descriptografada = descriptografa_mensagem_aes(mensagem_criptografada, chave)

# Imprime a mensagem descriptografada
print("Mensagem descriptografada:", mensagem_descriptografada)