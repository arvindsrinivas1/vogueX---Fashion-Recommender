import imp
from defer import return_value
from google_images_search import GoogleImagesSearch


class Config:
    def __init__(self) -> None:
        self.API_KEY = "AIzaSyDAm6ijCQKVo9w75JroZnU5nFMjI3SVP2Y"
        self.PROJ_CX = "525f979309bbd4a07"


class QueryBuilder:
    def __init__(self) -> None:
        pass

    def getQueryString(self, queries):
        return_query_string = ""
        for q in queries:
            return_query_string += q + " "

        return return_query_string


class SearchImages:
    def __init__(self) -> None:
        self.config = Config()
        self.gis = GoogleImagesSearch(self.config.API_KEY, self.config.PROJ_CX)
        self.default_num_of_records = 10
        self.query_builder = QueryBuilder()

    # gives the list of urls for a search
    def image_search(self, query_keywords, num_of_records=None):
        if not num_of_records:
            num_of_records = self.default_num_of_records

        query = self.query_builder.getQueryString(query_keywords)

        _search_params = {"q": query, "num": num_of_records}
        self.gis.search(search_params=_search_params)

        image_urls = []
        for image in self.gis.results():
            image_urls.append(image.url)
        return image_urls
