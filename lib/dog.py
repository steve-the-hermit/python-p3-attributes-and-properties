#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, job):
        self._name = None  # Initialize to None
        self._job = None  # Initialize to None
        self.name = name  # Use the property setter
        self.job = job  # Use the property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

    pass
