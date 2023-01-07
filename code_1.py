console = False
consolek = False
bypass = False
bardesc = "Computing"
barrange = "#"
srange = 0
nrange = 0
bspace = 10
svrange = 0
bactive = False
lprint = 0
gcode = "none"
gurl = "none"
customdic = {"desc": "Computing", "range": 1000, "actual_range": 0}
customcode = {"desc":"Computing"}

class coder():
    def code(self,code_name,code):
        global customcode
        customcode[code_name] = code
    def run(self,code_name,method="exec"):
        global customcode
        if method == "exec":
            try:
                exec(customcode[code_name]) 
            except:
                colors.Red("The code name does not exist or a error is in the code")
                quit()
        elif method == "eval":
            try:
                eval(customcode[code_name])
            except:
                colors.Red("The code name does not exist or a error is in the code")
                quit()
        else:
            colors.Red("The methods is inccoret. They are exec or eval")
            quit()

class bar():
    class custombar():
        class fonction():

            def repeat(self, char, repeat):
                repeated_string = char * repeat
                splitd_strng = repeated_string.split()
                separator = '-'
                result = separator.join(splitd_strng)
                return result

            def getsrange(self):
                global customdic
                return customdic["range"]

            def rerange(self):
                global customdic
                return customdic["range"] - customdic["actual_range"]

            def codeer(self, codename, code):
                global customdic
                customdic[codename] = code

            def getrange(self):
                global customdic
                return customdic["actual_range"]

            def acrange(self):
                global customdic
                customdic["actual_range"] = bar.custombar.fonction.getrange(
                    0) + 1
                return customdic["actual_range"]

            def evrun(self, function_name):
                global customdic
                code_to_lauch = customdic[function_name]
                eval(code_to_lauch)

            def run(self, function_name):
                global customdic
                code_to_lauch = customdic[function_name]
                exec(code_to_lauch)

            def prepare(self, desc, range):
                global customdic
                customdic["desc"] = desc
                customdic["range"] = range

        def getcode(self, url):
            import requests
            global gcode
            global gurl
            gurl = url
            code = requests.get(url)
            gcode = code.text

    def rename(self, desc):
        global bardesc
        global bactive
        if bactive:
            bardesc = desc
        else:
            pass

    def start(self, desc, range):
        global lprint
        global bardesc
        global barrange
        global srange
        global nrange
        global bspace
        global bactive
        lprint = 1
        bactive = True
        bspace = range
        srange = range
        barrange = "#"
        bardesc = desc

    def repeat(self, char, repeat):
        repeated_string = char * repeat
        splitd_strng = repeated_string.split()
        separator = '-'
        result = separator.join(splitd_strng)
        return result

    def next(self):
        global bactive
        if bactive:
            import sys
            global bspace
            global srange
            global nrange
            global svrange
            bspace = bspace - 1
            nrange = nrange + 1
            barrange = bar.repeat("", "#", svrange + 1) + \
                bar.repeat("", "-", bspace)
            svrange = svrange + 1
            global lprint
            if lprint == 1:
                import sys
                sys.stdout.write('\x1b[1A')
                sys.stdout.write('\x1b[2K')
            else:
                pass
            colors.Purple(bardesc + " : " + barrange + "| " +
                          str(int(nrange)) + "/" + str(int(srange)))
        else:
            quit(" You don't have definie the progress bar please add code.bar.start(desc,progress_bar_range)")
            import time
            time.sleep(1)

    def finish(self):
        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        global bactive
        if bactive:
            global bardesc
            global barrange
            global srange
            global nrange

            bardesc = "Computing"
            barrange = ""
            srange = 0
            nrange = 0
        else:
            pass


class utils():

    def sleep(self, timer):
        import time
        time.sleep(timer)

    def print(self, text):
        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        print(text)


class ai():
    class setting():
        def optimise(self, consolek=False):
            global op
            global lprint
            if lprint == 1:
                lprint = 2
            else:
                pass
            op = consolek
            if consolek:
                colors.Green("[AI Setting] The otimiser is activite")
            else:
                colors.Green("[AI  Optimiser] desactivted")

        def bypass(self, yes_no, maxrecursion=0):
            global bypass
            global lprint
            if lprint == 1:
                lprint = 2
            else:
                pass
            mxr = maxrecursion
            if yes_no:
                bypass = True
                colors.Red(
                    "[AI Setting] The max recursion changing can create bug of lag please don't put a very big number")
                colors.Red(
                    "[AI Setting] max recursion set to " + str(int(mxr)))
                import sys
                sys.setrecursionlimit(mxr)
            else:
                bypass = False

        def log(self, console=False):
            global cs
            global op
            global bypass
            import sys
            global lprint
            if lprint == 1:
                lprint = 2
            else:
                pass
            sys.setrecursionlimit(1000)
            bypass = False
            op = False
            cs = console
            if console:
                colors.Cyan("[AI Setting] Log in console activated")
            elif not console:
                colors.Cyan("[AI Setting] Log deactivated")
            else:
                quit(
                    "[AI Setting] Please write True or False in the definite code ex ai = code.ai(True) pr ai = code.ai(Flase)")

    def prepare(self):
        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        colors.Green("[AI Prepare] Setting up AI")
        open("result.py", "w").write("")
        colors.Green("[AI service worker] Result.py cleared")

    def info(self):

        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        colors.Green(
            "[AI Information] The Ai is robot that generate random number and see the number of try that take to generate a choosed")

    def end(self, tr):

        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        colors.LightPurple("[AI service worker] Caculating the result")
        import result
        import importlib
        from time import sleep
        open("result.py", "a").write(
            "def ready():\n  import code\n  color = code.color()\n  final = d1")
        from tqdm import tqdm
        st = tr - 1
        sd = tr

        for i in tqdm(range(0, st), desc=" [AI Service Worker] Running AI"):
            sleep(0.01)
            open("result.py", "a").write(" + d" + str(int(tr)))
            tr = tr - 1
        open("result.py", "a").write("\n  end = final / " + str(
            int(sd)) + "\n  color.LightPurple('[AI service worker] avertage of try : ' + str(float(end)))")

        importlib.reload(result)
        if cs:
            colors.LightPurple("[AI service worker] Lauching the code")
            result.ready()
        else:
            result.ready()

        if cs:
            colors.LightPurple("[AI service worker] Program finish")
        else:
            pass

    def computer(self, found, tr, min, max):

        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        i = 1
        f = 1
        import random
        from time import sleep
        import time
        time.sleep(1)
        if cs:
            colors.Yellow("[AI service Worker] Thread " +
                          str(int(tr)) + " is started")
        else:
            pass
        while i == 1:
            number = random.randint(min, max)
            number1 = random.randint(min, max)
            number2 = random.randint(min, max)
            number3 = random.randint(min, max)
            number4 = random.randint(min, max)
            number5 = random.randint(min, max)
            number6 = random.randint(min, max)
            number7 = random.randint(min, max)
            number8 = random.randint(min, max)
            number9 = random.randint(min, max)
            number10 = random.randint(min, max)
            if op:
                pass
            else:
                sleep(
                    0.001)

            if number == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number1 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number2 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number3 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number4 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number5 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number6 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number7 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number8 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            elif number9 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break

            elif number10 == found:
                i = 2
                mf = "d" + str(int(tr)) + " = " + str(int(f))
                open("result.py", "a").write(mf + "\n")
                break
            else:
                f = f + 15
        if cs:
            colors.Yellow("[AI Service Worker] Thread " +
                          str(int(tr)) + " have finish")
        else:
            pass

    def start(self, found, min, max, rtime=2):

        global lprint
        if lprint == 1:
            lprint = 2
        else:
            pass
        if rtime < 1001:
            pass
        else:
            if bypass == True:
                pass
            else:
                import time
                time.sleep(0.1)
                quit(
                    " RecursionError: maximum recursion depth exceeded\n Please take a value smaller than 1001\n Or you can add ai.bypass(maxrecursion) for bypass this error")
        import time
        time.sleep(0.1)
        import threading
        from tqdm import tqdm
        s = 0
        colors.Cyan("[AI Service Worker] Lauching AI")
        if cs:
            for i in range(rtime):
                if op:
                    pass
                else:
                    time.sleep(1)
                s = s + 1
                if op:
                    x = threading.Thread(ai.computer(self, found, s, min, max))
                    x.start()
                else:
                    ai.computer(self, found, s, min, max)

            time.sleep(1)
            colors.Green("[AI Service Worker] AI Have finish")
        else:
            for i in tqdm(range(0, rtime), desc=" [AI Service Worker] Running AI"):
                time.sleep(0.001)
                s = s + 1
                x = threading.Thread(ai.computer(self, found, s, min, max))
                x.start()
            time.sleep(1)
            if lprint == 1:
                lprint = 2
            else:
                pass
            colors.Green("[AI Service Worker] AI Have finish")

        ai.end(self, s)


class colors():
    def Red(text): print("\033[91m {}\033[00m".format(text))

    def Green(text): print("\033[92m {}\033[00m".format(text))

    def Yellow(text): print("\033[93m {}\033[00m".format(text))

    def LightPurple(text): print("\033[94m {}\033[00m".format(text))

    def Purple(text): print("\033[95m {}\033[00m".format(text))

    def Cyan(text): print("\033[96m {}\033[00m".format(text))

    def LightGray(text): print("\033[97m {}\033[00m".format(text))

    def Black(text): print("\033[98m {}\033[00m".format(text))


class color():
    def Red(self, text): print("\033[91m {}\033[00m".format(text))

    def Green(self, text): print("\033[92m {}\033[00m".format(text))

    def Yellow(self, text): print("\033[93m {}\033[00m".format(text))

    def LightPurple(self, text): print("\033[94m {}\033[00m".format(text))

    def Purple(self, text): print("\033[95m {}\033[00m".format(text))

    def Cyan(self, text): print("\033[96m {}\033[00m".format(text))

    def LightGray(self, text): print("\033[97m {}\033[00m".format(text))

    def Black(self, text): print("\033[98m {}\033[00m".format(text))
