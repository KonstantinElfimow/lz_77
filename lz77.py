def lz77(string: str):
    resource: str = string.replace(' ', '_') + '_'

    result: list = []
    search_buffer: list = []
    i: int = 0
    while i < len(resource):
        shift: int = 0
        length: int = 0
        lst: list = [j for j in range(len(search_buffer)) if resource[i] == search_buffer[j]]
        for j in lst:
            temp_length: int = 0

            while i + temp_length < len(resource) - 1 and resource[i + temp_length] == search_buffer[j + temp_length]:
                temp_length += 1

            if temp_length >= length:
                shift = i - j
                length = temp_length

        # print(''.join(x for x in search_buffer))
        search_buffer.extend(list(resource[i: i + length + 1]))
        result.append(tuple([shift, length, resource[i + length]]))

        i += length + 1

    # print(string)
    # result.append('-')

    return result
