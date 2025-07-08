# FastAPI Notes App

A simple yet full-featured notes application built with FastAPI and MongoDB. This project demonstrates a complete CRUD (Create, Read, Update, Delete) functionality through a web interface rendered using Jinja2 templates.

---

## Features

-   **Create Notes:** Add new notes with a title, description, and an "Important" flag.
-   **View All Notes:** A clean, card-based layout on the homepage displays all saved notes.
-   **Update Notes:** Edit existing notes on a dedicated update page.
-   **Delete Notes:** Remove notes with a single click (includes a confirmation prompt).
-   **Responsive UI:** Styled with Bootstrap for a clean and responsive user experience on all devices.

---

## Technology Stack

-   **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
-   **Database:** [MongoDB](https://www.mongodb.com/) (using `pymongo`)
-   **Frontend:** [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) Templates, HTML, [Bootstrap](https://getbootstrap.com/)
-   **Server:** [Uvicorn](https://www.uvicorn.org/)

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   A running MongoDB instance (either local or a cloud service like [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/FastAPI-Notes-App.git](https://github.com/your-username/FastAPI-Notes-App.git)
cd FastAPI-Notes-App
````

### 3\. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

  - **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  - **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 4\. Install Dependencies

First, create a `requirements.txt` file with the necessary packages:

**`requirements.txt`**

```
fastapi
uvicorn[standard]
pymongo
python-multipart
jinja2
bson
```

Now, install them using pip:

```bash
pip install -r requirements.txt
```

### 5\. Configure Database

Open the `config/db.py` file and update the MongoDB connection string to point to your database instance.

```python
# example in config/db.py
from pymongo import MongoClient

# Replace with your MongoDB connection string
conn = MongoClient("mongodb://localhost:27017") 
```

### 6\. Run the Application

Start the development server using Uvicorn:

```bash
uvicorn index:app --reload
```

The application will be available at **http://127.0.0.1:8000**.

-----

## Project Structure

```
/
|-- config/
|   |-- db.py           # Database connection setup
|-- models/
|   |-- note.py         # Pydantic model for a Note
|-- routes/
|   |-- note_routes.py  # API routes for handling notes logic
|-- schemas/
|   |-- note.py         # Helper functions (e.g., noteEntity) for data transformation
|-- templates/
|   |-- index.html      # Homepage template to display and add notes
|   |-- update.html     # Template for the note update page
|-- index.py            # Main FastAPI application entrypoint
|-- requirements.txt    # Project dependencies
```

-----

## API Endpoints

The application exposes the following endpoints:

| Method | Path                  | Description                                  |
| :----- | :-------------------- | :------------------------------------------- |
| `GET`  | `/`                   | Displays all notes on the homepage.          |
| `POST` | `/`                   | Creates a new note from form data.           |
| `GET`  | `/update/{note_id}`   | Displays the page to update a specific note. |
| `POST` | `/update/{note_id}`   | Submits the updates for a specific note.     |
| `GET`  | `/delete/{note_id}`   | Deletes a specific note.                     |

---
