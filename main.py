import code_1

# var call
cmd = code_1.utils()
ai = code_1.ai()
setting = ai.setting()

# code to test
cusbar = code_1.bar.custombar.fonction()
cusbar.prepare("Teste",10)
cusbar.codeer("wait","import time\ntime.sleep(0.1)")
cusbar.codeer("start","print('hi')")
cusbar.codeer("next","import code_1\ndic = code_1.bar.custombar.fonction()\nprint('|' + dic.repeat('#',dic.acrange()) + dic.repeat('-',dic.rerange()) + '|')\n")
cusbar.run("start")
cusbar.run("next")
cusbar.run("next")
cusbar.run("next")
quit()

# set up the setting
setting.log(False)
setting.optimise(True)
setting.bypass(True,5000)

# Start the ai
ai.prepare()
ai.info()
ai.start(568, 400, 600,5000)
