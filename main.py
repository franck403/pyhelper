import code_1

# var call
cmd = code_1.utils()
ai = code_1.ai()
setting = ai.setting()

# code to test
cusbar = code_1.bar.custombar.fonction()
cusbar.prepare("Teste",150)
cusbar.codeer("wait","import time\ntime.sleep(0.1)")
cusbar.codeer("next",'''import code_1\ndic = code_1.bar.custombar.fonction()\nprint("Computing |" + dic.repeat('#',dic.acrange()) + dic.repeat('-',dic.rerange()) + '|')''')
cusbar.codeer("loop","import code_1\nimport time\ndic = code_1.bar.custombar.fonction()\ncusbar = code_1.bar.custombar.fonction()\nloop_range = dic.getsrange()\nfor i in range(loop_range):\n   cusbar.run('next')\n   time.sleep(0.1)")
cusbar.run("loop")
quit()

# set up the setting
setting.log(False)
setting.optimise(True)
setting.bypass(True,5000)

# Start the ai
ai.prepare()
ai.info()
ai.start(568, 400, 600,5000)
