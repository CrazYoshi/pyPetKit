import hashlib
import json
import logging
import requests
from datetime import datetime, timedelta

from .const import (
    API_LOGIN_URL,
    API_FEEDERMINI_DEVICE_URL
)
from .device import PetKitDevice
from .history import PetKitHistory

_LOGGER = logging.getLogger(__name__)


class PetKitAPI:
    def __init__(self, user, password, access_token=None):
        """ Initialize PetKit API """
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        self._user = user
        self._password = hash.hexdigest()
        self._access_token = access_token
        self._expiration_date = datetime.utcnow()
        self.feeders = {}

    @property
    def is_authorized(self):
        return self._expiration_date < datetime.utcnow()

    def get_all_devices(self):
        """Populate all devices in the PetKit account."""
        if is_authorized() == False:
            request_token()
        
        result = requests.get(
            API_FEEDERMINI_DEVICE_URL,
            headers={'X-Session': self._access_token}
        )
        try:
            for item in result.json()['result']:
                feeder = PetKitDevice(self._access_token, item)
                self.feeders[feeder.id] = feeder

        except (KeyError, TypeError) as err:
            _LOGGER.error(
                "Error requesting device from PetKit: {}".format(err)
            )

    def request_token(self):
        """Request access and refresh tokens from PetKit."""
        params = {
            "username": self._user,
            "password": self._password,
            "encrypt": 1,
        }

        result = requests.post(API_LOGIN_URL, data=params)
        try:
            createdAt = datetime.strptime(
                result.json()['result']['session']['createdAt'],
                '%Y-%m-%dT%H:%M:%S.%fZ'
            )
            self._access_token = result.json()['result']['session']['id']
            self._expiration_date = createdAt + timedelta(
                seconds=result.json()['result']['session']['expiresIn']
            )
            _LOGGER.debug(
                "Obtained access token {} and expiration datetime {}".format(
                    self._access_token, self._expiration_date
                )
            )
        except (KeyError, TypeError) as err:
            _LOGGER.error("Error requesting token from PetKit: {}".format(err))

    def get_token(self):
      return self._access_token
    
    def getSensors(self):
        return self.feeders