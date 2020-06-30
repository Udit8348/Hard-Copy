import os

################
# BEGIN CONFIG #
################

ROBOT_NAME = 'PSU 2020-2021 Unified Robot'
ROBOT_NAME_SHORT = 'psu'
# change IMG_LOCATION if you prefer to use a different image or one hosted at a different link
IMG_LOCATION = f'./docs/controller.png'
DOCS_PATH = f'./docs/{ROBOT_NAME_SHORT}_key_bindings.md'
# update this constants path to reflect where you saved your constants.h file
CONSTANTS_PATH = f'./include/{ROBOT_NAME_SHORT}/constants.h'

##############
# END CONFIG #
##############

os.system(f"rm -rf {DOCS_PATH}")
os.system(f"touch {DOCS_PATH}")
source = open(f"{CONSTANTS_PATH}")

arrows = ["down", "left", "up", "right"]
bumpers = ["R1", "L1", "R2", "L2"]
letters = ["Y", "X", "A", "B"]

bindings = {}

for line in source.readlines():
    if "ControllerDigital" in line:
        line = line.strip().replace("const auto ", "").split(" = okapi::ControllerDigital::", 1)
        command = line[0]
        command_list = command.split("_")
        command = " ".join(command_list).lower()
        button = line[1].split(";", 1)[0]
        bindings[button] = command

source.close()

with open(f'{DOCS_PATH}', 'a') as output_file:
    output_file.write(f"# Key bindings for {ROBOT_NAME}\n")
    output_file.write(f"![Controller]({IMG_LOCATION})\n")
    output_file.write("\n## Button mappings\n")
    output_file.write("### Bumpers (1-4), Joysticks (5-6), Arrows (7-10), Letters (11-14)\n")

    for (i, button) in enumerate(bumpers):
        output_file.write(f"{i}. {button}: ")
        if button in bindings:
            output_file.write(f"{bindings[button]}")
        else:
            output_file.write("N/A")
        output_file.write("\n")

    output_file.write("5. Left Joystick: left side drive motors\n")
    output_file.write("6. Right Joystick: right side drive motors\n")

    for i, button in enumerate(arrows, start=7):
        output_file.write(f"{i}. {button}: ")
        if button in bindings:
            output_file.write(f"{bindings[button]}")
        else:
            output_file.write("N/A")
        output_file.write("\n")

    for i, button in enumerate(letters, start=11):
        output_file.write(f"{i}. {button}: ")
        if button in bindings:
            output_file.write(f"{bindings[button]}")
        else:
            output_file.write("N/A")
        output_file.write("\n")
