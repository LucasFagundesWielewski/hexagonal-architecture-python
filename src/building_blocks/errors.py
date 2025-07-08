from pydantic import BaseModel

class DomainError(Exception):
    pass

class ResourceNotFoundError(DomainError):
    pass

class RepositoryError(DomainError):
    @classmethod
    def save_operation_failed(cls) -> "RepositoryError":
        return cls("Save operation failed")
    
    @classmethod
    def get_operation_failed(cls) -> "RepositoryError":
        return cls("Get operation failed")
    
class APIErrorMessage(BaseModel):
    message: str
    type: str