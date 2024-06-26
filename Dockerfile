FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*

# install app
COPY allmembers.py /

# Set the working directory
WORKDIR /

# final configuration
ENV FLASK_APP=allmembers.py
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]