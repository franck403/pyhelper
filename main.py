import code_1

# var call
cmd = code_1.utils()
ai = code_1.ai()
setting = ai.setting()

# code to test
cusbar = code_1.bar.custombar.fonction()
cusbar.prepare("Teste",10)
cusbar.codeer("advence","dictinary = {'acutal_range':'0'}")
cusbar.codeer("start","print('hi')")
cusbar.codeer("next","import code_1\ndic = code_1.bar.custombar.fonction()\ndic.acrange()\nprint('hi 2')\n")
cusbar.run("start")
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
