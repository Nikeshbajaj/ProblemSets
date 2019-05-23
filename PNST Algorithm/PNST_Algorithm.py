# Author  :: Nikesh Bajaj
# Contact :: http://nikeshbajaj.in, bajaj.nikkey@gmail.com
# PNST Algorithm:: Properly Nested String Test

def PNST(S,verbose=False):
    '''
    PNST Algorithm- Properly Nested String Test
    Test whether given string S is propoerly nested or not, 
    given that S contains only following characters: '"(", "{", "[", "]", "}" ")" or empty
    
    if S contains any alpha nuemeric characters, it can be removed easily before applying PNST algo    
    
    Input
    -------
    S : string - input string to be tested         
    verbose: bool -  vverbosity of tests at each iteration
    
    Output
    -------
    test: Bool - True if string S is properly nasted else False
    
    '''
    N = len(S)
    if verbose: print('S: ',S, ' Length: ',N )
    S =S.replace('[]','').replace('()','').replace('{}','')
    if verbose: print(S)
    test = False
    while not(test):
        S1 = S
        S =S.replace('[]','').replace('()','').replace('{}','')
        if verbose: print(S1,S)
        if S==S1:
            test =True
    test=True if len(S)==0 else False
            
    if verbose: print('Solution',test,S,S1,len(S),len(S1))
    
    return test
