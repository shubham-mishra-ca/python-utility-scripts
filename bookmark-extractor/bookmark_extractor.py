import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.urls.append(attr[1])


def extract_bookmark_urls(bookmarks_file, output_file):
    '''
    (str, str) -> None

    Extract all URLs from bookmarks_file and write them to output_file.

    bookmarks_file is a string that represents the path to the browser
    bookmarks HTML file.

    output_file is a string that represents the path to the output text file.

    The function doesn't return anything. It writes the URLs to the output file.
    '''

    parser = MyHTMLParser()
    with open(bookmarks_file, 'r', encoding='utf-8') as f:
        data = f.read()
        parser.feed(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(parser.urls))

extract_bookmark_urls('Chrome_Bookmarks.html', 'links.txt')
