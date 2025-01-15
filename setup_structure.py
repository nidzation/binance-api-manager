import os

def create_folders_and_files():
    # Define folder structure
    folders = [
        "templates",    # For HTML templates
        "static",       # For CSS and JS files
        "static/css",   # CSS files
        "static/js",    # JavaScript files
        "config",       # Configuration files like .env
        "logs",         # Log files
    ]

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Folder created: {folder}")

    # Create necessary files
    files = {
        "templates/index.html": "<!-- Placeholder for index.html -->",
        "static/css/styles.css": "/* Placeholder for styles.css */",
        "static/js/script.js": "// Placeholder for script.js",
        "config/.env": "# Placeholder for .env configuration\n",
        "server.py": "# Placeholder for server logic\n",
    }

    for file_path, content in files.items():
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File created: {file_path}")

if __name__ == "__main__":
    create_folders_and_files()
