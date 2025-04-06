import torch
import requests
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import T5Tokenizer, T5ForConditionalGeneration
from newspaper import Article
from newspaper.article import ArticleException
from datetime import datetime
from dateutil import parser
import pytz

class TextSummarizer():
    def __init__(self):
        pass


    def smolLM(data):
        # checkpoint = "HuggingFaceTB/SmolLM2-135M"
        checkpoint = "HuggingFaceTB/SmolLM2-1.7B-Instruct"

        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForCausalLM.from_pretrained(checkpoint).to("cpu")

        def _summarize(text, max_length=5001):
            """Generates a summary using the SmolLM model."""
            prompt = f"Summarize the following text into 4000 letters:\n{text}\n Result:"
            inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to("cpu")
            
            with torch.no_grad():
                output = model.generate(
                    inputs.input_ids, 
                    max_length=max_length, 
                    num_return_sequences=1,
                    do_sample=True,
                    temperature=0.7
                )
            
            return tokenizer.decode(output[0], skip_special_tokens=True)

        
        if(len(data)>5000):
            data =  data[:5000]
        text = data
        summary = _summarize(text)
        # print("Summary:", summary)
        return summary
    

    def t5small(data):
        """Generates a summary using the T5-Small model."""
        tokenizer = T5Tokenizer.from_pretrained("t5-small")
        model = T5ForConditionalGeneration.from_pretrained("t5-small").to("cpu")

        def _summarize_t5(text, max_length=len(data)):
            inputs = tokenizer("summarize: " + text, return_tensors="pt", truncation=True, max_length=512)
            summary_ids = model.generate(inputs.input_ids, max_length=max_length)
            return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        summary = _summarize_t5(data)
        return summary
        # print(summary)
    

class NewspaperLib():
    def __init__(self, data, max_retries=3, wait_time=5):
        """Initializes the article and handles 503 errors with retries."""
        self.news_article = Article(data, language="en")
        
        for attempt in range(max_retries):
            try:
                self.news_article.download()
                self.news_article.parse()
                self.news_article.nlp()
                return  # Exit loop if successful

            except ArticleException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(wait_time)
            
            except requests.exceptions.RequestException as e:
                print(f"Network error: {e}")
                break  
        
        print("Failed to download the article after multiple attempts.")

    def summary(self):
        return self.news_article.summary

    def title(self):
        return self.news_article.title
    
    def publish_date(self):
        date = self.news_article.publish_date
        return date
        # print(date)
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # if(date == "N/A" or date==None):
        #     return date
        
        # if isinstance(date, str):
        #     dt = parser.parse(date)
        # elif isinstance(date, datetime):
        #     dt = date
        # else:
        #     raise TypeError("Input must be a datetime object or a string")

        # # Localize to IST if timezone is missing
        # if dt.tzinfo is None:
        #     ist = pytz.timezone("Asia/Kolkata")
        #     dt = ist.localize(dt)

        # time_zone = dt.tzname()

        # return dt.strftime(f"%d/%m/%Y {time_zone}")
    
    def paragraph(self):
        return self.news_article.text

    def autohors(self):
        return self.news_article.authors