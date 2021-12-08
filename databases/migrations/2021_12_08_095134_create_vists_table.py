"""CreateVistsTable Migration."""

from masoniteorm.migrations import Migration


class CreateVistsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("vists") as table:
            table.increments("id")
            table.string("place")
            table.string("description")
            table.string("goingWith")
            table.string("tripNotes")
            table.boolean("complete")
            table.string("type")
            table.string("date")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("vists")
