#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    tot = 0 #Variavel que armazena a contagem geral
    
    for i in s: #Repetidor para contagem dos as
        
        if i == 'a':
            
            tot += 1
    
    tot = n//len(s) * tot #Calculo para com a contagem da variavel N dada 
    
    for i in s[:n % len(s)]: #Repetidor para checagem de tamanho LEN da string fornecida
                             #Repetir ate o Length desejado
        if i == 'a': #Variavel tot recebendo a contagem dos as adicionados pela repeticao
            
            tot += 1
        
    return tot 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
