## vionel-recommendations

### Requirements
Docker:
https://docs.docker.com/installation/

Docker compose:
https://docs.docker.com/compose/install/

---

#### Create/start databases
'''
(cd recommender_data && docker-compose up -d)
'''

#### Build containers
'''
docker-compose build
'''

#### Run a container
'''
docker-compose run recommender
'''

#### Attach to bash in a container
'''
docker-compose run recommender bash
'''

#### Logs
'''
docker-compose logs
'''

#### Scale (if that makes sense)
'''
docker-compose scale recommender=3
'''