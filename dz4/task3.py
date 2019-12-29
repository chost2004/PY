import ast
'''

'''

s = ast.literal_eval(input('Введите данные: '))
report = []
fiveInOne = ['8 weeks', '12 weeks', '16 weeks']
#Protects against: diphtheria, tetanus, whooping cough, polio and Hib (Haemophilus influenzae type b)
pneumococcal = ['8 weeks', '16 weeks']
#Protects against: some types of pneumococcal infection
rotavirus = ['8 weeks', '12 weeks']
#Protects against: rotavirus infection, a common cause of childhood diarrhoea and sickness
meningitisB = ['8 weeks', '16 weeks', '12 months']
#Protects against: meningitis caused by meningococcal type B bacteria
hibMenC = ['12 months']
#Protects against: Haemophilus influenzae type b (Hib), meningitis caused by meningococcal group C bacteria    
measlesMumpsRubella = ['12 months', '40 months']
#Protects against: measles, mumps and rubella
fluVaccine = ['september', 'october', 'november']
#Given at: annually in Sept/Oct
preSchoolBooster = ['40 months']
#Protects against: diphtheria, tetanus, whooping cough and polio

if s[0] in fiveInOne or s[1] in fiveInOne:
    report.append('fiveInOne')
if s[0] in pneumococcal or s[1] in pneumococcal:
    report.append('pneumococcal')
if s[0] in rotavirus or s[1] in rotavirus:
    report.append('rotavirus')
if s[0] in meningitisB or s[1] in meningitisB:
    report.append('meningitisB')
if s[0] in hibMenC or s[1] in hibMenC:
    report.append('hibMenC')
if s[0] in measlesMumpsRubella or s[1] in measlesMumpsRubella:
    report.append('measlesMumpsRubella')
if s[0] in preSchoolBooster or s[1] in preSchoolBooster:
    report.append('preSchoolBooster')
if s[2] in fluVaccine:
    report.append('offer fluVaccine')
report.sort()
print (report)
  
  
    



