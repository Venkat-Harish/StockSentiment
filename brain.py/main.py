from google_search import GoogleSearch
from summarizer import TextSummarizer,NewspaperLib
from sentiment import sentiment_anlysis

class main():
    def __init__(self):
        self.google_search = GoogleSearch()  

    def response_newspaperlib(self,query):
        query =  ""
        
        links = self.google_search.get_links(query)

        output = []
        for news_link in links:
            print(news_link)
            news_obj = NewspaperLib(news_link)
            summary = news_obj.summary()
            date = news_obj.publish_date()
            text = news_obj.paragraph()
            if summary=="":
                continue
            result,confidence_score = sentiment_anlysis.get_one_sentiment_classification(summary)
            output.append([text,summary,result,confidence_score,date])

        for i in output:
            print(i[1:4])
        
        return output



    def response_llm(self,query):
        data = self.google_search.get_text(query)
        # for news in data:
        #     print(news)
        #     print("################################################################################################")


        i=0
        for news in data:
            print(i)
            i+=1
            summary = TextSummarizer.smolLM(news)

            result,confidence_score = sentiment_anlysis(summary)

            print(result)
            print(confidence_score)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

if __name__ == '__main__':
    main()





