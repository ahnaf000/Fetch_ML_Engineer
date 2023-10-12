# Fetch-ML-Engineer
This is the solution of the take home test for the Fetch Rewards Machine Learning Engineer position, completed by Ahnaf .


## View EDA Findings and Model Building Details
Open the notebook to [View the Exploratory Data Analysis Notebook](./notebook/playground.ipynb)


## Run Dockerized Apps:
docker build . -t jupyter_server
docker run -it -p 8080:8080 -v .:/app jupyter_server