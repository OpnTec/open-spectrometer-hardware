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

import tkinter as tk

      
def helpme(helpfor):
    top = tk.Toplevel()
    top.title("Help")
    scrolling = tk.Scrollbar(top)
    scrolling.pack(side=tk.RIGHT, fill=tk.Y)
    helptext = tk.Text(top, height=20, width=80, wrap=tk.WORD)
    helptext.pack(side=tk.LEFT, fill=tk.Y)
    scrolling.config(command=helptext.yview)
    helptext.config(yscrollcommand=scrolling.set)

    helptext.tag_configure('it', font=('Arial', 10, 'italic'))
    helptext.tag_configure('h1', font=('Verdana', 16, 'bold'))
    helptext.tag_configure('h2', font=('Verdana', 12, 'bold'))
    helptext.tag_configure('h3', font=('Verdana', 10, 'bold'))

    if (helpfor == 0): #do you need help with the device?
        helptext.insert(tk.END, " Communication device\n", 'h1')
        helptext.insert(tk.END, "\nThe communication device is the identifier for the USB->serial connection. The label under the entrybox states if the given device is accessible or not. Beware that the label only updates during startup and editing of the entry. If the nucleo is attached after starting the application, the label may or may not be correct.\n")
        helptext.insert(tk.END, "\nIf a valid device is not selected, an error message will appear, when pressing Collect. \n")
        helptext.insert(tk.END, "\n Linux \n", "h2")
        helptext.insert(tk.END, "\nOn Linux the STM32 Nucleo board attaches as a tty-device. The default on Debian-based systems is: \n")
        helptext.insert(tk.END, "\n  /dev/ttyACM0 \n")
        helptext.insert(tk.END, "\nIf the nucleo does not attach as the default device, check the output of dmesg or the contents of /dev/\n")
        helptext.insert(tk.END, "\nYou may find that the device exists, but you still get an error message when pressing collect. This is likely a permission-problem. It can be solved by adding your user to the dialout group. Type:\n")
        helptext.insert(tk.END, "\n  sudo adduser esben dialout \n")
        helptext.insert(tk.END, "\n macOS  \n", "h2")
        helptext.insert(tk.END, "\nOn macOS the STM32 Nucleo board attaches itself as a device called:\n")
        helptext.insert(tk.END, "\n  /dev/cu.usbmodemXYZ \n")
        helptext.insert(tk.END, "\nCheck the contents of /dev/ to find out what to replace XYZ with. In case this directory is hidden from view in Finder, you will need to open a terminal and type:\n")
        helptext.insert(tk.END, "\n  ls /dev/ \n")
        helptext.insert(tk.END, "\n Windows\n", "h2")
        helptext.insert(tk.END, "\nWindows uses an entirely different subsystem for serial communication than *NIX-systems. The STM32 Nucleo is attached as a COM-port (if the STM32 Virtual COM port driver is installed). Try with \n")
        helptext.insert(tk.END, "\n  COMn \n")
        helptext.insert(tk.END, "\nWhere n is an integer, eg. COM6\n")
        helptext.insert(tk.END, "\n \n")
        helptext.insert(tk.END, "\n \n")

    elif (helpfor == 1): #do you need help with the SH and ICG pulses?
        helptext.insert(tk.END, " Driving pulses\n", 'h1')
        helptext.insert(tk.END, "\nThe TCD1304 requires 3 driving pulses:   \n")
        helptext.insert(tk.END, "\n  - MCLK (master clock)")
        helptext.insert(tk.END, "\n  - SH (shift gate)")
        helptext.insert(tk.END, "\n  - ICG (integration clear gate)\n")
        helptext.insert(tk.END, "\nThe following is for STM32F40x firmwares. If you use the STM32F103 make sure to also read the final paragraph.\n")
        helptext.insert(tk.END, "\n MCLK - The master clock\n", "h2")
        helptext.insert(tk.END, "\nThe MCLK (sometimes called fM or φM) is the CCD's clock speed. It defines the time-base which the TCD1304 operates in, and for the unmodified CCD driver firmware MCLK has the value:\n")
        helptext.tag_add("fm",  "13.28", "13.29", "13.34","13.35")
        helptext.tag_config("fm" , offset=-4)
        helptext.insert(tk.END, "\n  MCLK = 2,0 MHz \n")
        helptext.insert(tk.END, "\nThe value of MCLK is used to derive the integration time from the SH-pulse\n")

        helptext.insert(tk.END, "\n SH - The shift gate\n", "h2") 
        helptext.insert(tk.END, "\nThe SH-pulse defines the integration time, tint, which for the TCD1304 cannot be shorter than 10 µs. The user controls the SH-period, which together with MCLK, determines the frequency of the SH-pulse: \n") 
        helptext.tag_add("tint2",  "21.44", "21.47")
        helptext.tag_config("tint2" , offset=-4)
        helptext.insert(tk.END, "\n  SH-frequency = MCLK / SH-period \n") 
        helptext.insert(tk.END, "\n  tint = 1 / SH-frequency = SH-period / MCLK \n") 
        helptext.tag_add("tint1",  "25.3", "25.6")
        helptext.tag_config("tint1" , offset=-4)
        helptext.insert(tk.END, "\nBecause the CCD has a minimum integration time of 10 µs, the SH-period cannot be smaller than: \n") 
        helptext.insert(tk.END, "\n  SH-period = tint · MCLK \n")
        helptext.tag_add("tint3",  "29.15", "29.18")
        helptext.tag_config("tint3" , offset=-4)
        helptext.insert(tk.END, "            = 10 µs · 2,0 MHz = 20 \n") 
        helptext.insert(tk.END, "\nBecause the timer controlling the SH-pulse is 32-bit, the largest value for the SH-period is  \n")  
        helptext.insert(tk.END, "\n  2³² - 1 = 4294967295 \n")  
        helptext.insert(tk.END, "\nCorresponding to a max. integration time of:   \n")  
        helptext.insert(tk.END, "\n  tint = (2³² - 1) / 2,0 MHz = 35 min \n")
        helptext.tag_add("tint4",  "38.3", "38.6")
        helptext.tag_config("tint4" , offset=-4)
        helptext.insert(tk.END, "\n  Example: \n", "h3") 
        helptext.insert(tk.END, "\nSay one whishes to make a collection with an integration time, tint, of 15 ms, what should the SH-period then be?\n")
        helptext.tag_add("tint5",  "42.64", "42.67")
        helptext.tag_config("tint5" , offset=-4)
        helptext.insert(tk.END, "\nThe integration time and the MCLK gives the SH-period as:\n") 
        helptext.insert(tk.END, "\n  SH-period = tint · MCLK \n") 
        helptext.insert(tk.END, "            = 15 ms · 2,0 MHz = 0,015 s · 2000000 Hz = 30000 \n")
        helptext.tag_add("tint5",  "46.15", "46.18")
        helptext.tag_config("tint5" , offset=-4)
        helptext.insert(tk.END, "\n ICG - The integration clear gate  \n", "h2")   
        helptext.insert(tk.END, "\nThe ICG-pulse defines the moment when the pixels are dumped to the output-pin of the CCD. The ICG-pulse must coincide with an SH-pulse, so the following relation must be obeyed:  \n")   
        helptext.insert(tk.END, "\n  ICG-period = n · SH-period \n")   
        helptext.insert(tk.END, "\nwhere n is an integer. When n equals 1, the CCD is said to operate in normal mode. When n is larger than 1, the CCD runs in electronic shutter mode.\n")
        helptext.insert(tk.END, "\nBecause it takes 4 MCLK cycles for the TCD1304 to output 1 pixel, and the chip has 3694 pixels the minimum value for the ICG-period becomes:  \n")     
        helptext.insert(tk.END, "\n   4 · 3694 = 14776\n")
        helptext.insert(tk.END, "\nThis in turn defines the read-out time for the CCD, and is of course dependent on MCLK:   \n")   
        helptext.insert(tk.END, "\n   tread = 14776 / MCLK = 14776 / 2,0 MHz = 7,4 ms\n")  
        helptext.tag_add("tread",  "63.4", "63.8")
        helptext.tag_config("tread" , offset=-4) 
        helptext.insert(tk.END, "\nIn the unmodified CCD driver firmware, the user LED blinks with half the frequency of the ICG-pulse.\n")
        helptext.insert(tk.END, "\n STM32F103-specifics\n", "h2") 
        helptext.insert(tk.END, "\nThe firmware for the STM32F103 differs from the STM32F40x firmwares in that:\n") 
        helptext.insert(tk.END, "\n MCLK = 800 kHz\n")
        helptext.insert(tk.END, "\nand since the chip only has 16-bit timers, the maximum allowed values for the SH- and ICG-period is:\n")
        helptext.insert(tk.END, "\n 2¹⁶ - 1 = 65535\n")
        helptext.insert(tk.END, "\nmeaning that the longest integration time is:\n")
        helptext.insert(tk.END, "\n tint = 65535 / 800 kHz = 82 ms\n")
        helptext.insert(tk.END, "\nThe minimum ICG-period is unaffected by MCLK and remains 14776, however the minimum SH-period becomes:\n")
        helptext.insert(tk.END, "\n SH-period = 10 µs · 800 kHz = 8")






    elif (helpfor == 2): #do you need help with averaging 
        helptext.insert(tk.END, "Averaging\n", 'h1')
        helptext.insert(tk.END, "\nS/N may be increased by collecting n identical recordings and averaging them to cancel out noise. In theory the signal should improve with √n.\n")
        helptext.insert(tk.END, "\nHowever CCD's are subject to readout noise, so it may be preferable to collect a single recording with longer integration time.\n")
        helptext.insert(tk.END, "\nThe CCD driver firmware features on-board averaging of 2-15 identical recordings without the penalty of having to perform n transmissions.\n")
        helptext.insert(tk.END, "\nStoring the individual recordings is not instantaneous, and using the average-feature requires a slight overhead in the ICG-period compared to the readout time.\n")
        helptext.insert(tk.END, "\nSTM32F40x\n", 'h2')
        helptext.insert(tk.END, "\nTo ensure that the MCU has time to store the individual integrations, the following condition should be met:\n")
        helptext.insert(tk.END, "\n    ICG-period = n·SH-period ≥ 30 000\n")
        helptext.insert(tk.END, "\nfor a CCD running with an MCLK of 2.0 MHz.\n")
        helptext.insert(tk.END, "\nSTM32F103\n", 'h2')
        helptext.insert(tk.END, "\nTo ensure that the MCU has time to store the individual integrations, the following condition should be met:\n")
        helptext.insert(tk.END, "\n    ICG-period = n·SH-period ≥ 32 000\n")
        helptext.insert(tk.END, "\nfor a CCD running with an MCLK of 800 kHz.")

    elif (helpfor == 3): #do you need help for inverting data
        helptext.insert(tk.END, "Options\n", 'h1')
        helptext.insert(tk.END, "\nPlot raw data\n", 'h2')
        helptext.insert(tk.END, "\nThe potential of a pixel is inversely related to the light intensity on the CCD, so the collected data should be inverted:\n")
        helptext.insert(tk.END, "\n    Ipixel = ADCmax - ADCpixel = 4095 - ADCpixel    (1)\n")
        helptext.tag_add("ipixel",  "7.5", "7.10", "7.16", "7.19", "7.25", "7.30", "7.43", "7.48")
        helptext.tag_config("ipixel" , offset=-4)
        helptext.insert(tk.END, "\nTaking the CCD's dark-current into account, it becomes:\n")
        helptext.insert(tk.END, "\n    Ipixel = ADCdark - ADCpixel                     (2)\n")
        helptext.tag_add("idark",  "11.5", "11.10", "11.16", "11.20", "11.26", "11.31")
        helptext.tag_config("idark" , offset=-4)
        helptext.insert(tk.END, "\nThe ADC-count for the dark-current is given by the ADC-count for the CCD's dummy-pixels.\n")
        helptext.insert(tk.END, "\nBy default, the application plots Ipixel as calculated in equation 2.\n")
        helptext.tag_add("iplot",  "15.35", "15.40")
        helptext.tag_config("iplot" , offset=-4)
        helptext.insert(tk.END, "\nChecking the 'Plot raw data' checkbox, the application plots ADCpixel directly.\n")
        helptext.tag_add("iplotu",  "17.64", "17.69")
        helptext.tag_config("iplotu" , offset=-4)
        helptext.insert(tk.END, "\nNotice that it's the raw data that is saved, and that it's up to the user to perform the operations above when using a different application.\n")

    #elif (helpfor == 4): #what is save and opened
        helptext.insert(tk.END, "\nBalanced output\n", 'h2')
        helptext.insert(tk.END, "\nOdd and even pixels on the TCD1304 are sent to different output shift registers in the CCD. Because of this, CCD-output may look noisier than it actually is.\n")
        helptext.insert(tk.END, "\nWith the 'Balanced output' box checked, the application estimates the register imbalance (RI) and compensates for the difference when plotting the data.\n")
        helptext.insert(tk.END, "\nThe register imbalance is calculated as the average of the differences between the output from the odd and even of the first 32 dummypixels.\n")
        helptext.insert(tk.END, "\nRI = (Σ[even] - Σ[odd])/16\n")
        helptext.insert(tk.END, "\nNotice that it's the raw data that is saved, and that it's up to the user to perform the operations above when using a different application.\n")


    elif (helpfor == 5): #what is save and opened
        helptext.insert(tk.END, "Saving files\n", 'h2')
        helptext.insert(tk.END, "When saving, the raw data from the CCD is written to a file with the following gnuplot-compatible format: The lines 1-3 contain general information. Line 4 contains the CCD's settings. Lines 5-3698 contain the raw data from the CCD, as shown here:\n")
        helptext.insert(tk.END, "\n#Data from the TCD1304 linear CCD\n")
        helptext.insert(tk.END, "#column 1 = pixelnumber,  column 2 = pixelvalue\n")
        helptext.insert(tk.END, "#Pixel 1-32 and 3679-3694 and are dummy pixels\n")
        helptext.insert(tk.END, "#SH-period: 40   ICG-period: 20000   Integration time: 20 us\n")
        helptext.insert(tk.END, "1 3936\n")
        helptext.insert(tk.END, "2 3934\n")
        helptext.insert(tk.END, ".. ..\n")
        helptext.insert(tk.END, ".. ..\n")
        helptext.insert(tk.END, "3694 3934\n")
        helptext.insert(tk.END, "\nNotice that it's the raw data that's saved. The raw data is not plottet by default. Instead the plotted intensities are calculated like this:\n")
        helptext.insert(tk.END,  "\n    Ipixel = ADCdark - ADCpixel\n")
        helptext.tag_add("isave",  "16.5", "16.10", "16.16", "16.20", "16.26", "16.31")
        helptext.tag_config("isave" , offset=-4)
        helptext.insert(tk.END, "\nThe ADC-count for the dark-current is given by the ADC-count for the CCD's dummy-pixels.\n")
        helptext.insert(tk.END, "\nOpening files\n", 'h2')
        helptext.insert(tk.END, "The application expects a data-format identical to the one outlined in the 'Saving files' section.\n")
        helptext.insert(tk.END, "\nThe command-line interface writes CCD-data to file in the same format, so the application can be used to open data collected with the CLI.\n")

    elif (helpfor == 6):
        helptext.insert(tk.END, "Capture mode\n", 'h1')
        helptext.insert(tk.END, "\nSingle\n", 'h2')
        helptext.insert(tk.END, "\nExactly what it says. The MCU returns one dataset. If averaging is enabled it will collect and average n times before returning the dataset.\n")
        helptext.insert(tk.END, "\nContinuous\n", 'h2')
        helptext.insert(tk.END, "\nAlmost exactly what it says. The MCU reads the CCD and returns datasets with a framerate determined by the ICG-period and the averaging setting. \n \nIt's not possible to change settings on the fly.\n")
        helptext.insert(tk.END, "\nImportant\n", 'h2')
        helptext.insert(tk.END, "\nNotice that the MCU can read the CCD much faster than it can transmit a dataset. To avoid overwriting data before transmission is complete and/or crashing consider the following:\n")
        helptext.insert(tk.END, "\nUART\n", 'h3')
        helptext.insert(tk.END, "If you're running the TCD1304 of off an STM32 Nucleo F401 the communication protocol is UART, which is slow. Transmission takes at least 641 ms, so the ICG-period should be at least:\n")
        helptext.insert(tk.END, "\nICG-period > 641 ms · 2.0 MHz = 1.282 · 10⁶\n")
        helptext.insert(tk.END, "\nUSB\n", 'h3')
        helptext.insert(tk.END, "If you're running the TCD1304 of off an STM32F103 or STM32F405, the communication protocol is full-speed USB. While FS-USB potentially runs at 12 Mbps, don't expect an actual speed this high.\n")
        helptext.insert(tk.END, "\nSTM32F103\n", 'h3')
        helptext.insert(tk.END, "I've been able to run the STM32F103 in continuous mode with an ICG-period as low as 44 000 with averaging set to 2, but not faster than that.\n")

        helptext.insert(tk.END, "\nThis corresponds to a max fps of: \n")
        helptext.insert(tk.END, "\nfps = 800 kHz / (2 · 42 000) = 9.5 Hz\n")
        helptext.insert(tk.END, "\nObserve that averaging is not instantaneous, and requires its own overhead with regards to the ICG-period, so keep the ICG-period ≥ 32 000.\n")
        helptext.insert(tk.END, "\nSTM32F405\n", 'h3')

    elif (helpfor == 10): #about
        helptext.insert(tk.END, "About\n", 'h1')
        helptext.insert(tk.END, "\nCopyright (c) 2019 Esben Rossel")
        helptext.insert(tk.END, "\nAll rights reserved.\n")
        helptext.insert(tk.END, "\nAuthor: Esben Rossel <esbenrossel@gmail.com>\n")
        helptext.insert(tk.END, "\nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:\n")
        helptext.insert(tk.END, "\n1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.")
        helptext.insert(tk.END, "\n2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\n")
        helptext.insert(tk.END, "\nTHIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n")

    helptext.config(state=tk.DISABLED)
