"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/","VistController@index").name("index"),
        Get("/@","VistController@show").name("show"),
        Post("/","VistController@create").name("create"),
        Put("/@id","VistController@update").name("update"),
        Delete("/@id", "VistController@destroy").name("destroy")
    ],prefix="/trips",name="trips")
]
