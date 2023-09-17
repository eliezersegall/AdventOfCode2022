"""
Day 3 of the Advent of Code 2020

part 1:
input: a file where each line is a string of letters both capital and small.
we need to split each word in half and find out what letter appears on both halves of the word.
then, we add that letter's value to the final sum.
each letter has a value as follows:
Lowercase item types a through z have values 1 through 26.
Uppercase item types A through Z have values 27 through 52.
output: the sum of all the letters we found.

part 2:
this time we split the lines into groups of 3 lines.
we need to find the letter that appears on all 3 lines and add its value to the final sum.
output: the sum of all the letters we found.
"""
# we create a dictionary with the values of each letter
# lowercase letters have values 1 through 26 which we get by subtracting 96 from the ascii value of the letter
letters_values = {chr(i): i - 96 for i in range(ord("a"), ord("z") + 1)}
# uppercase letters have values 27 through 52 which we get by subtracting 38 from the ascii value of the letter
letters_values.update({chr(i): i - 38 for i in range(ord("A"), ord("Z") + 1)})


def part1():
    """
    takes care of part 1

    reads Day3Input.txt and prints the sum of the letters that appear on both halves of each word

    :return: the sum of the letters that appear on both halves of each word
    :rtype: int
    """
    with open("Day3Input.txt", "r") as f:
        # we read the file's content into a list
        # each word is split in half and stored in a sub list
        words = [[word[0:len(word) // 2], word[len(word) // 2:]] for word in f.read().split("\n")]
    # we create a list of sets of letters that appear on both halves of each word
    letters = [set(word[0]) & set(word[1]) for word in words]
    # we pop each set of letters and add the value of each letter to the final sum
    print(sum(letters_values[letter.pop()] for letter in letters))


def part2():
    """
    takes care of part 2

    reads Day3Input.txt and prints the sum of the letters that appear on all 3 lines for each group

    :return: the sum of the letters that appear on all 3 lines for each group
    :rtype: int
    """
    with open("Day3Input.txt", "r") as f:
        # we read the file's content into a list
        words = f.read().split("\n")
    # we make a new list which contains sub lists of each trio of words from 'words'
    words_groups = [[words[i], words[i + 1], words[i + 2]] for i in range(0, len(words), 3)]
    # we create a list of sets of letters that appear in all 3 words for each group
    letters = [set(words[0]) & set(words[1]) & set(words[2]) for words in words_groups]
    # we pop each set of letters and add the value of each letter to the final sum
    print(sum(letters_values[letter.pop()] for letter in letters))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
