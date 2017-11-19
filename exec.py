import cx_Freeze

executables = [cx_Freeze.Executable("Military_training_v.1.py")]

cx_Freeze.setup(
    name="YOU MUST TRAIN!!!",
    options={"build_exe": {"packages":["pygame",],
                           "include_files":["plane.png",
                                           "background.png"]}},
    executables = executables
    )
