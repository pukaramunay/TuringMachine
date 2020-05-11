input_will_general = True
input_will_tape = True
while input_will_general== True:
    input_will_yn = True
    retries_tape = 10
    # Lines 15 to 73 code the `while` loop that asks the users to insert an
    # input that is subsequently converted in the tape, which is a list
    # composed by an even number of items and each item can be solely a 0 or a
    # 1.  If the tape is empty, users are required to insert a valid input;
    # in the case they fail to insert a valid input in all the 11 attempts, the
    # program is terminated (lines 25 to 39).  If the tape is valid thus, the
    # list is composed by at least 2 items, it is processed in order to make
    # it bear an even number of 0s and 1s (lines 40 to 73). This `while` loop
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
                      'chance! If you fail to insert a valid answer once '
                      'more, the program will be quit.')
            if retries_tape < 0:
                print('You exceeded the allowed number of attempts.\nThe '
                      'program will be quit. Bye!')
                input_will_tape = False
                input_will_yn = False
                input_will_general = False
        if len(tape) > 1:
            print('Based on your input, this is the tape to be processed:',
                  tape)
            h = 0    # h is the position of the tape's square which is inside
                     # the head of the machine
            state = 0
            while h + 1 < len(tape):
                if tape[h] == 0:
                    state = state - 1
                if tape[h] == 1:
                    state = state + 1
                if state < -1:
                    tape[h] = 1
                    state = state + 2    # Set state = 0
                if state > 1:
                    tape[h] = 0
                    state = state - 2    # Set state = 0
                h = h + 1
            while h + 1 == len(tape):  # Compensating the difference of
                # calculation starting from 0 (position) and 1 (lenght).
                if state < 0:
                    tape[h] = 1
                    state = state + 1    # Set state = 0
                if state > 0:
                    tape[h] = 0
                    state = state - 1    # Set state = 0
                if state == 0:
                    print('After processing the tape, this is the outcome:'
                          '       ', tape)    # The spaces put the original
                                              # and the processed tape on the
                                              # same level, facilitating
                                              # comparison between the two.
                    break
            break
    # Lines 80 to 104 code the `while` loop that asks to the users if they
    # would like to insert another values.  Since the user input is either YES
    # or NO, the loop is characterized by the suffix `yn`.  This `yn` loop is
    # executed in the case a valid tape has been submitted and successfully
    # processed.
    retries_yn = 5
    while input_will_yn == True:
        user_answer = input('Would you like to insert another input? (Y/N): ')
        if user_answer in ('y', 'ye', 'yes', 'ok', 'Y', 'YE', 'YES', 'OK'):
            input_will_yn = False
        elif user_answer in ('n', 'no', 'nop', 'nope',
                             'N', 'NO', 'NOP', 'NOPE'):
            print("You don't want to insert another input. "
                  "The program will be quit.")
            input_will_yn = False
            input_will_general = False
        else:
            retries_yn = retries_yn - 1
            if retries_yn > 0:
                print('Your input is not valid. Try again! You still have',
                      retries_yn + 1, 'more attempts.')
            if retries_yn == 0:
                print('Your input is not valid. This is your very last '
                      'chance! If you fail to insert a valid answer once '
                      'more, the program will be quit. Just type YES or NO!')
            if retries_yn < 0:
                print("You exceeded the allowed number of attempts.\nSince "
                      "you weren't able to type a YES or NO, now the program "
                      "will be unapologetically quit. Bye!")
                input_will_yn = False
                input_will_general = False