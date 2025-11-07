from openai import OpenAI

def get_sentiment(text: list) -> list:
    """
    Analyzes product reviews for sentiment using the OpenAI API.

    Each review is classified into one of four categories: positive, neutral, 
    negative, or irrelevant. The API returns one line per review, which is parsed 
    into a list of sentiment labels in the original order.

    Args:
        text (list of str): List of product review strings.

    Returns:
        list of str: Sentiment labels ("positive", "neutral", "negative", or "irrelevant").
                     Returns an error message if the input is empty or invalid.
    """

    if not text or not all(isinstance(el, str) for el in text):
        return "Wrong input. Text must be an array of strings."
    
    reviews_str = "\n".join(f"{idx+1}. {review}" for idx, review in enumerate(text))
    
    system_prompt = """
    You are an excellent product review sentiment analyst.
    Classify each product review into one of the following labels:
    positive, neutral, negative, or irrelevant.
    
    Definitions:
    - "Positive" means the review praises the product.
    - "Negative" means the review criticizes the product.
    - "Neutral" means the review is balanced or lacks strong emotion.
    - "Irrelevant" means the review does not express an opinion about the product itself (e.g., shipping info, unrelated personal stories, comparisons, general brand opinions).

    Rules:
    - Output exactly one label per review.
    - The output must have the format: [review_number]: [label]
    - Use only one of the four labels (no commentary or extra text).

    Examples:
    Review: "The product arrived quickly." Output: [review_number]: irrelevant  
    Review: "I love this drink, it’s so refreshing!" Output: [review_number]: positive  
    Review: "It’s okay, not amazing but not bad." Output: [review_number]: neutral  
    Review: "Tastes awful. Would not recommend." Output: [review_number]: negative
    """

    prompt = f"""
    You will be given {len(text)} numbered reviews. 
    Return exactly {len(text)} lines, each starting with the review number, a colon, a space, and a sentiment label.
    Use only one of: positive, neutral, negative, irrelevant.

    Do not add commentary, extra text, or blank lines.

    ###
    {reviews_str}
    """

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ]
    )

    output_lines = response.choices[0].message.content.strip().splitlines()

    sentiments = []
    for i, line in enumerate(output_lines):
        parts = line.strip().split(":")
        if len(parts) == 2:
            label = parts[1].strip().lower()
            if label in {"positive", "neutral", "negative", "irrelevant"}:
                sentiments.append(label)
            else:
                print(f"Invalid label at line {i+1}: {label}")
        else:
            print(f"Could not parse line {i+1}: {line}")

    return sentiments