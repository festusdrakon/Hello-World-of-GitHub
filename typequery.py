#playing around with ui elements on a 2.36" display

import appuifw

#display user input right away
wut = appuifw.query(u"insert it here", "query")
appuifw.note(u"you just typed "+ str(wut), "info")