secret_word = ['java','python','nodejs','mongodb']
guess_start = 0
guess_limit = 3
while guess_start < guess_limit:
     guess = input('guess the fast growing programming language: ')
     guess_start += 1
     for word in secret_word:
      if word == guess :
        print('your guess is correct')
        break
else:
    print('your guess is wrong ')