import sys
import traceback
consonants = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅗㅏ', 'ㅗㅐ', 'ㅗㅣ', 'ㅛ', 'ㅜ', 'ㅜㅓ', 'ㅜㅔ', 'ㅜㅣ', 'ㅠ', 'ㅡ', 'ㅡㅣ', 'ㅣ']
# jung = ['ㅏ', 'ㅐ' 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jong = ['', 'ㄱ', 'ㄲ', 'ㄱㅅ', 'ㄴ', 'ㄴㅈ', 'ㄴㅎ', 'ㄷ', 'ㄹ', 'ㄹㄱ', 'ㄹㅁ', 'ㄹㅂ', 'ㄹㅅ', 'ㄹㅌ', 'ㄹㅍ', 'ㄹㅎ', 'ㅁ', 'ㅂ', 'ㅂㅅ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',  'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
eng_kor_map = {'a': 'ㅁ', 'b': 'ㅠ', 'c': 'ㅊ', 'd': 'ㅇ', 'e': 'ㄷ', 'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'i': 'ㅑ', 'j': 'ㅓ', 'k': 'ㅏ', 'l': 'ㅣ', 'm': 'ㅡ', 'n': 'ㅜ', 'o': 'ㅐ', 'p': 'ㅔ', 'q': 'ㅂ', 'r': 'ㄱ', 's': 'ㄴ', 't': 'ㅅ', 'u': 'ㅕ', 'v': 'ㅍ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', 'Q': 'ㅃ', 'W': 'ㅉ', 'E': 'ㄸ', 'R': 'ㄲ', 'T': 'ㅆ', 'O': 'ㅒ', 'P': 'ㅖ'}
q01 = {'ㄱ': False, 'ㄴ': False, 'ㄷ': False, 'ㄹ': False, 'ㅁ': False, 'ㅂ': False, 'ㅅ': False, 'ㅇ': False, 'ㅈ': False, 'ㅊ': False, 'ㅋ': False, 'ㅌ': False, 'ㅍ': False, 'ㅎ': False, 'ㄲ': False, 'ㄸ': False, 'ㅃ': False, 'ㅆ': False, 'ㅉ': False, 'ㅏ': 4, 'ㅑ': 4, 'ㅐ': 5, 'ㅒ': 5, 'ㅓ': 4, 'ㅕ': 4, 'ㅔ': 5, 'ㅖ': 5, 'ㅗ': 2, 'ㅛ': 5, 'ㅜ': 3, 'ㅠ': 5, 'ㅡ': 4, 'ㅣ': 5}
q02 = {'ㄱ': 6, 'ㄴ': 7, 'ㄷ': 10, 'ㄹ': 8, 'ㅁ': 10, 'ㅂ': 6, 'ㅅ': 10, 'ㅇ': 10, 'ㅈ': 10, 'ㅊ': 10, 'ㅋ': 10, 'ㅌ': 10, 'ㅍ': 10, 'ㅎ': 10, 'ㄲ': 10, 'ㄸ': 1, 'ㅃ': 1, 'ㅆ': 10, 'ㅉ': 1, 'ㅏ': 4, 'ㅑ': False, 'ㅐ': False, 'ㅒ': False, 'ㅓ': False, 'ㅕ': False, 'ㅔ': False, 'ㅖ': False, 'ㅗ': False, 'ㅛ': False, 'ㅜ': False, 'ㅠ': False, 'ㅡ': False, 'ㅣ': 5}
state = [0]
result = []
batchim = True
incomplete = []


def eng_to_kor(eng):
    if eng == '<':
        return eng
    else:
        return eng_kor_map[eng]


def state_transition_func(q, sigma):
    global state
    print(q)
    '''
    if sigma == '<':
        if not incomplete or result[-1][1] == '':
            result.pop()
            incomplete.pop()
        else:
            index_temp = 2 - incomplete[-1].count('')
            result[-1][index_temp] = ''
            incomplete[-1][index_temp] = ''
    '''

    if sigma == '<':
        print('incomplete : ')
        print(incomplete)
        if incomplete:
            # delete by part
            # complex rollback
            if result[-1][1] == '':
                result.pop()
                incomplete.pop()
                if batchim:
                    state = [0]
                    return 0
                else:
                    state.pop()
                    if not state:
                        state = [0]
                    return state[-1]
            elif result[-1][2] == '' and len(result[-1][1]) == 1:
                result[-1][1] = ''
                incomplete[-1][1] = ''
                state = [1]
                return 1
            elif result[-1][2] == '' and len(result[-1][1]) == 2:
                result[-1][1] = result[-1][1][0]
                incomplete[-1][1] = incomplete[-1][1][0]
                state.pop()
                return state[-1]
            elif len(result[-1][2]) == 1:
                result[-1][2] = ''
                incomplete[-1][2] = ''
                state.pop()
                return state[-1]
            elif len(result[-1][2]) == 2:
                result[-1][2] = result[-1][2][0]
                incomplete[-1][2] = incomplete[-1][2][0]
                state.pop()
                return state[-1]
            else:
                print('what the fuck?')
                '''
                result[-1][1] = ''
                incomplete[-1][1] = ''
                state.pop()
                return state[-1]
                '''
        else:
            result.pop()
            state = [0]
            return 0

    else:
        if q == 0:
            if sigma in consonants:
                next_state = 1
            else:
                next_state = False
        elif q == 1:
            if sigma in consonants:
                next_state = False
            else:
                next_state = q01[sigma]
        elif q == 2:
            if sigma in consonants:
                next_state = q02[sigma]
            elif sigma in ['ㅏ', 'ㅣ', 'ㅐ']:
                next_state = 5
            else:
                next_state = False
        elif q == 3:
            if sigma in consonants:
                next_state = q02[sigma]
            elif sigma in ['ㅓ', 'ㅣ', 'ㅔ']:
                next_state = 5
            else:
                next_state = False
        elif q == 4:
            if sigma in consonants:
                next_state = q02[sigma]
            elif sigma == 'ㅣ':
                next_state = 5
            else:
                next_state = False
        elif q == 5:
            if sigma in consonants:
                next_state = q02[sigma]
            else:
                next_state = False
        elif q == 6:
            if sigma == 'ㅅ':
                next_state = 9
            elif sigma in consonants:
                next_state = 1
            else:
                next_state = q01[sigma]
        elif q == 7:
            if sigma == 'ㅈ' or sigma == 'ㅎ':
                next_state = 9
            elif sigma in consonants:
                next_state = 1
            else:
                next_state = q01[sigma]
        elif q == 8:
            if sigma in ['ㄱ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅌ', 'ㅍ', 'ㅎ']:
                next_state = 9
            elif sigma in consonants:
                next_state = 1
            else:
                next_state = q01[sigma]
        elif q == 9:
            if sigma in consonants:
                next_state = 1
            else:
                next_state = q01[sigma]
        else:
            if sigma in consonants:
                next_state = 1
            else:
                next_state = q01[sigma]
        state.append(next_state)
        return next_state


def action_func(q, sigma):
    if sigma == '<':
        return
    if q == 0:
        if sigma in consonants:
            result.append([sigma, '', ''])
            incomplete.append([sigma, '', ''])
            if batchim and len(incomplete) > 1:
                incomplete.pop(-2)
            elif not batchim and len(incomplete) > 2:
                incomplete.pop(-3)
        else:
            return False
    elif q == 1:
        if sigma in consonants:
            return False
        else:
            result[-1][1] = sigma
            incomplete[-1][1] = sigma
            if not batchim and len(incomplete) > 1:
                incomplete.pop(-2)
    elif q == 2:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
            incomplete.append([sigma, '', ''])
            if batchim and len(incomplete) > 1:
                incomplete.pop(-2)
            elif not batchim and len(incomplete) > 2:
                incomplete.pop(-3)
        elif sigma in consonants:
            if batchim:
                result[-1][2] = sigma  # batchim first
                incomplete[-1][2] = sigma
            else:
                result.append([sigma, '', ''])  # chosung first
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 2:
                    incomplete.pop(-3)
        elif sigma in ['ㅏ', 'ㅣ', 'ㅐ']:
            result[-1][1] = result[-1][1] + sigma
            incomplete[-1][1] = incomplete[-1][1] + sigma
        else:
            return False
    elif q == 3:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
            incomplete.append([sigma, '', ''])
            if batchim and len(incomplete) > 1:
                incomplete.pop(-2)
            elif not batchim and len(incomplete) > 2:
                incomplete.pop(-3)
        elif sigma in consonants:
            if batchim:
                result[-1][2] = sigma  # batchim first
                incomplete[-1][2] = sigma
            else:
                result.append([sigma, '', ''])  # chosung first
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 2:
                    incomplete.pop(-3)
        elif sigma in ['ㅓ', 'ㅣ', 'ㅔ']:
            result[-1][1] = result[-1][1] + sigma
            incomplete[-1][1] = incomplete[-1][1] + sigma
        else:
            return False
    elif q == 4:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
            incomplete.append([sigma, '', ''])
            if batchim and len(incomplete) > 1:
                incomplete.pop(-2)
            elif not batchim and len(incomplete) > 2:
                incomplete.pop(-3)
        elif sigma in consonants:
            if batchim:
                result[-1][2] = sigma  # batchim first
                incomplete[-1][2] = sigma
            else:
                result.append([sigma, '', ''])  # chosung first
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 2:
                    incomplete.pop(-3)
        elif sigma == 'ㅣ':
            result[-1][1] = result[-1][1] + sigma
            incomplete[-1][1] = incomplete[-1][1] + sigma
        else:
            return False
    elif q == 5:
        if sigma in ['ㄸ', 'ㅃ', 'ㅉ']:
            result.append([sigma, '', ''])
            incomplete.append([sigma, '', ''])
            if batchim and len(incomplete) > 1:
                incomplete.pop(-2)
            elif not batchim and len(incomplete) > 2:
                incomplete.pop(-3)
        elif sigma in consonants:
            if batchim:
                result[-1][2] = sigma  # batchim first
                incomplete[-1][2] = sigma
            else:
                result.append([sigma, '', ''])  # chosung first
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 2:
                    incomplete.pop(-3)
        else:
            return False
    elif q == 6:
        if sigma == 'ㅅ':
            # batchim first
            if batchim:
                result[-1][2] = result[-1][2] + sigma
                incomplete[-1][2] = incomplete[-1][2] + sigma
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        elif sigma in consonants:
            # batchim first
            if batchim:
                result.append([sigma, '', ''])
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        else:
            # batchim first
            if batchim:
                result.append([result[-1][2], sigma, ''])
                result[-2][2] = ''
                incomplete.append([incomplete[-1][2], sigma, ''])
                incomplete[-2][2] = ''
                if len(incomplete) > 1:
                    incomplete.pop(-2)
            # chosung first
            else:
                result[-1][1] = sigma
                incomplete[-1][1] = sigma
                if len(incomplete) > 1:
                    incomplete.pop(-2)
    elif q == 7:
        if sigma in ['ㅈ', 'ㅎ']:
            # batchim first
            if batchim:
                result[-1][2] = result[-1][2] + sigma
                incomplete[-1][2] = incomplete[-1][2] + sigma
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        elif sigma in consonants:
            # batchim first
            if batchim:
                result.append([sigma, '', ''])
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        else:
            # batchim first
            if batchim:
                result[-1][2] = ''
                result.append(['ㄴ', sigma, ''])
                incomplete[-1][2] = ''
                incomplete.append(['ㄴ', sigma, ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-1][1] = sigma
                incomplete[-1][1] = sigma
                if len(incomplete) > 1:
                    incomplete.pop(-2)
    elif q == 8:
        if sigma in ['ㄴ', 'ㄷ', 'ㄹ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ']:
            # batchim first
            if batchim:
                result.append([sigma, '', ''])
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        elif sigma in consonants:
            # batchim first
            if batchim:
                result[-1][2] = result[-1][2] + sigma
                incomplete[-1][2] = incomplete[-1][2] + sigma
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        else:
            # batchim first
            if batchim:
                result[-1][2] = ''
                result.append(['ㄹ', sigma, ''])
                incomplete[-1][2] = ''
                incomplete.append(['ㄹ', sigma, ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-1][1] = sigma
                incomplete[-1][1] = sigma
                if len(incomplete) > 1:
                    incomplete.pop(-2)
    elif q == 10:
        if sigma in consonants:
            # batchim first
            if batchim:
                result.append([sigma, '', ''])
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-2][2] = result[-1][0]
                incomplete[-2][2] = incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        else:
            # batchim first
            if batchim:
                result.append([result[-1][2][-1], sigma, ''])
                result[-2][2] = ''
                incomplete.append([incomplete[-1][2][-1], sigma, ''])
                incomplete[-2][2] = ''
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-1][1] = sigma
                incomplete[-1][1] = sigma
                if len(incomplete) > 1:
                    incomplete.pop(-2)
    else:
        if sigma in consonants:
            # batchim first
            if batchim:
                result.append([sigma, '', ''])
                incomplete.append([sigma, '', ''])
                if len(incomplete) > 1:
                    incomplete.pop(-2)
                ###
            # chosung first
            else:
                result[-2][2] = result[-2][2] + result[-1][0]
                incomplete[-2][2] = incomplete[-2][2] + incomplete[-1][0]
                result[-1][0] = sigma
                incomplete[-1][0] = sigma
        else:
            if batchim:
                result.append([result[-1][2][-1], sigma, ''])
                result[-2][2] = result[-2][2][0]
                incomplete.append([incomplete[-1][2][-1], sigma, ''])
                incomplete[-2][2] = incomplete[-2][2][0]
                if len(incomplete) > 1:
                    incomplete.pop(-2)
            else:
                result[-1][1] = sigma
                incomplete[-1][1] = sigma
                if len(incomplete) > 1:
                    incomplete.pop(-2)

if len(sys.argv) == 2 and (sys.argv[1] == '--chosung' or sys.argv[1] == '-c'):
    batchim = False

while True:
    try:
        print('Type hangul to get right result. Type invalid hangul or ; to exit')
        eng_in = input()
        kor_in = []

        for letter in eng_in:
            kor_in.append(eng_to_kor(letter))

        kor_in_temp = []

        for i in range(len(kor_in)):
            kor_in_temp = kor_in[:i+1]
            current_state = 0
            for letter in kor_in_temp:
                action_func(current_state, letter)
                current_state = state_transition_func(current_state, letter)

            for geulja in result:
                if geulja[1] == '' and geulja[2] == '':
                    print(geulja[0], end='')
                else:
                    print(chr(44032 + 588 * consonants.index(geulja[0]) + 28 * jung.index(geulja[1]) + jong.index(geulja[2])), end=''),
            print('')
            result = []
    except:
        traceback.print_exc()
        print('exit')
        break
