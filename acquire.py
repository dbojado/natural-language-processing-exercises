# Acquire File

import pandas as pd
import numpy as np

################## Acquire Codeup Blog ##################

def get_blog_articles():
    # if we already have the data, read it locally
    if path.exists('article.txt'):
        with open('article.txt') as f:
            return f.read()

    # otherwise go fetch the data
    url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='jupiterx-post-content')

    # save it for next time
    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text


################## Acquire News Articles ##################

def get_news_articles():
    # if we already have the data, read it locally
    if path.exists('article.txt'):
        with open('article.txt') as f:
            return f.read()

    # otherwise go fetch the data
    url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', class_='jupiterx-post-content')

    # save it for next time
    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text