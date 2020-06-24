import json
import requests

from datetime import datetime
from .schedule import PetKitSchedule
from .history import PetKitHistory
from .const import *

class PetKitDevice:
    def __init__(self, token, sensor):
      self._access_token = token
      self._sensor = sensor
      self._sensor["schedule"] = {}
      self._sensor["history"] = []
      for sh in sensor["feed"]["items"]:
          shd = PetKitSchedule(sh)
          self._sensor["schedule"][sh["id"]] = shd
      self.get_history(datetime.now().strftime("%Y%m%d"))

    @property
    def id(self):
        return self._sensor["id"]

    @property
    def name(self):
        return self._sensor["name"]

    @property
    def type(self):
        return self._sensor["type"]

    @property
    def batteryPower(self):
        return self._sensor["state"]["batteryPower"]

    @property
    def batteryStatus(self):
        return self._sensor["state"]["batteryStatus"]

    @property
    def desiccantLeftDays(self):
        return self._sensor["state"]["desiccantLeftDays"]

    @property
    def food(self):
        return return self._sensor["state"]["food"] == 1

    @property
    def feeding(self):
        return self._sensor["state"]["feeding"] == 1

    @property
    def schedule(self):
        return self._sensor["schedule"]

    @property
    def history(self):
        return self._sensor["history"]

    def get_history(self, day):
        params = {
            "deviceId": self._sensor["id"],
            "days": day
        }
        result = requests.post(
            API_FEEDERMINI_HISTORY_URL,
            data=params,
            headers={'X-Session': self._access_token}
        )
        try:
            for item in result.json()['result']:
                for history in item['items']:
                  self._sensor["history"].append(PetKitHistory(history))

        except (KeyError, TypeError) as err:
            _LOGGER.error(
                "Error requesting history from PetKit: {}".format(err)
            )
