consonants = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ']
eng_kor_map = {'a': 'ㅁ', 'b': 'ㅠ', 'c': 'ㅊ', 'd': 'ㅇ', 'e': 'ㄷ', 'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'i': 'ㅑ', 'j': 'ㅓ', 'k': 'ㅏ', 'l': 'ㅣ', 'm': 'ㅡ', 'n': 'ㅜ', 'o': 'ㅐ', 'p': 'ㅔ', 'q': 'ㅂ', 'r': 'ㄱ', 's': 'ㄴ', 't': 'ㅅ', 'u': 'ㅕ', 'v': 'ㅍ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', 'Q': 'ㅃ', 'W': 'ㅉ', 'E': 'ㄸ', 'R': 'ㄲ', 'T': 'ㅆ', 'O': 'ㅒ', 'P': 'ㅖ'}
q01 = {'ㄱ': False, 'ㄴ': False, 'ㄷ': False, 'ㄹ': False, 'ㅁ': False, 'ㅂ': False, 'ㅅ': False, 'ㅇ': False, 'ㅈ': False, 'ㅊ': False, 'ㅋ': False, 'ㅌ': False, 'ㅍ': False, 'ㅎ': False, 'ㄲ': False, 'ㄸ': False, 'ㅃ': False, 'ㅆ': False, 'ㅉ': False, 'ㅏ': 4, 'ㅑ': 4, 'ㅐ': 5, 'ㅒ': 5, 'ㅓ': 4, 'ㅕ': 4, 'ㅔ': 5, 'ㅖ': 5, 'ㅗ': 2, 'ㅛ': 5, 'ㅜ': 3, 'ㅠ': 5, 'ㅡ': 4, 'ㅣ': 5}
q02 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': 4, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': False, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': 5}
q03 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': False, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': 4, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': 5}
q04 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': False, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': False, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': 5}
q05 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': False, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': False, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': False}
q06 = {'ㄱ': 1, 'ㄴ': 1, 'ㄷ': 1, 'ㄹ': 1, 'ㅁ': 1, 'ㅂ': 1, 'ㅅ': 9, 'ㅇ': 1, 'ㅈ': 1, 'ㅊ': 1, 'ㅋ': 1, 'ㅌ': 1, 'ㅍ': 1, 'ㅎ': 1, 'ㄲ': 1, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 1, 'ㅉ': 1, 'ㅏ': 4, 'ㅑ': 4, 'ㅐ': 5, 'ㅒ': 5, 'ㅓ': 4, 'ㅕ': 4, 'ㅔ': 5, 'ㅖ': 5, 'ㅗ': 2, 'ㅛ': 5, 'ㅜ': 3, 'ㅠ': 5, 'ㅡ': 4, 'ㅣ': 5}
q00 = {'ㄱ': 1, 'ㄴ': 1, 'ㄷ': 1, 'ㄹ': 1, 'ㅁ': 1, 'ㅂ': 1, 'ㅅ': 1, 'ㅇ': 1, 'ㅈ': 1, 'ㅊ': 1, 'ㅋ': 1, 'ㅌ': 1, 'ㅍ': 1, 'ㅎ': 1, 'ㄲ': 1, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 1, 'ㅉ': 1}
q00 = {'ㄱ': 1, 'ㄴ': 1, 'ㄷ': 1, 'ㄹ': 1, 'ㅁ': 1, 'ㅂ': 1, 'ㅅ': 1, 'ㅇ': 1, 'ㅈ': 1, 'ㅊ': 1, 'ㅋ': 1, 'ㅌ': 1, 'ㅍ': 1, 'ㅎ': 1, 'ㄲ': 1, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 1, 'ㅉ': 1}
q00 = {'ㄱ': 1, 'ㄴ': 1, 'ㄷ': 1, 'ㄹ': 1, 'ㅁ': 1, 'ㅂ': 1, 'ㅅ': 1, 'ㅇ': 1, 'ㅈ': 1, 'ㅊ': 1, 'ㅋ': 1, 'ㅌ': 1, 'ㅍ': 1, 'ㅎ': 1, 'ㄲ': 1, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 1, 'ㅉ': 1}
q00 = {'ㄱ': 1, 'ㄴ': 1, 'ㄷ': 1, 'ㄹ': 1, 'ㅁ': 1, 'ㅂ': 1, 'ㅅ': 1, 'ㅇ': 1, 'ㅈ': 1, 'ㅊ': 1, 'ㅋ': 1, 'ㅌ': 1, 'ㅍ': 1, 'ㅎ': 1, 'ㄲ': 1, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 1, 'ㅉ': 1}
state_transition_tab = [q00, q01, q02, q03, q04, q05, q06, q07, q08, q09, q10]


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

#def action_func(q, sigma):

eng_in = input()
kor_out = []
for letter in eng_in: 
    kor_out.append(eng_to_kor(letter))
print(''.join(kor_out))
