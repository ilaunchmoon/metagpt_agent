import aiohttp
import asyncio
from bs4 import BeautifulSoup

def fetch_html(url):
    with open(url, encoding="utf-8") as f:
        html = f.read()
    return html

async def parse_github_trending(html):
    soup = BeautifulSoup(html, 'html.parser')

    repositories = []

    for article in soup.select('article.Box-row'):
        repo_info = {}
        
        repo_info['name'] = article.select_one('h2 a').text.strip()
        repo_info['url'] = article.select_one('h2 a')['href'].strip()

        # Description
        description_element = article.select_one('p')
        repo_info['description'] = description_element.text.strip() if description_element else None

        # Language
        language_element = article.select_one('span[itemprop="programmingLanguage"]')
        repo_info['language'] = language_element.text.strip() if language_element else None

        # Stars and Forks
        stars_element = article.select('a.Link--muted')[0]
        forks_element = article.select('a.Link--muted')[1]
        repo_info['stars'] = stars_element.text.strip()
        repo_info['forks'] = forks_element.text.strip()

        # Today's Stars
        today_stars_element = article.select_one('span.d-inline-block.float-sm-right')
        repo_info['today_stars'] = today_stars_element.text.strip() if today_stars_element else None

        repositories.append(repo_info)

    return repositories

async def main():
    url = 'github-trending-raw.html'
    html = fetch_html(url)
    repositories = await parse_github_trending(html)

    for repo in repositories:
        print(f"Name: {repo['name']}")
        print(f"URL: https://github.com{repo['url']}")
        print(f"Description: {repo['description']}")
        print(f"Language: {repo['language']}")
        print(f"Stars: {repo['stars']}")
        print(f"Forks: {repo['forks']}")
        print(f"Today's Stars: {repo['today_stars']}")
        print()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())