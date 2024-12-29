# Building The Docker Image
```sh
docker build -t .
docker run -p 8501:8501 textcorrectionimg
```
# Pushing The Docker Image To The Registry
```sh
docker images
docker login
docker tag textcorrectionimg agarwalshaan/textcorrection:1.0
docker push agarwalshaan/textcorrection:1.0
```

# Pulling The Image From Docker Registry
```sh
docker pull agarwalshaan/textcorrection:1.0
```

# Running The Image Locally
```sh
docker run -p 8501:8501 agarwalshaan/textcorrection:1.0
```