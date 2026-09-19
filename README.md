# Happy Numbers 

## Description
In this game, you will be diving into the world of "happy" numbers. A number is considered "happy" if by following a specific sequence, it results in 1. The sequence is as follows:

1. Start with any positive integers
2. Replace the number by the sum of the squares of its digits
3. Repeat the process untill the number is equals 1 (where it will stay), or it loops endless endlessly in a cycle which does not include 1.

These numbers for which this process ends in 1 are happy numbers.

## Example
19 is a happy number. Here is why:
- 1^2 + 9^2 = 82
- 8^2 + 2^2 = 68
- 6^2 + 8^2 = 100
- 1^2 + 0^2 + 0^2 = 1

As you can see, we eventually reached 1, which mmakes 19 a "happy" number. This project tasks you to create a program that can accurately determine whether any given number inteher is a happy number or not. 


## Project Structure
```text
 Happy Numbers/
│
├── src/
│   └── happy_number.py
├── README.md
└── requirements.txt
