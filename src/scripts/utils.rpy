init 1 python:

    import subprocess as sp
    import shutil as shell
    import requests as rq
    import os

    # This function is a small shortcut for
    # checking if the binary executable exists in system.
    # Not sure if it will work on windows, but it will on Linux and MacOS.
    def soh_CheckBinary(name: str):
        return shell.which(name) is None

    # This function fetches updates for mod repository
    # Returns True if there is, and False if there is no.
    def soh_FetchUpdates():
        pass