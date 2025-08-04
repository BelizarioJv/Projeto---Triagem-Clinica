#importando as funçoes
import functions
#Dicionario com as doenças comuns em posto de saude
diseasesDict= {
    "Hipertençao Arterial(Pressão Alta)": {
        "Causas":  'Alimentação rica em sal, sedentarismo, obesidade, estresse, genética',
        "Tratamento": ['Uso de medicamentos anti-hipertensivos','Acompanhamento regular com médico e aferição da pressão.'],
        'Recomendaçoes':['- Reduzir sal e alimentos ultraprocessados.','Praticar exercícios físicos.','Evitar álcool e cigarro.'],        
        'Riscos:': ['Acidente Vascular Cerebral (AVC).','Infarto do miocárdio.','Insuficiência cardíaca','Doença renal crônica.','Aneurismas'],
        'Sintomas': [ 'dor de cabeça','tontura','visao embaçada','zumbido','palpitaçoes','dor no peito','falta de ar']
    },
    "Diabetes Tipo2": {
        "Causas":'Má alimentação, sedentarismo, obesidade, histórico familiar.,',
        "Tratamento": ['Controle da glicemia com medicamentos ou insulina','Dieta equilibrada e atividade física.'],
        'Recomendaçoes':['Monitorar níveis de açúcar no sangue.','Evitar doces e carboidratos refinados','Manter acompanhamento com nutricionista e médico.'],
        'Riscos:': ['Doenças cardiovasculares (infarto, AVC).','Retinopatia diabética (pode causar cegueira)','Nefropatia (problemas nos rins).','- Neuropatia (danos nos nervos, especialmente nos pés).'],
        'Sintomas':['sede','urinando muito','fome exagerada','cansaço','visao turva','feridas demorando a cicatrizar','infecçoes','Formigamento','dormencia']
    },
    "Infecções Respiratórias (como gripe, resfriado, bronquite)": {
        "Causas":  'Vírus ou bactérias, mudanças climáticas, exposição à poluição.',
        "Tratamento": ['Analgésicos, antitérmicos, antibióticos (se bacteriana).','Repouso e hidratação.'],
        'Recomendaçoes':['Vacinação (ex: contra gripe)','Lavar as mãos com frequência.','Evitar locais fechados e aglomerados.'],
        'Riscos:': ['Pneumonia (especialmente em idosos e imunossuprimidos).','Crises de asma ou bronquite crônica.','Complicações cardíacas em pessoas com doenças pré-existentes.','Hospitalização em casos graves.'],
        'Sintomas': ['febre','tosse','dor de garganta','coriza','espirros','dor no corpo','cansaço','dificuldade para respirar']
    },
    "Gastroenterites(diarreia e vômitos)": {
        "Causas":  'Contaminação por alimentos ou água, vírus, bactérias.',
        "Tratamento": ['Reidratação oral (soro caseiro ou industrializado).','Medicamentos para aliviar sintomas.'],
        'Riscos:': ['Desidratação severa, especialmente em crianças e idosos.','Desequilíbrio eletrolítico.','Complicações renais em casos prolongados.','Infecções sistêmicas se não tratadas adequadamente'],
        'Sintomas': ['diarreia','vomitos','febre','mal estar','desidrataçao']
    },
    "Dengue": {
        "Causas":  'Picada do mosquito Aedes aegypti infectado',
        "Tratamento": ['Hidratação intensa.','- Controle da febre e dor com medicamentos.'],
        'Recomendaçoes':['Eliminar focos de água parada.','Usar repelente e telas de proteção.','Procurar atendimento ao primeiro sinal de febre alta e dor no corpo.'],
        'Riscos:': ['Dengue hemorrágica (sangramentos e risco de morte).','Choque hipovolêmico (queda brusca da pressão)','Desidratação grave que pode sobrecarregar o coração.','Maior risco em pessoas com diabetes, hipertensão ou imunossuprimidas'],
        'Sintomas': ['febre','dor nas articulaçoes','dor nos olhos','manchas na pele','nauseas','cansaço','sangramento']
    }
}
#Dicionario com os medicos em plantão
doctorsDict = {
    "MEDICO 1": {
       "Nome": "Doutor luiz",
        "Pacientes": []
    },
    "MEDICO 2": {
        "Nome": "Doutora Andrea",
        "Pacientes": [],
    },
    "MEDICO 3":{
        "Nome":"Doutor Antonio",
        "Pacientes":[],
    }
}
#Inicio do programa
functions.nameHospital()
print('-', (' '*30) ,'-')
print('PROCESSO DE TRIGEM')
print('-', (' '*10) ,'-')
print('1 - NOVO PACIENTE')
print('2 - VER PATIENTES EM ESPERA')
print('3 - TROCAR DOUTOR EM EXPEDIENTE')
print('4 - FINALIZAR O PROGRAMA')
print('-', (' '*30) ,'-')
while True :
        whichOperation = input('QUAL OPERACAO DESEJA FAZER: (1,2,3 ou 4): ').lower().strip()
        if whichOperation == '1':
            nome, idade, email, telefone, endereco = functions.registerPatients()
            sintomas = functions.askSinsomes()
            doenca = functions.checkSymptoms(sintomas,diseasesDict)
            doctorsDict, doutor = functions.doctorTransfer(doctorsDict, nome)
            functions.diagnosticResult(nome, idade, email, telefone, endereco, doenca, doutor)

        elif whichOperation == '2':
            print('Pacientes em espera:')
            for medico in doctorsDict:
                print(f"{doctorsDict[medico]['Nome']}: {doctorsDict[medico]['Pacientes']}")

        elif whichOperation == '3':
            functions.switchDoctor(doctorsDict)

        elif whichOperation == '4':
            print('Programa finalizado.')
            break

        else:
            print('Opção inválida. Tente novamente.')
