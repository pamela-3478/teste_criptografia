def validaUsuario(usuario):
    try:
        valid = True
        if not usuario:valid = False
        if len(usuario) > 30: valid = False
        if " " in usuario: valid = False
        if not usuario[0].isupper(): valid = False
        if contemNumeros(usuario): valid = False
        if contemCaracteresEspeciais(usuario): valid = False
        return valid
    except:
        return False

def validaSenha(senha = ''):
    valid = True
    senha = str(senha)
    if len(senha) < 10:
        valid = False
    if not contemCaracteresEspeciais(senha):
        valid = False
    if not contemMaiscula(senha) or not contemMinuscula(senha):
        valid = False
    return valid

def contemNumeros(texto = ''):
    return any(indice.isdigit() for indice in texto)

def contemCaracteresEspeciais(texto = ''):
    simbolos = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")
    for char in texto:
        if char in simbolos: return True
    return False

def contemMaiscula(texto = ''):
    try:
        return any(indice.isupper() for indice in texto)
    except:
        return False

def contemMinuscula(texto = ''):
    try:
        return any(indice.islower() for indice in texto)
    except:
            return False

print(validaUsuario("UsuarioComTudo123@A"))