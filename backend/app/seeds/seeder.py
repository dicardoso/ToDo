# pylint: disable=line-too-long,too-many-locals,too-many-branches,broad-except,too-many-statements,no-else-raise
"""This module runs seeds"""

from .seed_user import seeds as user_seed


class Seeds:
    """This class runs seeds"""

    def __init__(self, database, modules):
        self.session = database.session
        self.modules = modules

    def run(self):
        """This method runs seeds"""
        users = self.modules.user.User

        users = user_seed(users)
        try:
            print("Getting Started First Seeds ...")
            self.session.add_all(users)
            print("Successfully inserted data from First Seed")
        except Exception as error:
            self.session.rollback()
            print(f"Error: {error}")
            raise
        else:
            self.session.commit()

        self.session.close()
