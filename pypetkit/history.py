from datetime import timedelta

class PetKitHistory:
    def __init__(self, history):
        self._history = history

    @property
    def id(self):
        return self._history["id"]

    @property
    def name(self):
        if self._history.get("name") is None:
            return "Snack"
        return self._history.get("name")

    @property
    def status(self):
        return self._history["status"]

    @property
    def isExecuted(self):
        return self._history["isExecuted"] == 1

    @property
    def time(self):
        return timedelta(seconds=self._history["time"])

    @property
    def realAmount(self):
        if self._history.get("state") is not None:
            return timedelta(seconds=self._history["state"]["realAmount"])
        return None

    @property
    def completedAt(self):
        if self._history.get("state") is not None:
            return timedelta(seconds=self._history["state"]["completedAt"])
        return None
    
    @property
    def error(self):
        if self._history.get("state") is not None:
          return "errCode" in self._history["state"]
        return False
