#build docker
docker build -t my-flask-app .

#run container
docker run -d -p 5000:5000 --name flask-container my-flask-app
