import matplotlib.pyplot as plt
from collections import Counter 

def make_plot(sentiments: list) -> None:
    """
    Plots and saves a bar chart of sentiment counts to 'images/sentiments.png'.

    Args:
        sentiments (list of str): A list of sentiment labels.
    """
    sentiments_cnt = Counter(sentiments)    

    labels = list(sentiments_cnt.keys())
    height = list(sentiments_cnt.values())

    
    plt.bar(labels, height, color='hotpink')
    
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.title('Sentiment Distribution')

    plt.savefig('./images/sentiments.png')