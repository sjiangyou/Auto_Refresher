import time
import webbrowser
from scraper import check_keywords

def main():
    urls_old = []
    running = True
    while running:
        time.sleep(1)
        urls_new = check_keywords()
        if (urls_new != urls_old and not urls_old):
            for urls in urls_old:
                try:
                    urls_old.index(urls)
                except ValueError:
                   webbrowser.open(urls)
                   running = False


if __name__ == '__main__':
    main()