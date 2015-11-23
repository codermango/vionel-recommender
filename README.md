## vionel-recommendations

### Requirements
Docker:
https://docs.docker.com/installation/

Docker compose:
https://docs.docker.com/compose/install/

---

#### RECOMMENDER_DATA IS FOR DB SPECIFICATION USED DURING DEVELOPMENT ONLY!
never commit any data whatsoever to git directly

---


#### Create/start databases
```
(cd recommender_data && docker-compose up -d)
```

#### Build containers
```
docker-compose build
```

#### Run a container
```
docker-compose run --rm recommender
```

#### Attach to bash in a container
```
docker-compose run --rm recommender bash
```

#### Logs
```
docker-compose logs
```

#### Scale (if that makes sense)
```
docker-compose scale recommender=3
```