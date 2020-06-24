from datetime import timedelta

class PetKitSchedule:
    def __init__(self, schedule):
        self._schedule = schedule

    @property
    def id(self):
        return self._schedule["id"]

    @property
    def name(self):
        return self._schedule["name"]

    @property
    def amount(self):
        return self._schedule["petAmount"][0]["amount"]

    @property
    def time(self):
        return timedelta(seconds=self._schedule["time"])