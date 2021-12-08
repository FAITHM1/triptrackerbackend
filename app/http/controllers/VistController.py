""" A VistController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Vist import Vist

class VistController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", VistController)
        """
        id = self.request.param("id")
        return Vist.find(id)
        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", VistController)
        """
        return  Vist.all()

        pass

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", VistController)
        """
        place = self.request.input("place")
        description = self.request.input("description")
        goingWith = self.request.input("goingWith")    
        tripNotes = self.request.input("tripNotes")
        complete = self.request.input("complete")
        typ = self.request.input("type")
        date = self.request.input("date")
        vist = Vist.create({"place" : place,"description": description,"goingWith": goingWith,"tripNotes": tripNotes,"complete": complete,"type":typ,"date": date})
        return vist

        pass



    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", VistController)
        """
        place = self.request.input("place")
        description = self.request.input("description")
        goingWith = self.request.input("goingWith")    
        tripNotes = self.request.input("tripNotes")
        complete = self.request.input("complete")
        typ = self.request.input("type")
        date = self.request.input("date")
        id = self.request.param("id")
        Vist.where("id",id).update({"place" : place,"description": description,"goingWith": goingWith,"tripNotes": tripNotes,"complete": complete,"type":typ,"date": date})
        return  Vist.where("id",id).get()
        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", VistController)
        """
        id = self.request.param("id")
        vist = Vist.where("id",id).get()
        Vist.where("id",id).delete()
        return vist

        pass