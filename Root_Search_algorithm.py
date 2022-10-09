cube = 64
epsilon = 0.01
num_guesses = 0
# First case deals with the cube root of all numbers greater than 1
if abs(cube)>1:
    low = 0
    high = cube
    guess = (high+low/2.0)
    while abs(guess**3 - cube) >= epsilon:
        if guess**3<cube:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    print(guess, 'is close to the cube root of', cube)
# Second case deals with the cube root of numbers between 0 and 1
if cube<1 and cube>0:
    low = cube
    high = 1
    guess = (high+low/2.0)
    while abs(guess**3 - cube) >= epsilon:
        if guess**3<cube:
            low = guess
        else:
            high= guess
        guess = (high + low)/2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    print(guess, 'is close to the cube root of', cube)
# Third case deals with the cube root of numbers between -1 and 0
if cube<0 and cube>-1:
    low = abs(cube)
    high = 1
    guess = (high+low/2.0)
    while abs(guess**3 - abs(cube)) >= epsilon:
       if guess**3<abs(cube):
           low = guess
       else:
           high= guess
       guess = (high + low)/2.0
       num_guesses += 1
    print('num_guesses =', num_guesses)
    print(-guess, 'is close to the cube root of', cube)

