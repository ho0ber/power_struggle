#!/usr/bin/env python

import yaml
import valve.source.rcon
from ftplib import FTP

print("Loading config...")
with open("config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
print("Loaded.")

print("Uploading plugin...")
ftp = FTP(config["host"])
ftp.login(config["ftp_user"], config["ftp_password"])
ftp.cwd('1278528/ruste/server/1278528/oxide/plugins')

with open("PowerStruggle.py", "r") as upfile:
    ftp.storlines("STOR PowerStruggle.py", upfile)
ftp.quit()
print("Uploaded.")

# print("Reloading plugin on Rust server...")
# with valve.source.rcon.RCON((config["host"], config["rcon_port"]), config["rcon_password"]) as rcon:
#     try:
#         rcon.execute("oxide.reload PowerStruggle", .1)
#     except valve.source.rcon.NoResponseError:
#         pass
# print("Reloaded.")
# print("Done!")