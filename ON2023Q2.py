'''
FUNCTION IterativeCalculate(Number : INTEGER) RETURNS INTEGER
    DECLARE Total : Integer
    DECLARE ToFind : Integer
    ToFind ← Number
    Total ← 0
    WHILE Number <> 0
        IF ToFind MODULUS Number = 0 THEN
            Total ← Total + Number
        ENDIF
        Number ← Number - 1
    ENDWHILE
    RETURN Total
ENDFUNCTION
'''

def IterativeCalculate(number):
    ToFind = number
    Total = 0
    while number != 0:
        if (ToFind % number) == 0:
            Total += number
        number -= 1
    return Total

print(IterativeCalculate(10))

# recursive code
def RecursiveCalculate(number,ToFind):
    if number == 0:
        return 0
    else:
        if (ToFind % number ) == 0:
            total = number + RecursiveCalculate(number-1,ToFind)
        else:
            return(RecursiveCalculate(number-1,ToFind))
    return total

print(RecursiveCalculate(10,10))
