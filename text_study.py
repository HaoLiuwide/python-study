def getS(pair):
    return pair[1]


def main():
    filename = input('Enter a book\'s filename: ')
    book = open(filename, 'r').read()
    book = book.lower()
    for ch in ':.-,':
        book = book.replace(ch, '')
    words = book.strip().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort()
    items.sort(key=getS, reverse=True)
    for info in items:
        word, count = info[0], info[1]
        print('{0:<15}{1:>5}'.format(word, count))


if __name__ == '__main__':
    main()
