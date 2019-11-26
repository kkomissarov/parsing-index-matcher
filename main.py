import csv
from config import(
    PARSING_FILE_PATH,
    INDEX_FILE_PATH,
    RESULT_FILE_PATH,
    PARSING_FILE_ENCODING,
    INDEX_FILE_ENCODING,
    PARSING_COLUMN_NUM,
    INDEX_COLUMN_NUM,
    PARSING_HAS_TITLE,
    INDEX_HAS_TITLE,
)


def main():
    with open(PARSING_FILE_PATH, 'r', encoding=PARSING_FILE_ENCODING) as parsing_file:
        reader = csv.reader(parsing_file, delimiter=';')
        parsing_urls = [row[PARSING_COLUMN_NUM] for row in reader]
        if PARSING_HAS_TITLE:
            parsing_urls = parsing_urls[1:]

    with open(INDEX_FILE_PATH, 'r', encoding=INDEX_FILE_ENCODING) as index_file:
        reader = csv.reader(index_file, delimiter=',')
        index_urls = [row[INDEX_COLUMN_NUM] for row in reader]
        if INDEX_HAS_TITLE:
            index_urls = index_urls[1:]

    with open(RESULT_FILE_PATH, 'w') as result_file:
        print('Страницы есть в парсинге,но нет в индексе:', file=result_file)
        for url in parsing_urls:
            if url not in index_urls:
                print(url, file=result_file)

        print(file=result_file)

        print('Страницы есть в индексе, но нет в парсинге:', file=result_file)
        for url in index_urls:
            if url not in parsing_urls:
                print(url, file=result_file)


if __name__ == '__main__':
    main()
