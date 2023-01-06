import abc
from typing import List

from app.domain.vote import Vote

class VoteRepository(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def add(self, vote: Vote) -> Vote:
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def all(self)->List[Vote]:
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def total(self)->int:
        raise NotImplementedError