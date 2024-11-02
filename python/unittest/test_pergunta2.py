import unittest
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def descriptografar_mensagem_aes(mensagem_criptografada, chave):
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

class TestesDescriptografia(unittest.TestCase):
    def teste_descriptografia_sucesso(self):
        mensagem_criptografada = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        chave = "thisisasecretkey"
        mensagem_esperada = "Sistemas Embarcados"
        mensagem_descriptografada = descriptografar_mensagem_aes(mensagem_criptografada, chave)
        self.assertEqual(mensagem_descriptografada, mensagem_esperada)

    def teste_descriptografia_chave_invalida(self):
        mensagem_criptografada = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        chave = "chave_incorreta"  # Chave inválida
        with self.assertRaises(ValueError):  # Espera-se que uma ValueError seja lançada
            descriptografar_mensagem_aes(mensagem_criptografada, chave)

if __name__ == '__main__':
    unittest.main()