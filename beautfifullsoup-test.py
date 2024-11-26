from bs4 import BeautifulSoup
import requests
import re

def traverse_tags(url, tag, keyword):
    """Extract and search content of specific HTML tags from a given URL."""
    try:
        # Send a request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all specified tags
        tags = soup.find_all(tag)

        # Iterate through each tag
        for tag_content in tags:
            # Extract the text from the tag
            text = tag_content.get_text()

            pattern = rf'\b{keyword}\b'  # Use an f-string to insert the keyword

            # Find matches in the text
            matches = re.findall(pattern, text, flags=re.IGNORECASE)

            # Print the tag text if matches are found
            if matches:
                print(f"Found '{len(matches)}' matches in URL: {url}")
                print(text)
                print("-------------")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

class DomainHandler:
    def __init__(self, sitemap_url):
        """Initialize the class and fetch all domains from the sitemap."""
        print("Starting domain handler...")
        self.domains = self.fetch_and_parse_sitemap(sitemap_url)
        self.print_all_domains()

    def print_all_domains(self):
        """Print all the domains found."""
        print("Domains:")
        for domain in self.domains:
            print(domain)

    def return_all_domains(self):
        """Return the list of all domains."""
        return self.domains

    def fetch_and_parse_sitemap(self, sitemap_url):
        """Fetch and parse a sitemap, returning all URLs found."""
        print(f"Fetching sitemap: {sitemap_url}")
        urls = []
        try:
            # Fetch the sitemap
            response = requests.get(sitemap_url)
            response.raise_for_status()  # Check for HTTP errors
            xml = response.text

            # Parse with BeautifulSoup
            soup = BeautifulSoup(xml, "lxml")

            # Check if it's a sitemap index or a URL set
            sitemap_tags = soup.find_all("sitemap")
            if sitemap_tags:
                # It's a sitemap index, fetch nested sitemaps recursively
                for sitemap in sitemap_tags:
                    loc = sitemap.findNext("loc").text
                    urls.extend(self.fetch_and_parse_sitemap(loc))  # Use self to call the instance method
            else:
                # It's a URL set, extract all <loc> tags
                url_tags = soup.find_all("loc")
                print(url_tags)
                urls.extend([url.text for url in url_tags])

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {sitemap_url}: {e}")
        return urls


if __name__ == '__main__':
    sitemap_url = input("URL: ")+"sitemap.xml"
    keyword = input("keyword: ")
    print("Starting domain checkup...")
    domain_handler = DomainHandler(sitemap_url)  # Instantiate the class

    # Traverse and search all 'p' tags in the found domains
    tag1 = 'p'
    tag2 = 'a'
    tag3 = 'li'
    tag4 = 'div'

    for url in domain_handler.return_all_domains():
        traverse_tags(url, tag1, keyword)
        traverse_tags(url, tag2, keyword)
        traverse_tags(url, tag3, keyword)
        username = input("Press Enter" + url)
