from lz77 import lz77


def main():
    string: str = open('input.txt', encoding='utf-8', mode='r').read()
    result = lz77(string)

    with open('output.txt', encoding='utf-8', mode='w') as file_output:
        for counter, i in enumerate(range(len(result))):
            file_output.write('{}. {}'.format(counter + 1, str(result[i])))
            file_output.write('\n')


if __name__ == '__main__':
    main()
