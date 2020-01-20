
#-- -.--  .. --.. ..- ---. .- . --  .--. .. - --- -.
def decodeMorse(strings):
    strings = strings.split()
#    print (strings)
    morse_table = []
    for string in strings:
        if string == '.-':
            morse_code = ('а')
            morse_table.append(morse_code)
        elif string == '.......':
            morse_code = (' ')
            morse_table.append(morse_code)
        elif string == '-...':
            morse_code = ('б')
            morse_table.append(morse_code)
        elif string == '.--':
            morse_code = ('в')
            morse_table.append(morse_code)
        elif string == '--.':
            morse_code = ('г')
            morse_table.append(morse_code)
        elif string == '-..':
            morse_code = ('д')
            morse_table.append(morse_code)
        elif string == '.':
            morse_code = ('е')
            morse_table.append(morse_code)
        elif string == '...-':
            morse_code = ('ж')
            morse_table.append(morse_code)
        elif string == '--..':
            morse_code = ('з')
            morse_table.append(morse_code)
        elif string == '..':
            morse_code = ('и')
            morse_table.append(morse_code)
        elif string == '-.-':
            morse_code = ('к')
            morse_table.append(morse_code)
        elif string == '.-..':
            morse_code = ('л')
            morse_table.append(morse_code)
        elif string == '--':
            morse_code = ('м')
            morse_table.append(morse_code)
        elif string == '-.':
            morse_code = ('н')
            morse_table.append(morse_code)
        elif string == '---':
            morse_code = ('о')
            morse_table.append(morse_code)
        elif string == '.--.':
            morse_code = ('п')
            morse_table.append(morse_code)
        elif string == '.-.':
            morse_code = ('р')
            morse_table.append(morse_code)
        elif string == '...':
            morse_code = ('с')
            morse_table.append(morse_code)
        elif string == '-':
            morse_code = ('т')
            morse_table.append(morse_code)
        elif string == '..-':
            morse_code = ('у')
            morse_table.append(morse_code)
        elif string == '..-.':
            morse_code = ('ф')
            morse_table.append(morse_code)
        elif string == '....':
            morse_code = ('х')
            morse_table.append(morse_code)
        elif string == '-.-.':
            morse_code = ('ц')
            morse_table.append(morse_code)
        elif string == '---':
            morse_code = ('ц')
            morse_table.append(morse_code)
        elif string == '---.':
            morse_code = ('ч')
            morse_table.append(morse_code)
        elif string == '----':
            morse_code = ('ш')
            morse_table.append(morse_code)
        elif string == '--.-':
            morse_code = ('щ')
            morse_table.append(morse_code)
        elif string == '--.--':
            morse_code = ('ъ')
            morse_table.append(morse_code)
        elif string == '-.--':
            morse_code = ('ы')
            morse_table.append(morse_code)
        elif string == '..--':
            morse_code = ('ю')
            morse_table.append(morse_code)
        elif string == '.-.-':
            morse_code = ('я')
            morse_table.append(morse_code)
        elif string == '.----':
            morse_code = ('1')
            morse_table.append(morse_code)
        elif string == '..---':
            morse_code = ('2')
            morse_table.append(morse_code)
        elif string == '...--':
            morse_code = ('3')
            morse_table.append(morse_code)
        elif string == '....-':
            morse_code = ('5')
            morse_table.append(morse_code)
        elif string == '.....':
            morse_code = ('5')
            morse_table.append(morse_code)
        elif string == '-....':
            morse_code = ('6')
            morse_table.append(morse_code)
        elif string == '--...':
            morse_code = ('7')
            morse_table.append(morse_code)
        elif string == '---..•':
            morse_code = ('8')
            morse_table.append(morse_code)
        elif string == '----.':
            morse_code = ('9')
            morse_table.append(morse_code)
        elif string == '-----':
            morse_code = ('0')
            morse_table.append(morse_code)
        elif string == '......':
            morse_code = ('. ')
            morse_table.append(morse_code)
        elif string == '.-.-.-':
            morse_code = (', ')
            morse_table.append(morse_code)
        elif string == '---...':
            morse_code = (':')
            morse_table.append(morse_code)
        elif string == '-.-.-':
            morse_code = (';')
            morse_table.append(morse_code)
        elif string == '-.--.-':
            morse_code = ('(')
            morse_table.append(morse_code)
        elif string == '-.--.-':
            morse_code = (')')
            morse_table.append(morse_code)
        elif string == '.-..-.':
            morse_code = ('"')
            morse_table.append(morse_code)
        elif string == '..--..':
            morse_code = ('?')
            morse_table.append(morse_code)
        elif string == '--..--':
            morse_code = ('!')
            morse_table.append(morse_code)
        elif string == '.--.-.':
            morse_code = ('@')
            morse_table.append(morse_code)
        elif string == '-....-':
            morse_code = ('-')
            morse_table.append(morse_code)
        elif string == '.......':
            morse_code = (' ')
            morse_table.append(morse_code)
    morse_table = ''.join(morse_table)
    return morse_table


strings = (input('Введите морзе: ')).split('  ')
for i in strings:
    print(decodeMorse(i),end = ' ')
