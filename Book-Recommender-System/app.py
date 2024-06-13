from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass@123",
    database="book_recommendations"
)
cursor = db.cursor()

# Define functions to retrieve data from the database
def get_popular_books_from_db():
    query = "SELECT Book_Title, avg_rating FROM popular_books LIMIT 50"
    cursor.execute(query)
    return cursor.fetchall()

def get_book_recommendations_from_db(favorite_book_title):
    query = """
            SELECT books.ISBN, books.Book_Title, books.Book_Author, books.Year_Of_Publication, books.Publisher, books.Image_URL
            FROM books
            JOIN similarity_scores ON books.Book_Title = similarity_scores.Similar_Book_Title
            WHERE similarity_scores.Favorite_Book_Title = %s
            ORDER BY similarity_scores.Similarity_Score DESC
            LIMIT 50
            """
    cursor.execute(query, (favorite_book_title,))
    return cursor.fetchall()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    favorite_book_title = request.form['book_title']
    recommendations = get_book_recommendations_from_db(favorite_book_title)
    return render_template('recommendations.html', favorite_book_title=favorite_book_title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
