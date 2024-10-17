# BlogsWeb

## Overview
BlogsWeb is a web application built using Flask, a lightweight WSGI web application framework in Python. The application allows users to view blog posts, with the ability to limit the number of posts displayed on the main page.

## Features
- **View Blog Posts**: Users can view a list of blog posts on the main page.
- **Post Details**: Users can click on a blog post to view its details on a separate page.
- **Limit Posts**: Users can limit the number of posts displayed on the main page using query parameters.

## Technologies Used
- **Python**: The core programming language used for the backend.
- **Flask**: The web framework used to build the application.
- **Jinja2**: The templating engine used for rendering HTML.
- **dotenv**: Used for loading environment variables.
- **HTML/CSS**: For structuring and styling the web pages.

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd BlogsWeb
    ```
    
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    python flaskapp.py
    ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the main page.

## Routes
- **/**: The main page displaying a list of blog posts. You can limit the number of posts displayed by adding a `limit` query parameter, e.g., `/?limit=(0,5)`.
- **/blog/<post_num>**: Displays the details of a specific blog post identified by `post_num`.

## License
This project is licensed under the MIT License.