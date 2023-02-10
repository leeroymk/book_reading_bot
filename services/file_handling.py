# from book.book_dict import book2

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    divider: str = ';:.,!?'
    end: int = min(start + size, len(text)) - 1
    if end + 1 == len(text):
        res = text[start:]
        return res, len(res)
    else:
        last_char: str = text[min(start + size, len(text))]
        for i in range(end, start, -1):
            if text[i] in divider:
                stop = i
                if last_char in divider:
                    last_char = text[i]
                else:
                    res = text[start:stop + 1]
                    return res, len(res)
            else:
                last_char = text[i]


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as some_text:
        file = some_text.read()

    counter: int = 1
    start: int = 0
    while start < len(file):
        text_and_len = _get_part_text(file, start, PAGE_SIZE)
        book[counter] = text_and_len[0].lstrip()
        counter += 1
        start += len(text_and_len[0])


prepare_book(BOOK_PATH)
