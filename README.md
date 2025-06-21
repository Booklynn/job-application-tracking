# Job Application Tracking
A simple Flask web application to create and manage your job application list.

## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)

## Installation

This project requires Python 3.9 or newer and Flask.

1. Clone the repository:

```bash
git clone https://github.com/username/project.git
cd project
```
2. Create a virtual environment:

- Windows
```bash
python -m venv venv
venv\Scripts\activate
```
- Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
flask db upgrade
```

## Usage

Run the local development application with:

```bash
python run.py
```

To seed data, create **instance/config.py** with the following content:

```python
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_ROLE = 'Admin'
ADMIN_PASSWORD = 'supersecretpassword1'
```

Then run
```bash
python seed_data.py
```