import json

def buscar_curso(instituicoes, cep):
    cursos_nome = []
    cursos_oferta = []
    for instituicao in instituicoes:
        if instituicao['endereco']['cep'] == cep:
            for curso in instituicao['cursos']:
                cursos_nome.append(curso['nome'])
                cursos_oferta.append(curso['tipo_oferta'])
    for nome in cursos_nome:
        for oferta in cursos_oferta:
            print('{} >> {}'.format(nome,oferta))
            break


with open('LNPG/instituicoes-AL.json') as json_file:
    data = json.load(json_file)
    instituicoes = data['instituicoes']


buscar_curso(instituicoes, '57300-085')

'''
    for instituicao in instituicoes:
        print('-------------------------------------------------------------')
        print(instituicao['nome'])
        if 'telefone1' in instituicao:
            print(instituicao['telefone1'])
        if 'telefone2' in instituicao:
            print(instituicao['telefone2'])
        if 'email' in instituicao:
            print(instituicao['email'])
        print(instituicao['endereco']['municipio'])
        print('------------------------------------------------------------')
'''