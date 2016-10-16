eng_kor_map = {'a': 'ㅁ', 'b': 'ㅠ', 'c': 'ㅊ', 'd': 'ㅇ', 'e': 'ㄷ', 'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'i': 'ㅑ', 'j': 'ㅓ', 'k': 'ㅏ', 'l': 'ㅣ', 'm': 'ㅡ', 'n': 'ㅜ', 'o': 'ㅐ', 'p': 'ㅔ', 'q': 'ㅂ', 'r': 'ㄱ', 's': 'ㄴ', 't': 'ㅅ', 'u': 'ㅕ', 'v': 'ㅍ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', 'Q': 'ㅃ', 'W': 'ㅉ', 'E': 'ㄸ', 'R': 'ㄲ', 'T': 'ㅆ', 'O': 'ㅒ', 'P': 'ㅖ'}


def eng_to_kor(eng): 
    return eng_kor_map[eng]
#def state_transition_func(q, sigma):


#def action_func(q, sigma):

eng_in = input()
kor_out = []
for letter in eng_in: 
    kor_out.append(eng_to_kor(letter))
print(''.join(kor_out))
