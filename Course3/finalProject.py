import requests_with_caching
import json

def get_movies_from_tastedive(search):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= search
    params_d["type"]= "movies"
    params_d["limit"] = "5"
    resp = requests_with_caching.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic

def extract_movie_titles(dict):
    result=[]
    for Res in dict['Similar']['Results']:
        result.append(Res['Name'])
    return result

def get_related_titles(movieList):
    similarList = []
    testList = []
    for movie in movieList:
        testList = extract_movie_titles(get_movies_from_tastedive(movie))
        for movieNametest in testList:
               if movieNametest not in similarList:
                    similarList.append(movieNametest)
    return similarList

def get_movie_data(str):
    baseurl="http://www.omdbapi.com/"
    params_d = {}
    params_d["t"]= str
    params_d["r"]= "json"
    resp = requests_with_caching.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic

def get_movie_rating(movieNameJson):
    strRating=""
    for typeRatingList in movieNameJson["Ratings"]:
        if typeRatingList["Source"]== "Rotten Tomatoes":
            strRating = typeRatingList["Value"]
    if strRating != "":
        rating = int(strRating[:2])
    else: rating = 0
    return rating

def get_sorted_recommendations(movieList):
    listMovie = get_related_titles(movieList)
    listMovie = sorted(listMovie, key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)

    return listMovie
