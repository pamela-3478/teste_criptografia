import re, getpass
from valida_login import validaUsuario, validaSenha
from cryptographyFramework import *

def Login(usuario = '', senha = ''):
    if not validaUsuario(usuario): return False
    if not validaSenha(senha): return False
    return True

def criptografar(usuario = '', senha = '', mensagens = []):
    if Login(usuario, senha) == False: return
    initializeWrite()
    for mensagem in mensagens:
        encryptedText = encryptMessage(usuario, senha, mensagem)
        saveNewLine(encryptedText)

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

print(criptografar('MariaSilva', 'SenhaFort3!', ['ISTO E UM TESTE 1','ISTO E UM TESTE 2', 'ISTO E UM TESTE 3','ISTO E UM TESTE 4','ISTO E UM TESTE 5']))
print(descriptografar('MariaSilva', 'SenhaFort3!', True))