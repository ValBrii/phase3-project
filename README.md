# Phase3-project
This project is about a simple notes app which helps the user keep track of things that they want to note down. It can be something that they want to do or even something like a shopping list.

## Features
- The user can add a new note
- View existing notes
- Delete notes

## Technologies used
- Python

## Instructions for setting up the project locally
1. **Install nodejs**
1. **Fork the repository**
2. **Clone the repository**
```bash
git clone git@github.com:ValBrii/phase3-project.git
```
3. **Navigate to the project directory**
```bash
cd phase3-project
```
4. **Run code . to view the files**


### Running the Application

1. To add a new category, run:
    ```bash
    python main.py add-category --name "<category_name>"
    ```
2. To view all categories, run:
    ```bash
    python main.py list-categories
    ```
3. To add a new note under a category, run:
    ```bash
    python main.py add-note --title "<note_title>" --content "<note_content>" --category_id <category_id>
    ```
4. To view all notes, run:
    ```bash
    python main.py list-notes
    ```
5. To delete a note, run:
    ```bash
    python main.py delete-note --note-id <note_id>
    ```




## Contributions
All contributions are welcome.
To contribute to this project, follow the following steps
1. Fork the repo
2. create a new branch 

```bash
git checkout -b feature/yourfeature
```
3. Commit your changes 

```bash 
git commit -m "Add a new feature"
```

4. Push to the branch
``` bash
git push origin feature/YourFeature 
```

5. Open a pull request

## License
Distributed under MIT license


## Contact Information
britneyvalerie85@gmail.com
