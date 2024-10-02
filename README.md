## ML model deployment example
===========================

Complete code of the final project  to deploy and inference a machine learning model (built on the iris dataset) using Docker and FastAPI.

1. ### With terminal navigate to the root of this repository
--------------------------------------------------------

2. ### Build docker image
---------------------
```
    docker build -t ban6800_final .

```

3. ### Run container
----------------
```
    docker run --name nexford -p 8000:8000 ban6800_final

```


4. ### Output will contain
----------------------
`Uvicorn running on http://0.0.0.0:8000`


5. Visit the app on the browser via (price prediction)[https://final-project-57q2.onrender.com/] to get the predictions.
