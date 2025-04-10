import matplotlib.pyplot as plt
from collections import Counter 

def make_plot(sentiments: list) -> None:
    """_summary_

    Args:
        sentiments (list): _description_
    """
    sentiments_cnt = Counter(sentiments)    

    labels = list(sentiments_cnt.keys())
    height = list(sentiments_cnt.values())

    
    plt.bar(labels, height, color='hotpink')
    
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.title('Sentiment Distribution')

    plt.savefig('images/sentiments.png')
    