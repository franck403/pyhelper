#class bar():
 #   def rename(self, desc):
  #      global bardesc
   #     global bactive
    #    if bactive:
     #       bardesc = desc
      #  else:
       #     pass

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

#    def repeat(self, char, repeat):
 #       repeated_string = char * repeat
  #      splitd_strng = repeated_string.split()
   #     separator = '-'
    #    result = separator.join(splitd_strng)
     #   return result

#    def next(self):
 #       global bactive
  ##      if bactive:
    #        import sys
     #       global bspace
      #      global srange
       #     global nrange
        #    global svrange
         #   bspace = bspace - 1
          #  nrange = nrange + 1
           # barrange = bar.repeat("", "#", svrange + 1) + bar.repeat("", "-", bspace)
#            svrange = svrange + 1
 #           global lprint
  #          if lprint == 1:
   #             import sys
    #            sys.stdout.write('\x1b[1A')
     #           sys.stdout.write('\x1b[2K')
      #      else:
       #         pass
        #    colors.Purple(bardesc + " : " + barrange + "| " + str(int(nrange)) + "/" + str(int(srange)))
#        else:
 #           quit(" You don't have definie the progress bar please add code.bar.start(desc,progress_bar_range)")
  #          import time
   #         time.sleep(1)

#    def finish(self):
 #       global lprint
  #      if lprint == 1:
   #         lprint = 2
       # else:
       #     pass
      #  global bactive
     #   if bactive:
    #        global bardesc
   #         global barrange
  #          global srange
 #           global nrange

         #   bardesc = "Computing"
        #    barrange = ""
       #     srange = 0
      #      nrange = 0
     #   else:
    #        pass
