# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /home/debian/app

# Copy the current directory contents into the container at /app
COPY app/mypython.py ./ #source path is relative

# Run a Python script when the container launches
CMD ["python", "./mypython.py"]
