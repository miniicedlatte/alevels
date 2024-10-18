'''
FUNCTION IterativeVowels(Value : STRING) RETURNS INTEGER
    DECLARE Total : INTEGER
    DECLARE LengthString : INTEGER
    DECLARE FirstCharacter : CHAR
    Total ← 0
    LengthString ← LENGTH(Value)
    FOR X ← 0 TO LengthString - 1
        FirstCharacter ← MID(Value, 0, 1)
        IF FirstCharacter = 'a' OR FirstCharacter = 'e' OR
             FirstCharacter = 'i' OR FirstCharacter = 'o' OR
             FirstCharacter = 'u' THEN
             Total ← Total + 1
        ENDIF
        Value ← MID(Value, 1, LENGTH(Value)-1)
    NEXT X
 RETURN Total
ENDFUNCTION
'''

def IterativeVowels(value):
    total = 0
    lengthString = len(value)

    for i in range(lengthString):
        firstChar = value[0:1]
        #if firstChar in ('aieou')
        if firstChar == 'a' or firstChar == 'e' or firstChar == 'i' or firstChar == 'o' or firstChar == 'u' :
            total += 1
        value = value[1:len(value)]

    return total

print(IterativeVowels("areeba"))

#convert to recursive function

def RecursiveVowels(value) :
    length = len(value)

    if length == 0:
        return 0
    else:
        char = value[0:1]
        if char in ("aeiou"):
            total = 1 + RecursiveVowels(value[1:length])
        else:
            total = RecursiveVowels(value[1:length])

    return total

print(RecursiveVowels("house"))
