# Install dependencies
FROM ubuntu:22.04
RUN apt-get update; apt-get install -y wget python3-pip 
RUN pip3 install jupyterlab==3.4.5 numpy pandas matplotlib seaborn

# Set the working directory in the container
WORKDIR /app

# Copy the current directory content into the container
# COPY  . .

# Launch the Jupyterlab server
CMD ["python3", "-m", "jupyterlab", "--no-browser", "--ip=0.0.0.0", "--port=8080", "--NotebookApp.token='local'", "--NotebookApp.password='local'", "--allow-root"]