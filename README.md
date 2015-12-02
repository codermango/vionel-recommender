## vionel-recommender

I modified the structure of this repository like vionel-sdk.

I still remained the docker configuration and now it is mainly for the deployment of MongoDB actually.

For the recommendation part, I use `setuptools` for distribution.

### Requirements
Docker:
https://docs.docker.com/installation/

Docker compose:
https://docs.docker.com/compose/install/

---

##Docker setup
#### Create/start databases
```
(docker-compose up -d)

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

---

## How to use
Actually you can use the package without docker as well.
Just clone the repository and run `sudo python setup.py install`
Then you can import the module as usual.

###Example

```
from cb_recommender.recommender import SimilarityRecommender
sr = SimilarityRecommender(media_type='movie', 
                           db_name='VionelMovies', 
                           collection_name='BoxerMovies', 
                           hostname='192.168.1.80', 
                           port=27017)
```
SimilarityRecommender is provided default parameters as above.
For now, if you want to test on tv series, set the parameter like this:
```
sr = SimilarityRecommender(media_type='tv', 
                           db_name='VionelMovies', 
                           collection_name='AllSeries', 
                           hostname='192.168.1.80', 
                           port=27017)
```

Function for recommendation
```
recommend(input_movies, num_of_recommended_movies)
```

This function will return a dictionary containing the similary movies with similarity score and which features the recommendation is based on.

Example return format:
```
{
                "movie": {
                            "tt0340855": 0.6837561795878957,
                            "tt1124035": 0.9627459173643833,
                         },
                "reason": {
                            "tt0340855": {
                                  "imdbDirector": 0,
                                  "brightness": 0.025,
                                  "locationCountry": 0.21213203435596423,
                                  "vionelTheme": 0.13,
                                  "RGB": 0.0625,
                                  "locationCity": 0.20412414523193148,
                                  "wikiKeyword": 0,
                                  "imdbGenre": 0.05,
                                  "vionelScene": 0,
                                  "imdbMainactor": 0,
                                  "imdbKeyword": 0
                                },
                            "tt1124035": {
                                  "imdbDirector": 0,
                                  "brightness": 0,
                                  "locationCountry": 0.21213203435596423,
                                  "vionelTheme": 0,
                                  "RGB": 0.0625,
                                  "locationCity": 0.15811388300841897,
                                  "wikiKeyword": 0.13,
                                  "imdbGenre": 0.05,
                                  "vionelScene": 0.35,
                                  "imdbMainactor": 0,
                                  "imdbKeyword": 0
                        }
            }
``` 

If you just want to see the demo, just visit `http://192.168.1.80`. I will provide options for choosing 'movie' or 'tv' recommendation soon.



