'''
Objective:
The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize 
and summarize customer feedback for a SaaS product.

Task 1: Keyword Highlighter

Write a program that searches through a series of product reviews for keywords 
such as "good", "excellent", "bad", "poor", and "average". 
Print out each review with the keywords in uppercase so they stand out.
'''

reviews =  ["This product is really good. I'm impressed with its quality.",
         "The performance of this product is excellent. Highly recommended!",
       "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]


products = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    high_lighted_review = review
    for product in products:
        high_lighted_review = high_lighted_review.replace(product,product.upper())
    print(high_lighted_review)

'''
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. 
Use a predefined list of positive and negative words to check against. 
The function should return the count of positive and negative words for each review.

# '''
# def sentiment_tally(review, positive_words, negative_words):
#     positive_count = 0
#     negative_count = 0 
#     review = review.lower()
    
#     words = review.split()
    
#     for word in words:
#         if word.strip(".,!?") in positive_words:
#             positive_count += 1
#         elif word.strip(".,!?") in negative_words:
#             negative_count += 1
    
#     return positive_count, negative_count

# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# # Example usage:
# review = "The movie was good, but the ending was disappointing."
# pos_count, neg_count = sentiment_tally(review, positive_words, negative_words)
# print("Positive words count:", pos_count)
# print("Negative words count:", neg_count)

'''
Task 3: Review Summary
Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.
'''

# def create_summary(review):
#     if len(review) <= 30:
#         return review
    
#     last_space_index = review[:30].rfind(' ')
    
#     if last_space_index == -1:
#         return review[:30] + "..."
    
#     return review[:last_space_index] + "..."

# # Example usage:
# review1 = "This is a very detailed review about a product that I recently purchased and I must say..."
# review2 = "The service provided by the company was exceptional and I am very satisfied with it."

# summary1 = create_summary(review1)
# summary2 = create_summary(review2)

# print("Summary 1:", summary1)
# print("Summary 2:", summary2)










   