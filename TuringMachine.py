input_will_general = True
input_will_tape = True
while input_will_general== True:
    retries_tape = 8
    # Lines 14 to 62 code the `while` loop that asks the users to insert an
    # input that is subsequently converted in the tape, which is a list
    # composed by an even number of items and each item can be solely a 0 or a
    # 1.  If the tape is empty, users are required to insert a valid input;
    # in the case they fail to insert a valid input in all the 11 attempts, the
    # program is terminated (lines 24 to 38).  If the tape is valid thus, the
    # list is composed by at least 2 items, it is processed in order to make
    # it bear an even number of 0s and 1s (lines 39 to 56). This `while` loop
    # is characterized by the suffix `tape`.
    while input_will_tape == True:
        user_input = input('Insert a series of 0s and/or 1s: ')
        tape = []
        for keystroke in user_input:
            if keystroke in '0':
                tape.append(0)
            if keystroke in '1':
                tape.append(1)
        if len(tape) % 2 == 1:
            tape = tape[:-1]
        if len(tape) == 0:
            retries_tape = retries_tape - 1
            if retries_tape > 0:
                print('Your input is not valid. Try again! You still have',
                      retries_tape + 1, 'more attempts.')
            if retries_tape == 0:
                print('Your input is not valid. This is your very last '
                      'chance! If you fail to insert a valid input once '
                      'more, the program will be quit.')
            if retries_tape < 0:
                print('You exceeded the allowed number of attempts.\nThe '
                      'program will be quit. Bye!')
                input_will_general = False
                input_will_tape = False
                input_will_yn = False
        if len(tape) > 1:
            print('Based on your input, this is the tape to be processed:',
                  tape)
            h = 0    # position of the scanned square (in the machine's head)
            state = 0
            while len(tape) - (h + 1) >= 0:
                missing_squares = len(tape) - (h + 1)
                if tape[h] == 0:
                    state = state - 1
                if tape[h] == 1:
                    state = state + 1
                if state < (missing_squares - (2 * missing_squares)):
                    tape[h] = 1
                    state = state + 2
                if state > missing_squares:
                    tape[h] = 0
                    state = state - 2
                h = h + 1
            print('After processing the tape, this is the outcome:       '
                  , tape)  # The spaces put the original and the processed
                           # tape on the same level, facilitating comparison
                           # between the two.
            input_will_tape = False
            input_will_yn = True
    # Lines 69 to 91 code the `while` loop that asks to the users if they
    # would like to insert another values.  Since the user's input is either
    # yes or no, the loop is characterized by the suffix `yn`.
    retries_yn = 4
    while input_will_yn == True:
        user_answer = input('Would you like to insert another input? (Y/N): ')
        if user_answer in ('y', 'ye', 'yes', 'ok', 'Y', 'YE', 'YES', 'OK'):
            input_will_yn = False
            input_will_tape = True
        elif user_answer in ('n', 'no', 'nop', 'nope',
                             'N', 'NO', 'NOP', 'NOPE'):
            print("You don't want to insert another input. "
                  "The program will be quit. Bye!")
            input_will_general = False
            input_will_yn = False
        else:
            retries_yn = retries_yn - 1
            if retries_yn > 0:
                print('Your input is not valid. Try again! You still have',
                      retries_yn + 1, 'more attempts.')
            if retries_yn == 0:
                print('Your input is not valid. This is your very last '
                      'chance! If you fail to insert a valid answer once '
                      'more, the program will be quit.\nJust type YES or NO!')
            if retries_yn < 0:
                print('You exceeded the allowed number of attempts.\nThe '
                      'program will be quit. Bye!')
                input_will_general = False
                input_will_yn = False
