import requests
import time
from collections import deque

class GitHubRepoParser:
    def __init__(self, github_api_key):
        self.github_api_key = github_api_key
        self.base_url = "https://api.github.com"

    def get_contents_url(self, paths_url):
        headers = {
            "Authorization": f"token {self.github_api_key}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(paths_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def gather_raw_urls(self, list_of_files, level, timeout=60):
        print(f"Collecting Level #{level} Python files.")
        start_time = time.time()
        raw_urls = {}
        queue = deque([(list_of_files, level)])  # Initialize queue with initial list_of_files and level

        while queue:
            if time.time() - start_time > timeout:
                print("Timeout reached. Exiting...")
                break  # Terminate the loop if timeout is reached
            current_files, current_level = queue.popleft()  # Dequeue the first element from the queue
            for file in current_files:
                if file["type"] == "file":
                    dot_index = file["name"].rfind(".") + 1
                    extension = file["name"][dot_index:] if "/" not in file["name"][dot_index:] else "Miscellaneous"
                    if extension == "py":
                        raw_urls.setdefault(extension, []).append(file["download_url"])
                elif file["type"] == "dir":
                    contents = self.get_contents_url(file["url"])
                    queue.append((contents, current_level + 1))  # Enqueue the contents of the directory with increased level

        return raw_urls

    def initialize_repo_details(self, url):
        self.url = url
        self.owner = url.split('https://github.com/')[1].split('/')[0]
        self.repo = url.split('https://github.com/')[1].split('/')[1]

    def collect_data(self, url):
        self.initialize_repo_details(url)
        contents_url = f"{self.base_url}/repos/{self.owner}/{self.repo}/contents"
        headers = {
            "Authorization": f"token {self.github_api_key}",
            "Accept": "application/vnd.github.v3+json"
        }
        try:
            response = requests.get(contents_url, headers=headers)
            response.raise_for_status()
            list_of_files = response.json()
            raw_urls = self.gather_raw_urls(list_of_files, 0)
            return raw_urls
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch repository data: {str(e)}")
            return {}
