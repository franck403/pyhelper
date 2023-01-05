import code

cmd = code.utils()
ai = code.ai()
setting = ai.setting()

setting.log(False)
setting.optimise(True)
setting.bypass(True,5000)

ai.prepare()
ai.info()
ai.start(568, 400, 600,5000)
