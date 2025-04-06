from bs4 import BeautifulSoup
import requests
from googlesearch import search

class GoogleSearch():
    def __init__(self):
        return

    
    def get_text(self,query):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        search_url = "https://www.google.com/search?q=" + query + "News&tbm=nws&lr=lang_en"
        links = search(search_url,num_results=5)
        # for i in links:
        #     print(i)

        data = []
        print("checker1")
        for url in links:
            if(url[:6]!="https:"):
                continue
            # print("INSIDE "+ url)
            webpage_response = requests.get(url,headers=headers)
            soup_html = BeautifulSoup(webpage_response.text, "html.parser")

            url_data = ""
            for para in soup_html.find_all("p"):
                # print(para.text)
                url_data += para.text

            data.append(url_data)
        # print(data)
        return data 
    
    def get_links(self,query):
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        search_url = "https://www.google.com/search?q=" + query + "News&tbm=nws&lr=lang_en"
        links = search(search_url,num_results=15)
        
        url_list = []
        for url in links:
            if(url[:6]!="https:"):
                continue
            url_list.append(url)

        return url_list




