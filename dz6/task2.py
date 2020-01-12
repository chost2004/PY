'''
Next Version
You're fed up about changing the version of your software manually.
Instead, you will create a little script that will make it for you.
Exercice
Create a function nextVersion, that will take a string in parameter,
and will return a string containing the next version number.
For example:
nextVersion("1.2.3") === "1.2.4";
nextVersion("0.9.9") === "1.0.0";
nextVersion("1") === "2";
nextVersion("1.2.3.4.5.6.7.8") === "1.2.3.4.5.6.7.9";
nextVersion("9.9") === "10.0";
Rules
All numbers, except the first one, must be lower than 10: if there are,
you have to set them to 0 and increment the next number in sequence.


'''
Version = []
for x in (input("Введите версию: ")).split('.'):
    Version.append(int(x))


def nextVersion(ver):
    i = len(ver) - 1
    up = 0
    if i == 0:
        ver[0] += 1
        return ver
    while i >= 0:
        if (ver[i] in range (9)) and (i == len(ver) - 1):
            ver[i] += 1
            break
        if (ver[i] == 9) and (i == len(ver) - 1):
            ver[i] = 0
            up = 1
        elif i == 0 and up:
            ver[i] += 1
        elif ver[i] == 9 and up:
            ver[i] = 0
        elif (ver[i] in range (9)) and up:
            ver[i] += 1
            up = 0
        elif not up:
            break
        i -=1
    return (ver)
Version = nextVersion(Version)
result = []
for x in Version:
    result.append(str(x))
print ('.'.join(result))

    
