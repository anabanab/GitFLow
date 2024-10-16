import subprocess


def mergeRelease(releaseVersion):
    try:
          subprocess.run("git", "checkout", "main")
          subprocess.run("git", "merge", f"release-{releaseVersion}")

          subprocess.run("git", "checkout", "develop")
          subprocess.run("git", "merge", f"release-{releaseVersion}")

    except Exception as error:
        return f"Ett fel uppstod{error}"