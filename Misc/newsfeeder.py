import feedparser
import webbrowser

def main():

        print("\n \033[92m \033[1m*** Security News Feed *** \033[0m \n")
        print(" [0]:\033[91m The Hacker News \033[0m")
        print(" [1]:\033[91m Threat Post \033[0m")
        print(" [2]:\033[91m Naked Security \033[0m \n")   

        website_list = ("https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed")

        website_input = int(input("Enter website no. (0-2): "))

        NewsFeed = feedparser.parse(website_list[website_input])
        article_lst = []
        article_lnk = []
        for i in range(7):
            article = NewsFeed.entries[i]
            title = article.title
            link = article.link
            article_lnk.append(link)
            article_lst.append(title)

        article_num = 1
        for article in article_lst:
            print('[{}] {}'.format(str(article_num), article))
            article_num += 1

        article_lnk_click = False
        while not article_lnk_click:
            user_choice = int(input("Enter the article no. you wish to read(1-7): "))
            webbrowser.open(article_lnk[user_choice-1])
            article_lnk_click = True

main()