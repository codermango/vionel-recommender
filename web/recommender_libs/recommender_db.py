import pymongo
from pymongo import MongoClient
import json
import os


class RecommenderDB:

    def __init__(self):
        db_host = os.environ.get('MONGO_PORT_27017_TCP_ADDR', 27017)
        client = MongoClient(db_host)
        self.db = client.VionelMovies
        self.boxerMoviesCollection = self.db.boxerMovies
        

    def get_all_feature_list(self, feature_name):
        feature_list = []
        feature_dict_list = self.boxerMoviesCollection.find({}, {feature_name: 1, "_id": 0})
        for feature_dict in feature_dict_list:
            try:
                feature_list += feature_dict[feature_name]
            except KeyError:
                continue
        feature_list = list(set(feature_list))
        # print feature_list
        return feature_list


    def get_imdbid_feature_dict(self, feature_name):
        result_dict = {}

        all_movies_feature_dict_list = self.boxerMoviesCollection.find({}, {"imdbId": 1, feature_name: 1, "_id": 0})
        
        for movie in all_movies_feature_dict_list:
            imdbid = movie["imdbId"]
            try:
                feature = movie[feature_name]
                result_dict[imdbid] = feature
            except KeyError:
                continue
        # print result_dict
        return result_dict


    def get_feature_featurenum_dict(self, feature_name):
        result_dict = {}
        # get all the features
        feature_list = self.get_all_feature_list(feature_name)

        all_feature_dict_list = self.boxerMoviesCollection.find({}, {feature_name: 1, "_id": 0})
        all_feature_list = []
        for movie in all_feature_dict_list:
            try:
                feature = movie[feature_name]
                all_feature_list += feature
            except KeyError:
                continue
        all_feature_list = list(set(all_feature_list))

        count = 0
        for feature_id in all_feature_list:
            count += 1
            print feature_id, count
            documents = self.boxerMoviesCollection.find({feature_name: feature_id})
            feature_num = documents.count()
            result_dict[feature_id] = feature_num

        return result_dict



    def create_feature_num_collection(self):

        rgb_dict = self.get_feature_featurenum_dict("RGB")
        brightness_dict = self.get_feature_featurenum_dict("Brightness")
        genre_dict = self.get_feature_featurenum_dict("imdbGenres")
        director_dict = self.get_feature_featurenum_dict("imdbDirectors")
        imdbkeyword_dict = self.get_feature_featurenum_dict("imdbKeywords")
        wikikeyword_dict = self.get_feature_featurenum_dict("wikiKeywords")
        vioneltheme_dict = self.get_feature_featurenum_dict("vionelThemes")
        vionelscene_dict = self.get_feature_featurenum_dict("vionelScene")
        locationcountry_dict = self.get_feature_featurenum_dict("locationCountry")
        locationcity_dict = self.get_feature_featurenum_dict("locationCity")
        mainactor_dict = self.get_feature_featurenum_dict("imdbMainactors")
        

        result_dict = {}
        result_dict["imdbGenres"] = genre_dict
        result_dict["imdbDirectors"] = director_dict
        result_dict["imdbKeywords"] = imdbkeyword_dict
        result_dict["wikiKeywords"] = wikikeyword_dict
        result_dict["vionelThemes"] = vioneltheme_dict
        result_dict["vionelScene"] = vionelscene_dict
        result_dict["locationCountry"] = locationcountry_dict
        result_dict["locationCity"] = locationcity_dict
        result_dict["imdbMainactors"] = mainactor_dict
        result_dict["RGB"] = rgb_dict
        result_dict["Brightness"] = brightness_dict

        with open("feature_num.json", "w") as feature_num_file:
            result_dict_json = json.dumps(result_dict)
            feature_num_file.write(result_dict_json)


# if __name__ == '__main__':
#     recommenderdb = RecommenderDB()
#     recommenderdb.create_feature_num_collection()