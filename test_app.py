from app import Login, criptografar
from cryptographyFramework import encryptMessage, initializeWrite
from valida_login import validaSenha, validaUsuario

'''

def descriptografar(usuario='', senha='', descriptAll = False):
    if not Login(usuario, senha): return
    initializeRead()

    if descriptAll == False:
        mensagemCriptografada = readNextLine()
        mensagemDescriptografada = decryptMessage(usuario, senha, mensagemCriptografada)
        return mensagemDescriptografada
    
    if descriptAll == True:
        mensagensCriptografadas = readAllLines()
        mensagensDescriptografadas = {}

        for index, mensagem in enumerate(mensagensCriptografadas, start=1):
            if mensagem == None: continue
            mensagensDescriptografadas[index] = {'mensagem': decryptMessage(usuario, senha, mensagem)}
        return mensagensDescriptografadas

        def criptografar(usuario = '', senha = '', mensagens = []):
        if Login(usuario, senha) == False: return
        initializeWrite()
        for mensagem in mensagens:
            encryptedText = encryptMessage(usuario, senha, mensagem)
            saveNewLine(encryptedText)
'''

def test_criptografar_varias_mensagens():
    usuario = 'MariaSilva'
    senha = 'SenhaFort3'
    mensagens = ['ISTO E UM TESTE 1','ISTO E UM TESTE 2', 'ISTO E UM TESTE 3','ISTO E UM TESTE 4','ISTO E UM TESTE 5']
    criptografar(usuario, senha, mensagens)
    resultado_esperado = [encryptMessage(usuario, senha, mensagem).decode('utf-8') for mensagem in mensagens]
    with open('message.txt', 'r') as f:
        conteudo_arquivoErros = f.readlines()
        conteudo_arquivoCorreto = []
        for mensagem in conteudo_arquivoErros:
            conteudo_arquivoCorreto.append(mensagem.replace('\n', '')) 
        print(resultado_esperado, conteudo_arquivoCorreto)
    
def test_Login():
    # Usuários e senhas válidos
    assert Login("FulanoDeTal", "SenhaSegura123!") == True
    assert Login("CiclanoSilva", "OutraSenhaSegura1@") == True
    assert Login("BeltranoGomes", "UmaSenhaComNumeros123@") == True
    assert Login("AnaSouza", "SenhaMuitoBoa123@") == True
    assert Login("JoaquimFerreira", "SenhaFortissima$123") == True

    # Usuários e senhas inválidos
    assert Login("", "") == False
    assert Login("UsuárioTeste", "") == False
    assert Login("", "SenhaTeste123!") == False
    assert Login("beltrano.gomes", "SenhaInsegura") == False
    assert Login("Ciclano Silva", "OutraSenha1234@") == False
    assert Login("JohnDoe", "SENHA123!") == False
    assert Login("usuarioMuitoGrande", "SenhaInsegura123!") == False
    assert Login("UsuarioCurto", "senhafraca") == False
    
def test_validaUsuario():
    assert validaUsuario("") == False
    assert validaUsuario("Usuário com mais de 30 caracteres aqui") == False
    assert validaUsuario("Usuário com espaço") == False
    assert validaUsuario("usuário com letra minúscula") == False
    assert validaUsuario("UsuarioSemCaracteresEspeciais") == True
    assert validaUsuario("UsuarioComNumero123") == False
    assert validaUsuario("UsuarioComCaracterEspecial@") == False
    assert validaUsuario("UsuarioComTudo123@") == False
    assert validaUsuario("UsuarioComTudo123@A") == False

def test_validaSenha():
    assert validaSenha("") == False
    assert validaSenha("senha curta") == False
    assert validaSenha("senhainsegura") == False
    assert validaSenha("senhacomnumerosemcaracteresespeciais123") == False
    assert validaSenha("senhacaracteres@especiais!") == False
    assert validaSenha("SenhaMaiusculaMinuscula1@") == True
    assert validaSenha("Senhaforte!123456") == True

if __name__ == '__main__':
    test_Login()
