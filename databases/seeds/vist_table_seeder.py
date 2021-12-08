"""VistTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Vist import Vist

class VistTableSeeder(Seeder):
    def run(self):
        Vist.create({"place" : "newyork","description": "okay dddjnfjfnhhf","goingWith": "Zari","tripNotes" : "bring your food","complete": False,"type":"winter", "date": "jan 14"})
        """Run the database seeds."""
        pass
