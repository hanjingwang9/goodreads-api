import requests
from bs4 import BeautifulSoup

class Shelves:
    def get_shelf(user_id, shelf):
        """
        Scrapes user's 'to-read' shelf for book titles.

        Args:
            user_id (str): The numeric ID of the Goodreads user.
            shelf (str): Default set to to-read.

        Returns:
            list: A list of book titles.
        """
        url = f"https://www.goodreads.com/review/list/{user_id}?shelf={shelf}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')
            book_titles = []

            title_elements = soup.find_all('td', class_='field title')

            for element in title_elements:
                title_tag = element.find('a')
                if title_tag:
                    book_titles.append(title_tag.text.strip())

            return book_titles

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None