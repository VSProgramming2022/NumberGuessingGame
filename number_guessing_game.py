import random 

secret_num = random.randint(0, 10)

def main():
  no_of_guess = 0

  while True:
    c = int(input('Enter a number between 0 and 10: '))

    if c < secret_num:
      print("Your number is lower than the secret number.")

    elif c > secret_num:
      print("Your number is greater than the secret number.")

    elif c == secret_num:
      print("You Won!!!")
      return False

    if no_of_guess == 3:
      print("You are out of guesses.")
      return False

if __name__ == '__main__':
  main()