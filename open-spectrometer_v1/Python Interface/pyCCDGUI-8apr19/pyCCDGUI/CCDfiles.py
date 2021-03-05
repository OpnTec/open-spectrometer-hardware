# Copyright (c) 2019 Esben Rossel
 # All rights reserved.
 #
 # Author: Esben Rossel <esbenrossel@gmail.com>
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions
 # are met:
 # 1. Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
 # 2. Redistributions in binary form must reproduce the above copyright
 #    notice, this list of conditions and the following disclaimer in the
 #    documentation and/or other materials provided with the distribution.
 #
 # THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 # IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 # ARE DISCLAIMED.  IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
 # FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 # DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 # OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 # HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 # LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 # OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 # SUCH DAMAGE.


#python imports
import numpy as np
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import csv

#application imports
import config
import CCDpanelsetup

def openfile(self, CCDplot):
    filename = filedialog.askopenfilename(defaultextension=".dat", title="Open file", parent=self)
    line_count = 0
    try:
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=' ')

            for row in readCSV:
                if (line_count == 3):
                    config.SHsent = int(row[1])
                    config.ICGsent = int(row[6])
                if (line_count > 3):
                    config.rxData16[line_count-4] = int(row[1])
                line_count += 1
        CCDpanelsetup.buildpanel.updateplot(self, CCDplot)

        
    except IOError:
        messagebox.showerror("By the great otter!","There's a problem opening the file.")


def savefile(self):
    filename = filedialog.asksaveasfilename(defaultextension=".dat", title="Save file as", parent=self)
    try: 
        with open(filename, mode='w') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=' ')
            writeCSV.writerow(["#Data","from","the","TCD1304","linear","CCD"])
            writeCSV.writerow(["#column","1","=","pixelnumber",",","column","2","=","pixelvalue"])
            writeCSV.writerow(["#Pixel","1-32","and","3679-3694","and","are","dummy","pixels"])
            writeCSV.writerow(["#SH-period:",str(config.SHsent),"","","","ICG-period:",str(config.ICGsent),"","","","Integration","time:",str(config.SHsent/2),"µs"])
            for i in range (3694):
                writeCSV.writerow([str(i+1),str(config.rxData16[i])])


    except IOError:
        messagebox.showerror("By the great otter!","There's a problem saving the file.")
