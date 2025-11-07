from .label import get_sentiment
from .visualize import make_plot
import json


def run(filepath: str) -> list:
    """
    Processes review data from a JSON file, analyzes sentiment, and visualizes the result.
    
    Args:
        filepath (str): The path to the JSON file containing the review data.

    Returns:
        list of str: A list of sentiment labels for the reviews.
    """
    with open(filepath) as file:
        data = json.load(file)

    reviews = data['results']
    sentiments = get_sentiment(reviews)
    make_plot(sentiments)
    
    return sentiments

if __name__ == "__main__":
    print(run("data/reviews.json"))