Assessment Task for Django Developer
========

This is Test Assignment submission for Back End Internship with IdeaToContent

Task
--------

- Weather Forecast App
- We need to create an application to display the weather forecast for a selected set of coordinates with selected type of detailing data. 
- User will require to enter lat and lon in the inputs and chose detailing type according to API.
- Unit and Integration Tests

## How to run
```bash
# Fetch the repo using git
git clone https://github.com/Rushijaviya/WeatherForecast.git

# Go to the directory
cd WeatherForecast

# Install a compatible version
pip install -r requirements.txt

# Database Migrations
python manage.py makemigrations

# Database Migrations
python manage.py migrate

# run command
python manage.py runserver

# Go to this url in browser
http://127.0.0.1:8000/

# For Testing
python manage.py test

# For testing API
http://127.0.0.1:8000/api/v1/get-weatherforecast-data
```

## API Details:
- URL: /api/v1/get-weatherforecast-data
- Request Type: GET
- Parameter: lon, lat, detailing_type

Note:
--------
- You need to add your API key inside ```settings.py``` file in ```WEATHER_API_KEY``` variable.
- You can use postman for testing API. 