init 1 python:

    import subprocess as sp
    import shutil as shell
    import requests as rq
    import os


    # This function fetches updates for mod repository
    # Returns True if there is, and False if there is no.
    def soh_FetchUpdates():
        if not soh_IsNonSteam(): return

        try:
            content = rq.get("https://raw.githubusercontent.com/nitrogenez/soh-desktop/master/src/glob.rpy")
        except rq.ConnectionError as e:
            return False

        for i in content.text.split("\n"):
            if "VERSION" in i:
                fetched = i.strip().replace("VERSION = ", "").replace("\"", "")

        print("Fetched version. Currently installed: v%s; New: v%s" % (soh_Globals.VERSION, fetched))

        fetched_ver_split = fetched.split(".")
        current_ver_split = soh_Globals.VERSION.split(".")

        major = int(current_ver_split[0])
        minor = int(current_ver_split[1])
        cmajor = int(fetched_ver_split[0])
        cminor = int(fetched_ver_split[1])

        print("Current version array: %s" % current_ver_split)
        print("New version array: %s" % fetched_ver_split)

        if (major < cmajor):
            print("Found newer version: %s" % fetched)
            return True

        elif (minor < cminor):
            print("Found newer version: %s" % fetched)
            return True

        else:
            print("Modification is Up-to-Date")
            return False


    # This function will install updates for mod from repo.
    def soh_InstallUpdates():
        if not soh_IsNonSteam(): return
        if not soh_CheckBinary("git"): return

        git_out = sp.check_output(["git", "pull"])

        if git_out == "Already up to date.":
            return 0
        if "error" in git_out:
            return 1
        else:
            return 2


    # This function is a small shortcut for
    # checking if the binary executable exists in system.
    # Not sure if it will work on windows, but it will on Linux and MacOS.
    def soh_CheckBinary(name):
        return shell.which(name) is None


    # This function returns True if soh_Globals::BUILDTYPE is nonsteam
    def soh_IsNonSteam():
        return "nonsteam" in soh_Globals.BUILDTYPE


    # This function returns True if modification was cloned/downloaded directly from Git
    # and wasn't built for Steam or other platform
    def soh_IsGit():
        return os.exists("mods/soh-desktop/.git")
