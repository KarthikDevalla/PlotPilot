# PlotPilot: A Content-Based Book Recommendation System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A content-based book recommendation system that suggests personalized book recommendations based on book content. 

## Features

- Personalized Recommendations: The system analyzes book content to provide highly tailored book recommendations.
- Content Analysis: Utilizes NLP(Natural Langauge Processing) techniques to extract key features from books, such as genre, author, and plot keywords, enhancing the recommendation process.
- Similarity Algorithm: Applies cosine similarity to calculate the similarity between books and thus recommends accordingly.
- Scalability: Deployed this system on Streamlit which supports hundreds of users concurrently.

### Installation

Clone the repository:

   ```shell
   git clone https://github.com/your-username/content-based-book-recommendation.git
   ```

### Usage

Recommendation generation: Execute the recommendation script to generate personalized book recommendations based on user preferences:

   ```shell
   python app.py
   ```

## Acknowledgments

- The recommendation system implementation is inspired by the concept of content-based filtering.
- Dataset Courtesy [Kaggle](https://www.kaggle.com/datasets/muhammadadiltalay/imdb-video-games)
