from tree_sitter import Language, Parser
from io import BytesIO
import requests
from parser.githubRepoParse import GitHubRepoParser
import sys
sys.path.append('/Users/ayushraj/Developer/dev/GithubCodeFlow')
from models.functionsInfo import functionInfo

class FileParser:
    def __init__(self):
        # Build the language library
        Language.build_library(
            "build/my-languages.so",
            ["/Users/ayushraj/tree-sitter-python"],
        )

        # Define the language
        self.PY_LANGUAGE = Language("build/my-languages.so", "python")

        # Create a parser
        self.parser = Parser()
        self.parser.set_language(self.PY_LANGUAGE)

    def fetch_python_functions_info(self, repo_urls):
        all_function_info = []

        def extract_information(root, file_name):
            functions_info = []
            current_class = None
            todo = [(root, current_class)]
            while todo:
                node, current_class = todo.pop(0)
                if node.type == "function_definition":
                    function_name = node.child_by_field_name('name').text.decode('utf-8')
                    function_code = node.text.decode('utf-8')
                    function_info_obj = functionInfo(
                        fileName=file_name,
                        functionName=function_name,
                        functionBody=function_code,
                        functionClass=current_class
                    )
                    functions_info.append(function_info_obj)
                elif node.type == "class_definition":
                    current_class = node.child_by_field_name('name').text.decode('utf-8')
                for child in node.children:
                    todo.append((child, current_class))
            return functions_info

        for url in repo_urls:
            response = requests.get(url)
            if response.status_code == 200:
                tree = self.parser.parse(BytesIO(response.content).read())
                root = tree.root_node
                functions_info = extract_information(root, url.split('/')[-1])
                all_function_info.extend(functions_info)
            else:
                print(f"Failed to download the file from {url}")

        return all_function_info

def parseTheRepo(repo_link: str):
    github_api_key = "dfgfdfgdfgfggffg" 
    fileParser = GitHubRepoParser(github_api_key)
    response = fileParser.collect_data(repo_link)
    repo_urls = response.get("py", [])

    all_functions_info = FileParser().fetch_python_functions_info(repo_urls)
    return all_functions_info


