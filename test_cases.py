# -*- coding: utf-8 -*-

import submission
import collections


def main():
    try:
        print('\n========== Problem A ==========')
        for computeMaxWordLength in (submission.computeMaxWordLength1,
                                     submission.computeMaxWordLength2,
                                     submission.computeMaxWordLength3):
            print('<{}>'.format(computeMaxWordLength.__name__))
            print(1, computeMaxWordLength('which is the longest word'))  # longest
            print(2, computeMaxWordLength('cat sun dog'))  # sun
            print(3, computeMaxWordLength(' '.join(str(x) for x in range(100000))))  # 99999

        print('\n========== Problem B ==========')
        print(1,
              submission.computeMostFrequentWord('the quick brown fox jumps over the lazy fox'))  # set(['the', 'fox'])
        print(2, submission.computeMostFrequentWord('the quick brown fox jumps over the lazy dog'))  # set(['the'])

        print('\n========== Problem C1 ==========')
        print(1, submission.computeLongestPalindrome0(""))  # 0
        print(2, submission.computeLongestPalindrome0("ab"))  # 1
        print(3, submission.computeLongestPalindrome0("aa"))  # 2
        print(4, submission.computeLongestPalindrome0("animal"))  # 3

        print('\n========== Problem C ==========')
        print(1, submission.computeLongestPalindrome(""))  # 0
        print(2, submission.computeLongestPalindrome("ab"))  # 1
        print(3, submission.computeLongestPalindrome("aa"))  # 2
        print(4, submission.computeLongestPalindrome("animal"))  # 3

        print('\n========== Problem D ==========')
        print(1, submission.mutateSentences('a a a a a'))  # ['a a a a a']
        print(2, submission.mutateSentences('the cat'))  # ['the cat']
        print(3, submission.mutateSentences(
            'the cat and the mouse'))  # ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']

        print('\n========== Problem E ==========')
        print(1, submission.manhattanDistance((0, 0), (5, 5)))  # 10
        print(2, submission.manhattanDistance((2, 3), (2, 3)))  # 0
        print(3, submission.manhattanDistance((3, 5), (1, 9)))  # 6

        print('\n========== Problem F ==========')
        v1 = collections.defaultdict(float, {'a': 5})
        v2 = collections.defaultdict(float, {'b': 2, 'a': 3})
        print(1, submission.sparseVectorDotProduct(v1, v2))  # 15

        v1 = collections.defaultdict(float, {'c': 5})
        v2 = collections.defaultdict(float, {'b': 1, 'a': 2})
        print(2, submission.sparseVectorDotProduct(v1, v2))  # 0.0

        v1 = collections.defaultdict(float, {'a': 5, 'b': 4})
        v2 = collections.defaultdict(float, {'b': 2, 'a': -1})
        print(3, submission.sparseVectorDotProduct(v1, v2))  # 3

        print('\n========== Problem G ==========')
        v1 = collections.defaultdict(float, {'a': 5})
        scale = 2
        v2 = collections.defaultdict(float, {'b': 2, 'a': 3})
        submission.incrementSparseVector(v1, 2, v2)
        print(1, dict(v1))  # {'a': 11, 'b': 4.0}

    except NotImplementedError as err:
        # print err
        print("\nNotImplementedError: you didn't implement the function.")


if __name__ == '__main__':
    main()
