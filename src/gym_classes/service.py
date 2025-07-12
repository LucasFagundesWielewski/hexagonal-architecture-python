from bson.objectid import ObjectId
from pymongo.database import Database

from src.gym_classes.errors import GymClassNotFoundError
from src.gym_classes.models import GymClass, CreateOrUpdateClass

class GymClassService:
    def __init__(self, db: Database) -> None:
        self._collection = db.get_collection("gym_classes")

    def get_class(self, class_id: ObjectId) -> GymClass:
        document = self._collection.find_one({"_id": class_id})
    
        if not document:
            raise GymClassNotFoundError(f"Gym class with ID {class_id} not found.")
        
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
        return GymClass(**document)
    
    def get_all(self) -> list[GymClass]:
        gym_classes = []
        documents = self._collection.find({})
        for document in documents:
            document["_id"] = str(document["_id"])
            gym_classes.append(GymClass(**document))

        days_order = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7
        }

        return sorted(gym_classes, key=lambda x: days_order[x.day_of_week])
    
    def create_class(self, class_data: CreateOrUpdateClass) -> GymClass:
        document = class_data.dict()
        result = self._collection.insert_one(document)

        return self.get_class(result.inserted_id)
    
    def update(self, class_id: str, class_data: CreateOrUpdateClass) -> GymClass:
        gym_class = self.get_class(ObjectId(class_id))
        gym_class.name = class_data.name
        gym_class.day_of_week = class_data.day_of_week
        gym_class.start_time = class_data.start_time
        gym_class.coach = class_data.coach
        gym_class.description = class_data.description

        new_values = gym_class.dict()
        del new_values["_id"]  # Remove _id to avoid update issues

        self._collection.update_one({"_id": ObjectId(class_id)}, {"$set": new_values})
        return gym_class
    
    def delete(self, gym_class_id: str) -> None:
        self._collection.delete_one({"_id": ObjectId(gym_class_id)})
