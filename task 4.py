# Ensure the required libraries are installed
# !pip install pandas scikit-learn

# 1. IMPORTING LIBRARIES
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 2.1 Sample Movie Data
movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'MovieName': ['A', 'B', 'C', 'D', 'E'],
    'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy'],
    'Description': ['Action-packed movie with explosions and fights.',
                    'A funny comedy with lots of laughs and humor.',
                    'Thrilling action movie with suspenseful scenes.',
                    'A drama with emotional and touching moments.',
                    'A funny comedy with lots of laughs and humor.']
}

# 2.2 Sample Ratings Data
ratings_data = {
    'UserID': [1, 1, 2, 2, 3],
    'MovieID': [1, 2, 3, 4, 5],
    'Rating': [5, 4, 3, 2, 4],
}

# 3. Create DataFrames
movies_df = pd.DataFrame(movies_data)
ratings_df = pd.DataFrame(ratings_data)

# 4. Merge dataframes to get movie details with ratings
movie_ratings = pd.merge(ratings_df, movies_df, on='MovieID')

# 5. CONTENT-BASED FILTERING

# 5.1 Function to create a TF-IDF matrix
def create_tfidf_matrix(descriptions):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    return tfidf_vectorizer.fit_transform(descriptions)

# 5.2 Function to compute cosine similarity
def compute_cosine_similarity(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)

# 5.3 Function to get movie recommendations based on ratings and similarity
def get_movie_recommendations(movie_name, rating_threshold=2.0):
    if movie_name not in movies_df['MovieName'].values:
        return []
    
    movie_index = movies_df.index[movies_df['MovieName'] == movie_name].tolist()[0]
    
    # Get movies similar to the selected one based on cosine similarity
    similar_movies = list(enumerate(cosine_similarity[movie_index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]  # Exclude the movie itself
    
    # Get movies with ratings above the threshold
    high_rated_similar_movies = []
    for i, _ in similar_movies:
        avg_rating = movie_ratings[movie_ratings['MovieID'] == movies_df['MovieID'][i]]['Rating'].mean()
        if avg_rating > rating_threshold:
            high_rated_similar_movies.append((movies_df['MovieName'][i], avg_rating))
    
    # Sort movies based on average ratings
    high_rated_similar_movies = sorted(high_rated_similar_movies, key=lambda x: x[1], reverse=True)
    return high_rated_similar_movies

# 6. Create TF-IDF matrix and compute cosine similarity
tfidf_matrix = create_tfidf_matrix(movies_df['Genre'])
cosine_similarity = compute_cosine_similarity(tfidf_matrix)

# 7. Take input from user and get recommendations
def main():
    print("\nSimple Movie Recommendation System")
    movie_name = input("\nEnter the Movie Name: ")
    
    recommendations = get_movie_recommendations(movie_name)
    if recommendations:
        print(f"\nTop Movie Recommendations for '{movie_name}' based on User Preferences Using Content-Based Filtering")
        for movie, rating in recommendations:
            print(f"{movie} (Average Rating: {rating:.2f})")
    else:
        print(f"\nNo recommendations found for '{movie_name}'. Please check the movie name and try again.")

if __name__ == "__main__":
    main()
