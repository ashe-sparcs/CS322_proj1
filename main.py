consonants = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ']
eng_kor_map = {'a': 'ㅁ', 'b': 'ㅠ', 'c': 'ㅊ', 'd': 'ㅇ', 'e': 'ㄷ', 'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'i': 'ㅑ', 'j': 'ㅓ', 'k': 'ㅏ', 'l': 'ㅣ', 'm': 'ㅡ', 'n': 'ㅜ', 'o': 'ㅐ', 'p': 'ㅔ', 'q': 'ㅂ', 'r': 'ㄱ', 's': 'ㄴ', 't': 'ㅅ', 'u': 'ㅕ', 'v': 'ㅍ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', 'Q': 'ㅃ', 'W': 'ㅉ', 'E': 'ㄸ', 'R': 'ㄲ', 'T': 'ㅆ', 'O': 'ㅒ', 'P': 'ㅖ'}
q01 = {'ㄱ': False, 'ㄴ': False, 'ㄷ': False, 'ㄹ': False, 'ㅁ': False, 'ㅂ': False, 'ㅅ': False, 'ㅇ': False, 'ㅈ': False, 'ㅊ': False, 'ㅋ': False, 'ㅌ': False, 'ㅍ': False, 'ㅎ': False, 'ㄲ': False, 'ㄸ': False, 'ㅃ': False, 'ㅆ': False, 'ㅉ': False, 'ㅏ': 4, 'ㅑ': 4, 'ㅐ': 5, 'ㅒ': 5, 'ㅓ': 4, 'ㅕ': 4, 'ㅔ': 5, 'ㅖ': 5, 'ㅗ': 2, 'ㅛ': 5, 'ㅜ': 3, 'ㅠ': 5, 'ㅡ': 4, 'ㅣ': 5}
q02 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': 4, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': False, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': 5}
result = []


def eng_to_kor(eng): 
    return eng_kor_map[eng]

def state_transition_func(q, sigma):
    if q == 0:
        if sigma in consonants:
            return 1
        else:
            return False
    elif q == 1:
        if sigma in consonants:
            return False
        else:
            return q01[sigma]
    elif q == 2:
        if sigma in consonants:
            return q02[sigma]
        elif sigma == 'ㅏ':
            return 4
        elif sigma == 'ㅣ':
            return 5
        else:
            return False
    elif q == 3:
        if sigma in consonants:
            return q02[sigma]
        elif sigma == 'ㅓ':
            return 4
        elif sigma == 'ㅣ':
            return 5
        else:
            return False
    elif q == 4:
        if sigma in consonants:
            return q02[sigma]
        elif sigma == 'ㅣ':
            return 5
        else:
            return False
    elif q == 5:
        if sigma in consonants:
            return q02[sigma]
        else:
            return False
    elif q == 6:
        if sigma == 'ㅅ':
            return 9
        elif sigma in consonants:
            return 1
        else:
            return q01[sigma]
    elif q == 7:
        if sigma == 'ㅈ' or sigma == 'ㅎ':
            return 9
        elif sigma in consonants:
            return 1
        else:
            return q01[sigma]
    elif q == 8:
        if sigma in ['ㄱ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅌ', 'ㅍ', 'ㅎ']:
            return 9
        elif sigma in consonants:
            return 1
        else:
            return q01[sigma]
    elif q == 9:
        if sigma in consonants:
            return 1
        else:
            return q01[sigma]
    else:
        if sigma in consonants:
            return 1
        else:
            return q01[sigma]


def action_func(q, sigma):
    if q == 0:
        if sigma in consonants:
            result.append([sigma, '', ''])
        else:
            return False
    elif q == 1:
        if sigma in consonants:
            return False
        else:
            result[-1][1] = sigma
    elif q == 2:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
        elif sigma in consonants:
            result[-1][2] = sigma  # batchim first
            #result.append([sigma, '', ''])  # chosung first
        elif sigma in ['ㅏ', 'ㅣ']:
            result[-1][1] = result[-1][1] + sigma
        else:
            return False
    elif q == 3:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
        elif sigma in consonants:
            result[-1][2] = sigma  # batchim first
            #result.append([sigma, '', ''])  # chosung first
        elif sigma in ['ㅓ', 'ㅣ']:
            result[-1][1] = result[-1][1] + sigma
        else:
            return False
    elif q == 4:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
        elif sigma in consonants:
            result[-1][2] = sigma  # batchim first
            #result.append([sigma, '', ''])  # chosung first
        elif sigma == 'ㅣ':
            result[-1][1] = result[-1][1] + sigma
        else:
            return False
    elif q == 5:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
        elif sigma in consonants:
            result[-1][2] = sigma  # batchim first
            #result.append([sigma, '', ''])  # chosung first
        else:
            return False
    elif q == 6:
        if sigma == 'ㅅ':
            # batchim first
            result[-1][2] = result[-1][2] + sigma
            # chosung first
            #result[-2][2] = result[-1][0]
            #result[-1][0] = sigma
        elif sigma in consonants:
            # batchim first
            result.append([sigma, '', ''])
            # chosung first
            ##
        else:
            # batchim first
            result[-1][2] = ''
            result.append(['ㄱ', sigma, ''])
            # chosung first
            #result[-1][1] = sigma
    elif q == 7:
        if sigma in ['ㅈ', 'ㅎ']:
            # batchim first
            result[-1][2] = result[-1][2] + sigma
            # chosung first
            #result[-2][2] = result[-1][0]
            #result[-1][0] = sigma
        elif sigma in consonants:
            # batchim first
            result.append([sigma, '', ''])
            # chosung first
            ##
        else:
            # batchim first
            result[-1][2] = ''
            result.append(['ㄱ', sigma, ''])
            # chosung first
            #result[-1][1] = sigma
    elif q == 8:
        if sigma in ['ㄴ', 'ㄷ', 'ㄹ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ']:
            # batchim first
            result.append([sigma, '', ''])
            # chosung first
            ##
        elif sigma in consonants:
            # batchim first
            result[-1][2] = result[-1][2] + sigma
            # chosung first
            #result[-2][2] = result[-1][0]
            #result[-1][0] = sigma
        else:
            # batchim first
            result[-1][2] = ''
            result.append(['ㄱ', sigma, ''])
            # chosung first
            #result[-1][1] = sigma
    elif q == 10:
        if sigma in consonants:
            result[-2][2] = result[-2][2] + result[-1][0]
            result[-1][0] = sigma
        else:
            result.append([result[-1][2][-1], sigma, ''])
            result[-2][2] = ''
            #result.append([result[-1][2], sigma, ''])
    else:
        if sigma in consonants:
            # batchim first
            result.append([sigma, '', ''])
            # chosung first
            ##
        else:
            # batchim first
            result.append([result[-1][2][-1], sigma, ''])
            result[-2][2] = result[-2][2][0]
            # chosung first
            #result[-1][1] = sigma

eng_in = input()
kor_in = []
for letter in eng_in: 
    kor_in.append(eng_to_kor(letter))

q = 0
for letter in kor_in:
    action_func(q, letter)
    q = state_transition_func(q, letter)
print(result)
print(kor_in)
