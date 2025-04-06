from llmware.agents import LLMfx

class sentiment_anlysis:
    def __init__(self):
        pass

    def get_one_sentiment_classification(text):
        if not text:
            print("Error: No text provided for sentiment analysis.")
            return None
        
        agent = LLMfx(verbose=True)
        agent.load_tool("sentiment")
        
        sentiment = agent.sentiment(text)
        print("Raw Sentiment Output:", sentiment)  # Debugging

        sentiment_value = sentiment.get("llm_response", {}).get("sentiment", "unknown")
        confidence_level = sentiment.get("confidence_score", 0)

        # print(f"Sentiment: {sentiment_value} | Confidence: {confidence_level}")

        # if "positive" in sentiment_value:
        #     print("Sentiment is positive.")

        # elif "negative" in sentiment_value:
        #     print("Sentiment is negative.")

        # else:
        #     print("Sentiment is neutral or unknown.")

        return sentiment_value,confidence_level

