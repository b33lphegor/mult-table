#!/usr/bin/env python3

if __name__ == '__main__':

    for i in range(1, 13):

        print('{:>3}|'.format(i), end=' ')

        for j in range(1, 13):

            print('{:>4}'.format(i * j), end=' ')

        if i == 1:

            print('\n{:*^64}'.format(''), end=' ')

        print('')
