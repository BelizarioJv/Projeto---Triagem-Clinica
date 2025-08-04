
#Funçao para chamar o nome do posto
def nameHospital ():
    print('*' *50)
    print('-', (' '*50) ,'-')
    print(('-'*10) ,'POSTO DE SAUDE BELIZARIO' ,('-'*10))
    print('-', (' '*50) ,'-')
    print('*' *50)

#funçao para pergunta os sintomas do paciente e pergunta se tem mais algum sintoma ate que tenha um digito valido
def askSinsomes():
    sinsomesUserList = []
    while True:
        sinsomesUser = input('Digite o sintoma do paciente: ').lower().strip()
        sinsomesUserList.append(sinsomesUser)

        anothersisome = input('Paciente tem outro sintoma? sim(s) ou nao(n): ').strip().lower()
        while anothersisome != 's' and anothersisome != 'n':
            print('Digite errado.')
            anothersisome = input('Paciente tem outro sintoma? sim(s) ou nao(n): ').strip().lower()

        if anothersisome == 'n':
          break
    print('Lista de sintomas do paciente:', sinsomesUserList)
    return sinsomesUserList


# Funçao para verificar doenças no dicionario 
def checkSymptoms(sinsomesUserList,diseasesDict):
    diagnosticos = []
    for disease in diseasesDict:
        sintomasDaDoenca = set(diseasesDict[disease]['Sintomas'])
        if set(sinsomesUserList).issubset(sintomasDaDoenca):
            print(f'Os sintomas informados indicam: {disease}')
            print('-', (' '*50) ,'-')
            diagnosticos.append(disease)
    if diagnosticos:
        return diagnosticos
    else:
        print('Nenhuma doença correspondente encontrada.')
        return ['Diagnóstico não definido']



#Funçao para cadastrar paciente
def registerPatients ():
    while True:
        namePatient = input('Digite o nome do paciente: ').strip()
        agePatient = input('Digite a idade do paciente: ').strip()
        emailPatient = input('Digite o email do paciente: ').strip()
        numberPatient = input('Digite o numero de telefone do paciente: ').strip()
        patientAddress = input('Digite o endereço do paciente: ').strip()
        print('-', (' '*50) ,'-')
        if '' in [namePatient, agePatient, emailPatient, numberPatient,patientAddress]:
         print('Algum campo está vazio, por favor preencha todos!')
        else :
            return[namePatient,agePatient,emailPatient,numberPatient,patientAddress]

#Funçao para ver os medicos na clinica e qual vai atender o paciente:
def doctorTransfer (doctorsDict,namePatient):
       print(doctorsDict)
       choosedDoctor = ''
       whichDoctor = int(input('Digite para qual medico transferir:(1,2 ou 3)'))
       if whichDoctor == 1:
           choosedDoctor = doctorsDict['MEDICO 1']['Nome']
           doctorsDict["MEDICO 1"]["Pacientes"].append(namePatient)
       elif whichDoctor == 2 :
           choosedDoctor = doctorsDict['MEDICO 2']['Nome']
           doctorsDict["MEDICO 2"]["Pacientes"].append(namePatient)
       elif whichDoctor == 3 :
           choosedDoctor = doctorsDict['MEDICO 3']['Nome']
           doctorsDict["MEDICO 3"]["Pacientes"].append(namePatient)
       else:
           print('Digito Invalido')
       return doctorsDict , choosedDoctor
     
#Funçao para dar o diagnostico e transferir para o doutor com menos paciente esperando atendimento
def diagnosticResult (namePatient,agePatient,emailPatient,numberPatiente,patientAddres,disease,whichDoctor):
   print('-', (' '*50) ,'-')
   print(f'Paciente = {namePatient}')
   print(f'Idade = {agePatient}')
   print(f'Email = {emailPatient}')
   print(f'Numero telefone = {numberPatiente}')
   print(f'Paciente = {patientAddres}')
   print(f'Sintomas para: {disease}')
   print(f'Encaminhamento para o doutor: {whichDoctor}')
   print('-', (' '*50) ,'-')
   

#Funçao para trocar medicos de plantão3
def switchDoctor (doctorsDict):
    print(F'OS MEDICOS EM PLANTAO SÃO OS:')
    print(doctorsDict)
    chooseDoctor = int(input('Digite qual doutor deseja trocar'))
    doctorName = input('Digite o nome do doutor que irá substituir:')
    if chooseDoctor == 1 : 
        doctorsDict['MEDICO 1']["Pacientes"].clear()
        doctorsDict['MEDICO 1']['Nome'] = doctorName
    elif chooseDoctor == 2: 
        doctorsDict['MEDICO 2']["Pacientes"].clear()
        doctorsDict['MEDICO 2']['Nome'] = doctorName
    elif chooseDoctor == 3 : 
        doctorsDict['MEDICO 3']["Pacientes"].clear()
        doctorsDict['MEDICO 3']['Nome'] = doctorName
    else:
        print('Digito invalido')
    return doctorsDict



        

       
        
       


   




  