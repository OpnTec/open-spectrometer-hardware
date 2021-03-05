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
import tkinter as tk
from tkinter import ttk
import numpy as np
import serial

#application imports
import config
from CCDhelp import *
import CCDserial
import CCDfiles

class buildpanel(tk.Frame):
  def __init__(self, master, CCDplot, SerQueue):
    #geometry-rows for packing the grid
    device_row = 10
    shicg_row = 20
    continuous_row = 30
    avg_row = 40
    collect_row = 50
    plotmode_row = 60
    save_row = 70
    update_row = 80
    progress_var = tk.IntVar()
    
    tk.Frame.__init__(self, master=None)


    #Create all widgets and space between them
    self.devicefields(device_row)
    #insert vertical space
    self.grid_rowconfigure(device_row+3, minsize=30)
    self.CCDparamfields(shicg_row)
    #insert vertical space
    self.grid_rowconfigure(shicg_row+4, minsize=30) 
    self.collectmodefields(continuous_row)
    self.avgfields(avg_row)
	#insert vertical space
    self.grid_rowconfigure(avg_row+2, minsize=30)
    self.collectfields(collect_row, SerQueue, progress_var)
    #vertical space
    self.grid_rowconfigure(collect_row+2, minsize=30) 
    self.plotmodefields(plotmode_row, CCDplot)
    self.saveopenfields(save_row, CCDplot)
    self.updateplotfields(update_row, CCDplot)








  def devicefields(self, device_row):
    #device setup - variables, widgets and traces associated with the device entrybox
    #variables
    self.device_address = tk.StringVar()
    self.device_status = tk.StringVar()
    self.device_statuscolor = tk.StringVar()
    #widgets
    self.ldevice = tk.Label(self, text="COM-device:")
    self.ldevice.grid(column=0, row=device_row)
    self.edevice = tk.Entry(self, textvariable=self.device_address, justify='left')
    self.edevice.grid(column=1, row=device_row)   
    self.ldevicestatus = tk.Label(self, textvariable=self.device_status, fg="green")
    #setup trace to check if the device exists
    self.device_address.trace("w", lambda name, index, mode, Device=self.device_address, status=self.device_status, colr=self.ldevicestatus: self.DEVcallback(name, index, mode, Device, status, colr))
    self.device_address.set(config.port)
    self.ldevicestatus.grid(columnspan=2, row=device_row+1)
    #help button    
    self.bhdev = tk.Button(self, text="?", command=lambda helpfor=0: helpme(helpfor))
    self.bhdev.grid(row=device_row, column=3)


	
  def CCDparamfields(self, shicg_row):
    #CCD parameters - variables, widgets and traces associated with setting ICG and SH for the CCD
    self.SHvalue = tk.StringVar()
    self.SHvalue.set("200") 
    self.ICGvalue = tk.StringVar()
    self.ICGvalue.set("100000")
    self.tint = tk.StringVar()
    self.tint.set("Integration time is 0.1 ms")
    self.ICGSHstatus = tk.StringVar()
    self.ICGSHstatus.set("Correct CCD pulse timing.")
    self.ICGSHstatuscolor = tk.StringVar()
    #pulse timing tip
    self.ltipSHICG = tk.Label(self, text="ICG = n·SH")
    self.ltipSHICG.grid(columnspan=2, row=shicg_row-1) 
	#setup SH-entry
    self.lSH = tk.Label(self, text="SH-period:")
    self.lSH.grid(column=0, row=shicg_row)
    self.eSH = tk.Entry(self, textvariable=self.SHvalue, justify='right')
    self.eSH.grid(column=1, row=shicg_row)
    #setup ICG-entry
    self.lICG = tk.Label(self, text="ICG-period:")
    self.lICG.grid(column=0, row=shicg_row+1)
    self.eICG = tk.Entry(self, textvariable=self.ICGvalue, justify='right')
    self.eICG.grid(column=1, row=shicg_row+1)
    #setup ICGSH-status label
    self.lICGSH = tk.Label(self, textvariable=self.ICGSHstatus, fg="green")
    self.lICGSH.grid(columnspan=2, row=shicg_row+2)
    #integration time label
    self.ltint = tk.Label(self, textvariable=self.tint)
    self.ltint.grid(columnspan=2, row=shicg_row+3)
	#help button
    self.bhtiming = tk.Button(self, text="?", command=lambda helpfor=1: helpme(helpfor))
    self.bhtiming.grid(row=shicg_row, rowspan=2, column=3)
    #setup traces to update tx-data
    self.SHvalue.trace("w", lambda name, index, mode, status=self.ICGSHstatus, tint=self.tint, colr=self.lICGSH, SH=self.SHvalue, ICG=self.ICGvalue: self.ICGSHcallback(name, index, mode, status, tint, colr, SH, ICG))
    self.ICGvalue.trace("w", lambda name, index, mode, status=self.ICGSHstatus, tint=self.tint, colr=self.lICGSH, SH=self.SHvalue, ICG=self.ICGvalue: self.ICGSHcallback(name, index, mode, status, tint, colr, SH, ICG))


  def collectmodefields(self, continuous_row):
    #setup continuous vs one-shot
    self.collectmode_frame = tk.Frame(self)
    self.collectmode_frame.grid(row=continuous_row, columnspan=2)  
    self.CONTvar = tk.IntVar()
    self.rcontinuous = tk.Radiobutton(self.collectmode_frame, text="Continuous", variable=self.CONTvar, value=1, command=lambda CONTvar=self.CONTvar: self.modeset(CONTvar))
    self.rcontinuous.grid(row=0, column=2, sticky="W")
    self.roneshot = tk.Radiobutton(self.collectmode_frame, text="Single", variable=self.CONTvar, value=0, command=lambda CONTvar=self.CONTvar: self.modeset(CONTvar))
    self.roneshot.grid(row=0, column=1, sticky="W")
	#help button
    self.bhcollectmode = tk.Button(self, text="?", command=lambda helpfor=6: helpme(helpfor))
    self.bhcollectmode.grid(row=continuous_row, column=3)


  def avgfields(self, avg_row):
	#setup AVG entry
    self.lAVG = tk.Label(self, text="Average:")
    self.lAVG.grid(column=0, row=avg_row)
    self.AVGscale = tk.Scale(self, orient='horizontal', from_=1, to=15)
    self.AVGscale.configure(command=self.AVGcallback)
    self.AVGscale.grid(column=1, row=avg_row, sticky="we")
    #help button
    self.bhavg = tk.Button(self, text="?", command=lambda helpfor=2: helpme(helpfor))
    self.bhavg.grid(row=avg_row, column=3)


  def collectfields(self, collect_row, SerQueue, progress_var):
    #setup collect and stop buttons
    self.progress = ttk.Progressbar(self, orient="horizontal",  maximum=10,  mode="determinate",  var=progress_var)
    self.bcollect = tk.Button(self, text="Collect", command=lambda panel=self, SerQueue=SerQueue, progress_var=progress_var: CCDserial.rxtx(panel, SerQueue, progress_var))
    self.bcollect.event_generate('<ButtonPress>', when='tail')
    self.bcollect.grid(row=collect_row, columnspan=3, sticky="EW", padx=5)
    self.bstop = tk.Button(self, text="Stop", state=tk.DISABLED, command=lambda queue=SerQueue: CCDserial.rxtxcancel(queue))
    self.bstop.grid(row=collect_row, column=3)
    self.progress.grid(row=collect_row+1, columnspan=3, sticky="EW", padx=5)

 
  def plotmodefields(self, plotmode_row, CCDplot):
	#setup plot mode checkbuttons
    self.plotmode_frame = tk.Frame(self)
    self.plotmode_frame.grid(row=plotmode_row, columnspan=2)        
    self.balance_var = tk.IntVar()
    self.rawplot_var = tk.IntVar()
    self.cinvert = tk.Checkbutton(self.plotmode_frame, text="Plot raw data", variable=self.rawplot_var, offvalue=1, onvalue=0)#, state=tk.ACTIVE)
    self.cinvert.deselect()
    self.cinvert.grid(row=0, column=1, sticky="W")
    self.cbalance = tk.Checkbutton(self.plotmode_frame, text="Balance output", variable=self.balance_var, offvalue=0, onvalue=1)#, state=tk.ACTIVE)
    self.cbalance.select()
    self.cbalance.grid(row=0, column=2, sticky="W")
    self.grid_rowconfigure(plotmode_row+2, minsize=50)
	#help button
    self.bhinv = tk.Button(self, text="?", command=lambda helpfor=3: helpme(helpfor))
    self.bhinv.grid(row=plotmode_row, column=3)
    #setup traces
    self.rawplot_var.trace("w", lambda name, index, mode, invert=self.rawplot_var, plot=CCDplot: self.RAWcallback(name, index, mode, invert, plot))
    self.balance_var.trace("w", lambda name, index, mode, balance=self.balance_var, plot=CCDplot: self.BALcallback(name, index, mode, balance, plot))


  def saveopenfields(self, save_row, CCDplot):
	#setup save/open buttons
    self.fileframe = tk.Frame(self)
    self.fileframe.grid(row=save_row, columnspan=2)
    self.bopen = tk.Button(self.fileframe, text="Open", width=11, command=lambda self=self, CCDplot=CCDplot: CCDfiles.openfile(self, CCDplot))
    self.bsave = tk.Button(self.fileframe, text="Save", width=11, state=tk.DISABLED,command=lambda self=self: CCDfiles.savefile(self))
    self.bopen.pack(side=tk.LEFT)
    self.bsave.pack(side=tk.LEFT)
	#help button
    self.bhsav = tk.Button(self, text="?", command=lambda helpfor=5: helpme(helpfor))
    self.bhsav.grid(row=save_row, column=3)

  def updateplotfields(self, update_row, CCDplot):
    self.bupdate = tk.Button(self, text="Update plot", command=lambda CCDplot=CCDplot: self.updateplot(CCDplot))
    #setup an event on the invisible update-plot button with a callback this thread can invoke in the mainloop
    self.bupdate.event_generate('<ButtonPress>', when='tail')

    #commented out, it's needed to inject an event into the tk.mainloop for updating the plot from the 'checkfordata' thread
    #self.bupdate.grid(row=update_row, columnspan=3, sticky="EW", padx=5)



  ### Callbacks for traces, buttons, etc ###
  def callback(self):
    self.bopen.config(state=tk.DISABLED)
    return() 


  def ICGSHcallback(self, name, index, mode, status, tint, colr, SH, ICG):
    try:
        config.SHperiod = np.uint32(int(SH.get()))
        config.ICGperiod = np.uint32(int(ICG.get()))
    except:
        print("SH or ICG not an integer")
    self.print_tint = tk.StringVar()

    

    if (config.SHperiod < 1):
      config.SHperiod = 1
    if (config.ICGperiod < 1):
      config.ICGperiod = 1


    if ((config.ICGperiod % config.SHperiod) or (config.SHperiod < 20) or (config.ICGperiod < 14776)):
        status.set("CCD pulse timing violation!")
        colr.configure(fg="red")
        self.print_tint.set("invalid")
    else:
        status.set("Correct CCD pulse timing.")
        colr.configure(fg="green")
        if (config.SHperiod < 20000000):
            self.print_tint.set(str(config.SHperiod/2000) + " ms")
        elif (config.SHperiod <= 1200000000):
            self.print_tint.set(str(config.SHperiod/2000000) + " s")
        elif (config.SHperiod >  1200000000):
            self.print_tint.set(str(round(config.SHperiod/120000000,2)) + " min")


    #tint.set("Integration time is " + + " ms")
    tint.set("Integration time is " + self.print_tint.get())

  def modeset(self, CONTvar):
    config.AVGn[0]=CONTvar.get()


  def AVGcallback(self,AVGscale):
    config.AVGn[1] = np.uint8(self.AVGscale.get())


  def RAWcallback(self, name, index, mode, invert, CCDplot):
    config.datainvert = invert.get()
    if (config.datainvert == 0):
        self.cbalance.config(state=tk.DISABLED)
    else:
        self.cbalance.config(state=tk.NORMAL)
    self.updateplot(CCDplot)

  def BALcallback(self, name, index, mode, balanced, CCDplot):
    config.balanced = balanced.get()
    self.updateplot(CCDplot)

  def DEVcallback(self, name, index, mode, Device, status, colr):
    config.port = Device.get()
    try:
        ser = serial.Serial(config.port, config.baudrate, timeout=1)
        status.set("Device exist")
        ser.close()
        colr.configure(fg="green")
    except serial.SerialException:
        status.set("Device doesn't exist")
        colr.configure(fg="red")

  def updateplot(self, CCDplot):
    #This subtracts the ADC-pixel from ADC-dark
    if (config.datainvert==1): 
        config.pltData16 = (config.rxData16[10]+config.rxData16[11])/2 - config.rxData16
        #This subtracts the average difference between even and odd pixels from the even pixels
        if (config.balanced==1):
            config.offset = (config.pltData16[18]+config.pltData16[20]+config.pltData16[22]+config.pltData16[24]-config.pltData16[19]-config.pltData16[21]-config.pltData16[23]-config.pltData16[24])/4
            for i in range (1847):
                config.pltData16[2*i] = config.pltData16[2*i] - config.offset 
    CCDplot.a.clear()
    #plot intensities
    if (config.datainvert == 1):
        CCDplot.a.plot(config.pltData16)
        CCDplot.a.set_ylabel("Intensity")
        CCDplot.a.axis([0,3694,-10,2250])
    else:
        #plot raw data    
        CCDplot.a.plot(config.rxData16)
        CCDplot.a.set_ylabel("ADCcount")
        CCDplot.a.axis([0,3694,-10,4095])
    CCDplot.a.set_xlabel("Pixelnumber")

    CCDplot.canvas.draw()

