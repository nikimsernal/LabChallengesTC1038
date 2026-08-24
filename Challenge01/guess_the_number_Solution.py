import random

def main():
  num = random.randint(0,20)
  cnt = 0
  
  name = input('Hello! What is your name? ')
  
  guess = int(input(f'Well, {name} , I am thinking of a number between 1 and 20. Take a guess! '))
  
  while(guess != num):
    if(num < guess):
      cnt+=1
      print('Your guess is too high. ')
      guess = int(input('Take a guess '))
    else:
      cnt+=1
      print('Your guess is too low. ')
      guess = int(input('Take a guess  '))
    
  if(num == guess):
    cnt+=1
    print('Good job,', name, '! You guessed my number in', cnt, 'guesses!')

main()
