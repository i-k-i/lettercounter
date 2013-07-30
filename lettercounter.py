import sys
import locale
import wx

tmp =''
litdict={}
enc = locale.getpreferredencoding()

def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open',wildcard=wildcard,  style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog. Destroy()
    return path
inpfile=get_path('*')
sfile=open(inpfile)

for i in sfile.read().decode(enc):
   if i not in ('"',"'",','): # usindg in csv
       litdict.setdefault(i,0)
       litdict[i] += 1
sfile.close()

outfile = open(inpfile+'.csv', 'w')
for i in sorted(litdict.items()):
    outfile.write('{0},{1}\r\n'.format(i[0].encode(enc), i[1]))
outfile.close()
