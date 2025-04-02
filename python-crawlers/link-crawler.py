import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

def get_all_links(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return []

  soup = BeautifulSoup(response.content, 'html.parser')
  links = set()

  for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    # Ignore hrefs that are just fragments
    if not href.startswith('#'):
      # Resolve relative URLs
      full_url = urljoin(url, href)
      # Ensure the link belongs to the same domain
      if urlparse(full_url).netloc == urlparse(url).netloc:
        links.add(full_url)

  return links

def save_links_to_file(links, file_path):
  try:
    with open(file_path, 'w') as file:
      for link in sorted(links):
        file.write(link + '\n')
    print(f"Links saved to {file_path}")
  except IOError as e:
    print(f"Error writing to file: {e}")

if __name__ == "__main__":
  target_url = input("Enter the URL to crawl: ").strip()
  output_file = "unique_links.txt"

  print("Crawling for links...")
  unique_links = get_all_links(target_url)

  print(f"Found {len(unique_links)} unique links.")
  save_links_to_file(unique_links, output_file)