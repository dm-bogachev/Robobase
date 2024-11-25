# Use the official Python image.
FROM python:3.9

# Set the working directory.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app/
# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container.
EXPOSE 8000

# Run the application.
#CMD ["mysqld", "--character-set-server=utf8", "--collation-server=utf8_unicode_ci"]

CMD ["python", "-Xutf8", "manage.py", "runserver", "0.0.0.0:80"]
