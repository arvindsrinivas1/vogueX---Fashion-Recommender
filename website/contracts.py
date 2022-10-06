class ErrorCodes:
    USER_NOT_LOGGED_IN = 1
    OBJECT_NOT_SAVED = 2

class SessionParameters:
    USERID = 'userid'

class RecommendationContractRequest:
    #### RECOMMENDATION PAYLOAD FIELDS
    OCCASION_KEY = "occasion"
    CITY_KEY = "city"

class RecommendationContractResponse:
    LINKS  = "links"

class PreferenceContractRequest:
    PREFERENCES = "preferences"
    