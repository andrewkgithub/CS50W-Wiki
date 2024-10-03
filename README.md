# CS50W Wiki Project

This project is a Wikipedia-like online encyclopedia built as part of the CS50 Web Programming with Python and JavaScript (CS50W) course. It allows users to create, edit, and view encyclopedia entries written in Markdown, which are then converted to HTML and displayed on the website.

## Project Structure

The project consists of the following main components:

- **encyclopedia/**: Contains the Django app for managing encyclopedia entries.
  - `static/`: Stores static files like CSS for the project.
  - `templates/`: Contains the HTML templates used for rendering pages.
    - `create.html`: Template for creating new encyclopedia entries.
    - `edit.html`: Template for editing existing encyclopedia entries.
    - `entry.html`: Template for viewing an encyclopedia entry.
    - `error.html`: Template for showing error messages.
    - `index.html`: The main index page that lists all encyclopedia entries.
    - `layout.html`: The base layout that all templates extend.
    - `search_results.html`: Displays search results when a user searches for an entry.
  - `views.py`: Contains the logic for handling requests and rendering templates.
  - `urls.py`: Defines the URL patterns for the encyclopedia app.
  - `util.py`: Contains helper functions for interacting with Markdown files.

- **entries/**: Stores all encyclopedia entries as Markdown files.

- **wiki/**: The overall Django project configuration.

- `db.sqlite3`: The SQLite database file.

- `manage.py`: The Django command-line utility for administrative tasks.

## Features

1. **Entry Page**: 
   - Users can view an encyclopedia entry by visiting `/wiki/<entry_title>`. If the entry exists, it is displayed in HTML format. If the entry does not exist, an error page is shown.

2. **Index Page**: 
   - Displays a list of all encyclopedia entries. Users can click on any entry to view its contents.

3. **Search**: 
   - Users can search for encyclopedia entries. If a match is found, the user is taken to the corresponding entry. If no match is found, the user is presented with a list of entries that contain the search query as a substring.

4. **Create New Page**: 
   - Users can create a new encyclopedia entry by providing a title and content in Markdown format. If an entry with the same title already exists, an error message is displayed.

5. **Edit Page**: 
   - Users can edit the content of an existing encyclopedia entry. The page is pre-populated with the current content of the entry in Markdown format.

6. **Random Page**: 
   - Users can click the "Random Page" link to be taken to a randomly selected encyclopedia entry.

7. **Markdown to HTML Conversion**: 
   - All entries are written in Markdown but are converted to HTML before being displayed to the user.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/andrewkgithub/wiki.git

2. Install the required dependencies:
   pip install django markdown2

3. Run the Django development server:
   python manage.py runserver

4. Open your browser and navigate to http://127.0.0.1:8000/ to view the project.
