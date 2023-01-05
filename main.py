import code

# var call
cmd = code.utils()
ai = code.ai()
setting = ai.setting()

# set up the setting
setting.log(False)
setting.optimise(True)
setting.bypass(True,5000)

# Start the ai
ai.prepare()
ai.info()
ai.start(568, 400, 600,5000)
