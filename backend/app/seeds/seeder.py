# pylint: disable=line-too-long,too-many-locals,too-many-branches,broad-except,too-many-statements,no-else-raise
"""This module runs seeds"""

from .seed_categories import seeds as categories_seed
from .seed_labels import seeds as labels_seed
from .seed_task_status import seeds as task_status_seed
from .seed_user import seeds as user_seed


class Seeds:
    """This class runs seeds"""

    def __init__(self, database, modules):
        self.session = database.session
        self.modules = modules

    def run(self):
        """This method runs seeds"""
        categories = self.modules.categories.Category
        labels = self.modules.labels.Label
        task_status = self.modules.task_status.TaskStatus
        users = self.modules.user.User

        categories = categories_seed(categories)
        labels = labels_seed(labels)
        task_status = task_status_seed(task_status)
        users = user_seed(users)
        try:
            print("Getting Started First Seeds ...")
            self.session.add_all(categories)
            self.session.add_all(labels)
            self.session.add_all(task_status)
            self.session.add_all(users)
            print("Successfully inserted data from First Seed")
        except Exception as error:
            self.session.rollback()
            print(f"Error: {error}")
            raise
        else:
            self.session.commit()

        self.session.close()
