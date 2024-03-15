from abc import ABC, abstractmethod


class AbstractOperatorInterface(ABC):

    @abstractmethod
    def single_action(self):
        pass

    @abstractmethod
    def list_action(self):
        pass
