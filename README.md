# CodeGenie🧞

This library provides a next-generation coding experience using AI agents.

Other Language README
[Japanese](README.ja.md)

## Installation

You can install it from the GitHub repository.

```sh
python -m pip install git+https://github.com/drago-suzuki58/CodeGenie
```

## Usage

CodeGenie uses the Google Gemini API. Please obtain your API key in advance.

Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create an API key.

**Example Usage:**

```python
from codegenie import CodeGenie

code_genie = CodeGenie(api_key="YOUR_API_KEY", model="gemini-2.0-flash-exp")

code_genie.number_guess_game(1, 100)
```

When you run the code above, CodeGenie will generate Python code for the specified number guessing game and execute it on the spot.  
The generated code example is as follows:

```python
def number_guess_game(*args, **kwargs):
    import random
    if len(args) == 2:
        lower_bound = args[0]
        upper_bound = args[1]
    else:
         lower_bound = 1
         upper_bound = 100

    secret_number = random.randint(lower_bound, upper_bound)
    guess = None
    attempts = 0

    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while guess != secret_number:
        try:
          guess = int(input("Take a guess: "))
          attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number in {attempts} tries!")
    
# Example
#number_guess_game(1,10)
#number_guess_game()

```

As shown above, you can have the AI generate various functions by calling `code_genie.any_function_name()`.

## Caching Functionality

Generated code is cached in the `./cache` folder by default. This reduces API calls when the same process is executed again.

- **Changing the cache directory:** You can change it with the `cache_dir` argument when initializing CodeGenie.
- **Deleting the cache:** You can do this by deleting the corresponding files.

## Disclaimer

This library uses `exec()` internally, which allows the AI to execute arbitrary code. Although a confirmation mechanism is in place, please be sure to check the generated code before execution. Due to security risks, it is recommended to use this library only in development and testing environments.

The developers are not responsible for any damages caused by the use of this library. Please use it at your own risk.
