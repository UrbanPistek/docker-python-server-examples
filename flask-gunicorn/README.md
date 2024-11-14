# Example: Flask-Gunicorn Server

### Routes

```
/
/routes
/sample_get
/sample_post
```
### Usage

> /sample_get
```
curl 0.0.0.0:7711/sample_get
```

> /sample_post
```
curl --header "Content-Type: application/json" --request POST --data '{"msg": "hello there"}' 0.0.0.0:7711/sample_post
```

### Build

Build image:

```
docker build --tag py-flask-gunicorn .
```

Run:

```
docker run --name py-flask-service py-flask-gunicorn
```

With docker compose (build & run):

```
docker compose up
```

