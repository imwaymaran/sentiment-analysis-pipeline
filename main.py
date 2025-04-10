from label import get_sentiment
from visualize import make_plot
import json


def run(filepath: str) -> list:
    """
    Processes review data from a JSON file, analyzes sentiment, and visualizes the result.
    
    Args:
        filepath (str): The path to the JSON file containing the review data.

    Returns:
        list of str: A list of sentiment labels for the reviews.
    """
    
    # open the json object
    with open(filepath) as file:
        data = json.load(file)

    reviews = data['results']
    
    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)
    
    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)
    return sentiments

if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
