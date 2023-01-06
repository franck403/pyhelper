import code_1

# var call
cmd = code_1.utils()
ai = code_1.ai()
setting = ai.setting()

# set up the setting
setting.log(False)
setting.optimise(True)
setting.bypass(True,5000)

# Start the ai
ai.prepare()
ai.info()
ai.start(568, 400, 600,5000)
