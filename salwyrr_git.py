# Salwyrr Minecraft Launcher simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
from sys import exit
import asyncio
import pathlib

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2023 [github.com/fahmiyufrizal]'
salwyrrFN = (r'Salwyrr_NetCafe_Launcher.exe')
salwyrrLN = path.expandvars(r'%appdata%\.Salwyrr\launcher\bootstrap\jre\bin\javaw.exe')
salwyrrLN_g = (r'Salwyrr\launcher\bootstrap\jre\bin\javaw.exe')
salwyrrLN_game = (r'Salwyrr\launcher')
dp0 = os.getcwd()
base_salwyrr = path.expandvars(r'%appdata%\.Salwyrr')
base_salwyrr_g = (r'Salwyrr')

#protection
if not path.exists (salwyrrFN):
	print(" [x] Don't change filename!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()