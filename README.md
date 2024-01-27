# TimesWorld Onboarding System

Welcome to TimesWorld Onboarding System! This system allows users to register and onboard themselves.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

TimesWorld Onboarding System is a web application designed to facilitate user registration and onboarding for TimesWorld employees.

## Features

- User-friendly registration form
- Onboard users with essential information
- Role-based access and dashboard
- 

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Postgresql

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/timesworldonboarding.git
   cd timesworld-

 ## RUN the following commands
2. pip install -r requirements.txt

3. Create a database in PostgreSQL.

4. Change the file name of 'ENV.txt' to '.env' and place your credentials

5. python manage.py migrate

6. python manage.py runserver

The Application will be accessible at http://localhost:8000/.

### Usage

1. Navigate to http://localhost:8000/ in your web browser.
2. Register and fill out the Onboarding form.(The First name should not contain special characters
    the password must be minimum length of 6 )
3. Login with your usarname(email) & password
4. Access your dashboard based on your assigned role.

## License
This project is licensed under the MIT License.





