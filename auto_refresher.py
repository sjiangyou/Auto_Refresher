import time
import webbrowser
from scraper import check_keywords

def main():
    urls_old = []
    running = True
    print('beginning to search school website')
    iterations = 0
    while running:
        iterations += 1
        time.sleep(0.5)
        urls_new = check_keywords()
        if (urls_new != urls_old and not urls_old):
            for urls in urls_old:
                try:
                    urls_old.index(urls)
                except ValueError:
                   webbrowser.open(urls)
            running = False
        if iterations % 20 == 0:
            print('still looking')


if __name__ == '__main__':
    main()