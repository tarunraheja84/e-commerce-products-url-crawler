import aiohttp
import asyncio
from urllib.parse import urlparse, urljoin
from collections import defaultdict
from bs4 import BeautifulSoup

from utils.output import save_matched_urls_to_json
from utils.load_config import load_config
from utils.fetch_html import fetch_html
from utils.helper_functions import is_same_domain, matches_pattern

visited = set()
matched_urls_map = defaultdict(list)

def extract_links(html, base_url, domains, patterns):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all(["link","a"], href=True):
        href = tag['href']
        full_url = urljoin(base_url, href)
        if is_same_domain(full_url, domains):
            parsed = urlparse(full_url)
            clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path
            links.add(clean_url)

            if matches_pattern(parsed, patterns):
                print("Product URL found:", clean_url)
                matched_urls_map[parsed.scheme + "://" + parsed.netloc].append(clean_url)

    return links

async def crawl(session, url, queue, domains, patterns, semaphore):
    if url in visited:
        return
    visited.add(url)

    html = await fetch_html(session, url, semaphore)

    if html:
        for link in extract_links(html, url, domains, patterns):
            if link not in visited:
                queue.append(link)

async def main():
    start_urls, patterns, semaphore_limit = load_config()
    semaphore = asyncio.Semaphore(semaphore_limit)
    domains = [urlparse(url).netloc for url in start_urls]
    queue = list(start_urls)

    async with aiohttp.ClientSession() as session:
        while queue:
            tasks = []
            current_batch = queue[:]
            queue.clear()

            for url in current_batch:
                tasks.append(crawl(session, url, queue, domains, patterns, semaphore))
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

    save_matched_urls_to_json(matched_urls_map)

    print("\nMatched URLs by domain:")
    for domain, urls in matched_urls_map.items():
        print(f"- {domain}: {len(urls)} URLs")
