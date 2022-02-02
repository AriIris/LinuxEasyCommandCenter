# Created by Mintmann at the Linux Mint forums
# https://forums.linuxmint.com/
# version 1.0
# 2022-02-02

import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import WORD
from tkinter import messagebox
from subprocess import Popen, PIPE
from datetime import datetime
from subprocess import check_output
import platform
import time
import subprocess
import distutils.spawn
import webbrowser


def center(win):
    """
    centers a tkinter window
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

root = Tk()
root.option_add("*Font", 'Georgia 10')
root.wm_title(" LECC - Linux Easy Command Center ")
root.geometry("800x600")
root.maxsize(800, 600)
root.minsize(800, 600)
center(root)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="lightgray")
s.map("TNotebook.Tab", background=[("selected", "magenta")])

tab_control = ttk.Notebook(root)
# tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='List 1')
# tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='List 2')
tab_control.pack(expand=1, fill='both')
# tab3
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='List 3')
tab_control.pack(expand=1, fill='both')
# tab4
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='List 4')
tab_control.pack(expand=1, fill='both')
# tab5
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Run 1')
tab_control.pack(expand=1, fill='both')
# tab6
tab6 = ttk.Frame(tab_control)
tab_control.add(tab6, text='Run 2')
tab_control.pack(expand=1, fill='both')


# put your password here
mepaswrd = "put your password here"


datenow = datetime.today()
findme = os.environ["HOME"]
findme = findme.replace("home", "")
findme = findme.replace("/", "")
osenvpath = os.environ['PATH']
logpath = '/home/' + findme + '/Desktop/z_'


def urlmint():
        webbrowser.open('https://forums.linuxmint.com/')

def urldistros():
        webbrowser.open('https://distrowatch.com/')

def is_tool(name):
  return distutils.spawn.find_executable(name) is not None

def aboutErr():
    messagebox.showinfo(" Popen error! \n Password might have been incorrect. \n Script will now close. ")

def openNewWindow():
    about = Toplevel(root)
    about.option_add("*Font", 'Georgia 10')
    about.title("LECC - About")
    about.geometry("500x400")
    about.maxsize(500, 400)
    about.minsize(500, 400)

    statusbar2 = Label(about, bg="#A9A9A9", text="About", bd=1, relief=FLAT, anchor=W)
    statusbar2.pack(side=BOTTOM, fill=X)

    var1 = StringVar()
    var1.set("This is my first Python script.")
    label1 = Label(about, textvariable=var1, font=("Georgia", 10))
    label1.place(x=20, y=20)

    var2 = StringVar()
    var2.set("I am new to Python & Linux distros.")
    label2 = Label(about, textvariable=var2, font=("Georgia", 10))
    label2.place(x=20, y=40)

    var3 = StringVar()
    var3.set("Typing Terminal commands became tedious so I made this script.")
    label3 = Label(about, textvariable=var3, font=("Georgia", 10))
    label3.place(x=20, y=60)

    var4 = StringVar()
    var4.set("This script does not make any system changes.")
    label4 = Label(about, textvariable=var4, font=("Georgia", 10))
    label4.place(x=20, y=80)

    var5 = StringVar()
    var5.set("This script puts text files on the desktop for command & manual results.")
    label5 = Label(about, textvariable=var5, font=("Georgia", 10))
    label5.place(x=20, y=100)

    var6 = StringVar()
    var6.set("The output file name starts with a lowercase 'z' to group them together.")
    label6 = Label(about, textvariable=var6, font=("Georgia", 10))
    label6.place(x=20, y=120)

    var7 = StringVar()
    var7.set("  ")
    label7 = Label(about, textvariable=var7, font=("Georgia", 10))
    label7.place(x=20, y=140)

    var8 = StringVar()
    var8.set("Edit this script file and change 'put your password here' to your password.")
    label8 = Label(about, textvariable=var8, font=("Georgia", 10))
    label8.place(x=20, y=160)

    var9 = StringVar()
    var9.set("If anyone wants to add another command just let me know.")
    label9 = Label(about, textvariable=var9, font=("Georgia", 10))
    label9.place(x=20, y=180)

    var10 = StringVar()
    var10.set("  ")
    label10 = Label(about, textvariable=var10, font=("Georgia", 10))
    label10.place(x=20, y=200)

    var11 = StringVar()
    var11.set("Some commands will not work unless they are installed.")
    label11 = Label(about, textvariable=var11, font=("Georgia", 10))
    label11.place(x=20, y=220)

    var12 = StringVar()
    var12.set("Examples; Pip3, Python3, LSscsi, Nvidia, Psensor, Zoom.")
    label12 = Label(about, textvariable=var12, font=("Georgia", 10))
    label12.place(x=20, y=240)


    # menus
    menubar2 = Menu(about, bg="#A9A9A9", relief=FLAT)
    filemenu2 = Menu(menubar2, tearoff='off')

    filemenu2.add_command(label="Close", font=("Georgia", 10), activeforeground="#FF00FF", command=about.destroy)
    menubar2.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu2)

    about.config(menu=menubar2)
    center(about)
    about.mainloop()

def openErrorWindow(msg,prog):
    about = Toplevel(root)
    about.option_add("*Font", 'Georgia 10')
    about.title("Run Error")
    about.geometry("300x100")
    about.maxsize(300, 120)
    about.minsize(300, 120)

    statusbar2 = Label(about, bg="#A9A9A9", text="Notice", bd=1, relief=FLAT, anchor=W)
    statusbar2.pack(side=BOTTOM, fill=X)

    var1 = StringVar()
    var1.set("'" + prog + "' appears to not exist.")
    label1 = Label(about, textvariable=var1, font=("Georgia", 12))
    label1.place(x=20, y=20)

    # menus
    menubar2 = Menu(about, bg="#A9A9A9", relief=FLAT)
    filemenu2 = Menu(menubar2, tearoff='off')

    filemenu2.add_command(label="Close", font=("Georgia", 10), activeforeground="#FF00FF", command=about.destroy)
    menubar2.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu2)

    about.config(menu=menubar2)
    center(about)
    about.mainloop()

def buttonquithandler():
    response = str(messagebox.askquestion("Quit", "Are you sure you want to quit?"))
    if response.lower().startswith("yes"):
        exit()

s = ttk.Style()
s.theme_use('default')
s.configure("TCombobox", fieldbackground="orange", background="#0288d1")

system_info = platform.platform()
statusbar = Label(root, bg="#A9A9A9", text=system_info, bd=1, relief=FLAT, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# inxi
def inxi_changed(event):
    msg=inxiOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

# tab 1 comboboxes
inxiOptions=('b - cpu,speeds,mem,system,machine,cpu,graphics,network,drives,processes',
             'i - Network device info', 'r - Distro repositories', 's - Sensors (temps & fan speeds',
             'tcm - Show CPU process & Show memory used (top 5)', 'w - Weather (local)',
             'A - Show Audio/sound card(s) info & driver(s)', 'B - System battery',
             'C - Show full CPU output, include core speeds & CPU max speed (if available)',
             'D - Shows total disk space & used percentage', 'F - Show Full output for inxi',
             'G - Show graphic card(s) info & driver(s)',
             'I - Show Info: processes, uptime, memory, GiB used, shell, version',
             'M - Show computer information?', 'N - Show network info & driver',
             'S - Show System info: host name, kernel, desktop environment',
             'Fxpmzr - Show system information list')
selected_inxi = tk.StringVar()
inxiOpts=ttk.Combobox(tab1, textvariable=selected_inxi, width=30)    
inxiOpts['values']=inxiOptions
inxiOpts['state']='readonly'
inxiOpts.current(0)
inxiOpts.place(relx=.32, rely=0.158)       
inxiOpts.bind('<<ComboboxSelected>>', inxi_changed)


# df
def df_changed(event):
    msg=dfOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

dfOptions=('a - List pseudo, duplicate, inaccessible', 'l - List local file systems', \
           'm - List mounted file systems', 'h - Disk usage')
selected_df = tk.StringVar()
dfOpts=ttk.Combobox(tab1, textvariable=selected_df, width=30)    
dfOpts['values']=dfOptions
dfOpts['state']='readonly'
dfOpts.current(0)
dfOpts.place(relx=.32, rely=0.329)       
dfOpts.bind('<<ComboboxSelected>>', df_changed)

# dmidecode -t
def dmidecode_changed(event):
    msg=dmidecodeOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

dmidecodestr=('0 - BIOS', '1 - System', '2 - Baseboard', '3 - Chassis', '4 - Processor', '5 - Memory Controller',
              '6 - Memory Module', '7 - Cache', '8 - Port Connector', '9 - System Slots',
              '10 - On-Board Devices', '11 - OEM Strings', '12 - System Config Options',
              '13 - Bios Language', '16 - Physical Memory Array', '17 - Memory Devices', '18 - 32bit Memory Error',
              '19 - Memory Array Mapped', '20 - Memory Devices Mapped', '26 - Voltage Probe', '32 - System Boot',
              '27 - Cooling Device', '28 - Temperature Probes', '29 - Electrical Current Probe',
              '34 - Management Device', '39 - Power Supply', '40 - Additional Info')

dmidecodeOptions= dmidecodestr
selected_dmidecode = tk.StringVar()
dmidecodeOpts=ttk.Combobox(tab1, textvariable=selected_dmidecode, width=30)    
dmidecodeOpts['values']=dmidecodeOptions
dmidecodeOpts['state']='readonly'
dmidecodeOpts.current(0)
dmidecodeOpts.place(relx=.32, rely=0.216)       
dmidecodeOpts.bind('<<ComboboxSelected>>', dmidecode_changed)

# xinput
def xinput_changed(event):
    msg=xinputOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

xinputOptions = ("list - All the input devices",
                 "list --long - Includes detailed info about capabilities of devices")

selected_xinput = tk.StringVar()
xinputOpts=ttk.Combobox(tab1, textvariable=selected_xinput, width=30)    
xinputOpts['values']=xinputOptions
xinputOpts['state']='readonly'
xinputOpts.current(0)
xinputOpts.place(relx=.32, rely=0.274)       
xinputOpts.bind('<<ComboboxSelected>>', xinput_changed)


# lpstat
def lpstat_changed(event):
    msg=lpstatOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

lpstatstr=("d - Current default destination", "e - Available destinations on local network",
           "H - Server host name and port",
           "l - Long listing of printers, classes, jobs", "r - CUPS server status",
           "s - Status summery", "t - All status information: a,c,d,o,p,r,v",
           "u - List current user print jobs", "v - List printers")
lpstatOptions = lpstatstr
selected_lpstat = tk.StringVar()
lpstatOpts=ttk.Combobox(tab1, textvariable=selected_lpstat, width=30)    
lpstatOpts['values']=lpstatOptions
lpstatOpts['state']='readonly'
lpstatOpts.current(0)
lpstatOpts.place(relx=.32, rely=0.619)       
lpstatOpts.bind('<<ComboboxSelected>>', lpstat_changed)


# uname
def uname_changed(event):
    msg=unameOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

unamestr=("a - Print all known information", "i - hardware platform", "m - system architecture",
          "n - network node hostname", "o - operating system", "p - processor type",
          "r - kernel release", "s - kernel name", "v - kernel version")

unameOptions = unamestr
selected_uname = tk.StringVar()
unameOpts=ttk.Combobox(tab1, textvariable=selected_uname, width=30)    
unameOpts['values']=unameOptions
unameOpts['state']='readonly'
unameOpts.current(0)
unameOpts.place(relx=.32, rely=0.386)       
unameOpts.bind('<<ComboboxSelected>>', uname_changed)

# nvidia
def nvidia_changed(event):
    msg=nvidiaOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

nvidiastr=("@ - No switch shows gpu driver info", "L - Shows gpu name")

nvidiaOptions = nvidiastr
selected_nvidia = tk.StringVar()
nvidiaOpts=ttk.Combobox(tab1, textvariable=selected_nvidia, width=30)    
nvidiaOpts['values']=nvidiaOptions
nvidiaOpts['state']='readonly'
nvidiaOpts.current(0)
nvidiaOpts.place(relx=.32, rely=0.099)       
nvidiaOpts.bind('<<ComboboxSelected>>', nvidia_changed)

# hostname
def hostname_changed(event):
    msg=hostnameOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

hostnamestr=("@ - No switch shows the host name", "I - Shows the ip adddress")

hostnameOptions = hostnamestr
selected_hostname = tk.StringVar()
hostnameOpts=ttk.Combobox(tab1, textvariable=selected_hostname, width=30)    
hostnameOpts['values']=hostnameOptions
hostnameOpts['state']='readonly'
hostnameOpts.current(0)
hostnameOpts.place(relx=.32, rely=0.447)       
hostnameOpts.bind('<<ComboboxSelected>>', hostname_changed)


# tab 2 comboboxes
# ifconfig
def ifconfig_changed(event):
    msg=ifconfigOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

ifconfigstr=("a - List all available interfaces", "s - Short list of interfaces")

ifconfigOptions = ifconfigstr
selected_ifconfig = tk.StringVar()
ifconfigOpts=ttk.Combobox(tab2, textvariable=selected_ifconfig, width=30)    
ifconfigOpts['values']=ifconfigOptions
ifconfigOpts['state']='readonly'
ifconfigOpts.current(0)
ifconfigOpts.place(relx=.32, rely=0.271)       
ifconfigOpts.bind('<<ComboboxSelected>>', ifconfig_changed)

# netstat
def netstat_changed(event):
    msg=netstatOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

netstatstr=("i - Show Kernel interface table", "r - Show Kernel routing table", "pnltu - Show active listen ports")

netstatOptions = netstatstr
selected_netstat = tk.StringVar()
netstatOpts=ttk.Combobox(tab2, textvariable=selected_netstat, width=30)    
netstatOpts['values']=netstatOptions
netstatOpts['state']='readonly'
netstatOpts.current(0)
netstatOpts.place(relx=.32, rely=0.329)       
netstatOpts.bind('<<ComboboxSelected>>', netstat_changed)

# ip
def ip_changed(event):
    msg=ipOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

ipstr=("address - Show addresses", "link show - Show network devices",
       "neigh - Shows current neighbor table in kernel",
       "route - Show routing table")
ipOptions = ipstr
selected_ip = tk.StringVar()
ipOpts=ttk.Combobox(tab2, textvariable=selected_ip, width=30)    
ipOpts['values']=ipOptions
ipOpts['state']='readonly'
ipOpts.current(0)
ipOpts.place(relx=.32, rely=0.386)       
ipOpts.bind('<<ComboboxSelected>>', ip_changed)

# ss
def ss_changed(event):
    msg=ssOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

ssstr=("-t -a - List TCP sockets", "-u -a - List all UDP sockets")

ssOptions = ssstr
selected_ss = tk.StringVar()
ssOpts=ttk.Combobox(tab2, textvariable=selected_ss, width=30)    
ssOpts['values']=ssOptions
ssOpts['state']='readonly'
ssOpts.current(0)
ssOpts.place(relx=.32, rely=0.448)       
ssOpts.bind('<<ComboboxSelected>>', ss_changed)

# du
def du_changed(event):
    msg=ssOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

dustr=("ah - Size for directories & files", "sh - Summerize all", "Sh - Size for directories only")

duOptions = dustr
selected_du = tk.StringVar()
duOpts=ttk.Combobox(tab2, textvariable=selected_du, width=30)    
duOpts['values']=duOptions
duOpts['state']='readonly'
duOpts.current(0)
duOpts.place(relx=.32, rely=0.158)       
duOpts.bind('<<ComboboxSelected>>', du_changed)

# sysctl
def sysctl_changed(event):
    msg=sysctlOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

sysctlstr=("abi - parameters", "debug - parameters", "dev - parameters", "fs - parameters",
           "kernel - parameters", "net - parameters", "user - parameters")

sysctlOptions = sysctlstr
selected_sysctl = tk.StringVar()
sysctlOpts=ttk.Combobox(tab3, textvariable=selected_sysctl, width=30)    
sysctlOpts['values']=sysctlOptions
sysctlOpts['state']='readonly'
sysctlOpts.current(0)
sysctlOpts.place(relx=.32, rely=0.850)       
sysctlOpts.bind('<<ComboboxSelected>>', sysctl_changed)

# top
def top_changed(event):
    msg=topOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

topstr=('U - root', 'U - ' + findme, 'U - daemon')

topOptions= topstr
selected_top = tk.StringVar()
topOpts=ttk.Combobox(tab4, textvariable=selected_top, width=30)    
topOpts['values']=topOptions
topOpts['state']='readonly'
topOpts.current(0)
topOpts.place(relx=.32, rely=0.278)       
topOpts.bind('<<ComboboxSelected>>', top_changed)


# locate .conf
def locate_changed(event):
    msg=locateOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

locatestr=('@ - etc', '@ - home', '@ - usr', '@ - var')

locateOptions= locatestr
selected_locate = tk.StringVar()
locateOpts=ttk.Combobox(tab4, textvariable=selected_locate, width=30)    
locateOpts['values']=locateOptions
locateOpts['state']='readonly'
locateOpts.current(0)
locateOpts.place(relx=.32, rely=0.218)       
locateOpts.bind('<<ComboboxSelected>>', locate_changed)

# locate extensions
def locateext_changed(event):
    msg=locateextOpts.get()
    statusbar.config(text=msg)
    statusbar.update()

locateextstr=('@ - *.bash', '@ - *.bin', '@ - *.bmp', '@ - *.class', '@ - *.cfg',
              '@ - *.cpp', '@ - *.css', '@ - *.csv', '@ - *.efi', '@ - *.gz',
              '@ - *.gif', '@ - *.html', '@ - *.ini', '@ - *.java', '@ - *.jpg',
              '@ - *.js', '@ - *.log', '@ - *.linux', '@ - *.pdf', '@ - *.php',
              '@ - *.pl', '@ - *.png', '@ - *.py', '@ - *.rtf', '@ - *.tiff',
              '@ - *.txt', '@ - *.wav', '@ - *.zip')

locateextOptions= locateextstr
selected_locateext = tk.StringVar()
locateextOpts=ttk.Combobox(tab4, textvariable=selected_locateext, width=30)    
locateextOpts['values']=locateextOptions
locateextOpts['state']='readonly'
locateextOpts.current(0)
locateextOpts.place(relx=.32, rely=0.3368)       
locateextOpts.bind('<<ComboboxSelected>>', locateext_changed)


# new combined
def Popen_Function_Common(cmd2):
    cmd2 = cmd2.replace('-@', '')

    if ('*' in cmd2):
        if ('.conf' in cmd2):
            cmd = cmd2
            ctxt = cmd2.replace('*.', '')
            ctxt = ctxt.replace('/', '_')
            log = open(logpath + ctxt + '.txt', 'w')
        else:
            if ('*.' in cmd2):
                cmd = cmd2
                log = open(logpath + cmd2 + '.txt', 'w')
            else:
                cmd,opt = cmd2.split('*')
                log = open(logpath + cmd  + ' ' + opt + '.txt', 'w')
    else:
        if ('cpuinfo' in cmd2) or ('os-release' in cmd2) or ('sysctl' in cmd2):
            cmd = cmd2
            cmd2 = cmd2.replace('/', '_')
            log = open(logpath + cmd2 + '.txt', 'w')
        else:
            cmd = cmd2
            cmd2 = cmd2.replace('/', '_')
            log = open(logpath + cmd2  + '.txt', 'w')

    log.write(cmd + '\n\n')
    log.flush()  # <-- here's something not to forget!

    cmd = ('sudo -S ' + cmd)
    proc = subprocess.Popen(cmd.split(), bufsize=1, encoding='UTF-8', errors='ignore',
        stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)

    proc.stdin.write(mepaswrd)
    proc.stdin.write('\n')
    proc.stdin.flush()

    counter = 0
    for line in proc.stdout:
        if ("sysctl" in cmd) and ("grep" in cmd):
            a,b,c,d,e,f,g = cmd.split(' ')
            if (("abi." in line) and ("abi" in g) or ("debug." in line) and ("debug" in g) or
                ("dev." in line) and ("dev" in g) or ("fs." in line) and ("fs" in g) or
                ("kernel." in line) and ("kernel" in g) or ("net." in line) and ("net" in g) or
                ("user." in line) and ("user" in g) or ("vm." in line) and ("vm" in g)):
                line = line.replace("\x03", "")  # works for the ETX control key
                line = line.replace("12", "")
                line = line.replace("   Memory top 5", " : Memory top 5")
                line2 = ('{:02d}: {}'.format(counter, line))
                counter = counter + 1
                log.write(line2)
        else:
            line = line.replace("\x03","")  # works for the ETX control key
            line = line.replace("12", "")
            line = line.replace("   Memory top 5", " : Memory top 5")
            line2 = ('{:02d}: {}'.format(counter, line))
            counter = counter + 1
            log.write(line2)

def Popen_Function_Run(cmd):
    cmdchk = cmd

    if ('vlc' in cmd):
        cmd = cmd
    else:
        cmd = 'sudo -S ' + cmd

    swtf = is_tool(cmdchk)
    if(swtf == True):
        proc = subprocess.Popen(cmd.split(), errors='ignore', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        proc.stdin.write(mepaswrd)
        proc.stdin.write('\n')
        proc.stdin.flush()
    else:
        openErrorWindow(cmd,cmdchk)

def Popen_Function_Url(cmd):
    if ("zoom" in cmd):
        webbrowser.open('https://support.zoom.us/hc/en-us/articles/206175806-Top-Questions')



# tab 1 button handlers
def fdisk1():
    Popen_Function_Common('fdisk -l')
def fdisk1b():
    Popen_Function_Common('man fdisk')

def nvidia2():
    msg = nvidiaOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('nvidia-smi -' + resultchoice)
def nvidia2b():
    Popen_Function_Common('man nvidia-smi')

def inxi3():
    msg = inxiOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('inxi -' + resultchoice)
def inxi3b():
    Popen_Function_Common('man inxi')

def dmidecode4():
    msg = dmidecodeOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('dmidecode -t ' + resultchoice + '*' + resultdesc)
def dmidecode4b():
    Popen_Function_Common('man dmidecode')

def xinput5():
    msg = xinputOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('xinput --' + resultchoice)
def xinput5b():
    Popen_Function_Common('man xinput')

def df6():
    msg = dfOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('df -' + resultchoice)
def df6b():
    Popen_Function_Common('man df')

def uname7():
    msg = unameOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('uname -' + resultchoice)
def uname7b():
    Popen_Function_Common('man uname')

def hostname8():
    msg = hostnameOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('hostname -' + resultchoice)
def hostname8b():
    Popen_Function_Common('man hostname')

def pip39():
    Popen_Function_Common('pip3 list')
def pip39b():
    Popen_Function_Common('man pip3')

def python310():
    Popen_Function_Common('python3 -V')
def python310b():
    Popen_Function_Common('man python3')

def lpstat11():
    msg = lpstatOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('lpstat -' + resultchoice)
def lpstat11b():
    Popen_Function_Common('man lpstat')

def whoami12():
    Popen_Function_Common('whoami')
def whoami12b():
    Popen_Function_Common('man whoami')

def dpkg13():
    Popen_Function_Common('dpkg -l')
def dpkg13b():
    Popen_Function_Common('man dpkg')

def free14():
    Popen_Function_Common('free -h')
def free14b():
    Popen_Function_Common('man free')

def lshw15():
    Popen_Function_Common('lshw')
def lshw15b():
    Popen_Function_Common('man lshw')

def lspci16():
    Popen_Function_Common('lspci -tv')
def lspci16b():
    Popen_Function_Common('man lspci')


# tab 2 button handlers
def ps21():
    Popen_Function_Common('ps')
def ps21b():
    Popen_Function_Common('man ps')

def pstree22():
    Popen_Function_Common('pstree')
def pstree22b():
    Popen_Function_Common('man pstree')

def du23():
    msg = duOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('du -' + resultchoice)
def du23b():
    Popen_Function_Common('man du')

def lsblk24():
    Popen_Function_Common('lsblk')
def lsblk24b():
    Popen_Function_Common('man lsblk')

def ifconfig25():
    msg = ifconfigOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('ifconfig -' + resultchoice)
    # -a List interfaces available
    # -s Short list
def ifconfig25b():
    Popen_Function_Common('man ifconfig')

def netstat26():
    msg = netstatOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('netstat -' + resultchoice)
def netstat26b():
    Popen_Function_Common('man netstat')

def ip27():
    msg = ipOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('ip ' + resultchoice)
def ip27b():
    Popen_Function_Common('man ip')

def ss28():
    msg = ssOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('ss ' + resultchoice)
def ss28b():
    Popen_Function_Common('man ss')

def lscpu29():
    Popen_Function_Common('lscpu')
def lscpu29b():
    Popen_Function_Common('man lscpu')

def lsusb30():
    Popen_Function_Common('lsusb -tv')
def lsusb30b():
    Popen_Function_Common('man lsusb')

def env31():
    Popen_Function_Common('env ')
def env31b():
    Popen_Function_Common('man env')

def ufw32():
    Popen_Function_Common('ufw status')
def ufw32b():
    Popen_Function_Common('man ufw')

def lspci33():
    Popen_Function_Common('lspci')
def lspci33b():
    Popen_Function_Common('man lspci')

def lsscsi34():
    Popen_Function_Common('lsscsi')
def lsscsi34b():
    Popen_Function_Common('man lsscsi')

def w35():
    Popen_Function_Common('w')
def w35b():
    Popen_Function_Common('man w')

def hwinfo36():
    Popen_Function_Common('hwinfo * --disk')
def hwinfo36b():
    Popen_Function_Common('man hwinfo')

def dmesg37():
    Popen_Function_Common('dmesg')
def dmesg37b():
    Popen_Function_Common('man dmesg')



# tab 3 button handlers
def blkid50():
    Popen_Function_Common('blkid')
def blkid50b():
    Popen_Function_Common('man blkid')

def ps51():
    Popen_Function_Common('ps -au')
def ps51b():
    Popen_Function_Common('man ps')

def findmnt52():
    Popen_Function_Common('findmnt')
def findmnt52b():
    Popen_Function_Common('man findmnt')

def ufw53():
    Popen_Function_Common('ufw status verbose')
def ufw53b():
    Popen_Function_Common('man ufw')

def parted54():
    Popen_Function_Common('parted -l')
def parted54b():
    Popen_Function_Common('man parted')

def who55():
    Popen_Function_Common('who')
def who55b():
    Popen_Function_Common('man who')

def lsb_release56():
    Popen_Function_Common('lsb_release -a')
def lsb_release56b():
    Popen_Function_Common('man lsb_release')

def osrelease57():
    Popen_Function_Common('cat /etc/os-release')
def osrelease57b():
    Popen_Function_Common('man os-release')

def lslogins58():
    Popen_Function_Common('lslogins -u')
def lslogins58b():
    Popen_Function_Common('man lslogins')

def hcitool69():
    Popen_Function_Common('hcitool dev')
def hcitool69b():
    Popen_Function_Common('man hcitool')

def cpuinfo70():
    Popen_Function_Common('cat /proc/cpuinfo')
def cpuinfo70b():
    Popen_Function_Common('man cat')

def sysctl71():
    Popen_Function_Common('cat /etc/sysctl.conf')
def sysctl71b():
    Popen_Function_Common('man cat')

def sysctl72():
    Popen_Function_Common('sysctl -a')
def sysctl72b():
    Popen_Function_Common('man sysctl')

def sysctl73():
    msg = sysctlOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('sysctl -a | grep ' + resultchoice)
def sysctl73b():
    Popen_Function_Common('man sysctl')

def ls74():
    Popen_Function_Common("pip3 list")
def ls74b():
    Popen_Function_Common('man pip3')


# list 4 button handlers
def lsbin70():
    Popen_Function_Common('ls /bin')
def lsbin70b():
    Popen_Function_Common('man ls')

def lsetc71():
    Popen_Function_Common('ls /etc')
def lsetc71b():
    Popen_Function_Common('man ls')

def lssbin72():
    Popen_Function_Common('ls /sbin')
def lssbin72b():
    Popen_Function_Common('man ls')

def listconf73():
    msg = locateOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('locate /' + resultdesc +'/*.conf')
def listconf73b():
    Popen_Function_Common('man locate')

def top75():
    msg = topOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    Popen_Function_Common('top -b -n1 -U ' + resultdesc)
def top75b():
    Popen_Function_Common('man top')

def locateext75():
        msg = locateextOpts.get()
        resultchoice, resultdesc = msg.split(' - ')
        Popen_Function_Common('locate ' + resultdesc)
def locateext75b():
        Popen_Function_Common('man locate')




# tab 5 run programs
def xed60():
    Popen_Function_Run('xed')
def xed60b():
    Popen_Function_Common('man xed')

def gparted61():
    Popen_Function_Run('gparted')
def gparted61b():
    Popen_Function_Common('man gparted')

def nvidia62():
    Popen_Function_Run('nvidia-settings')
def nvidia62b():
    Popen_Function_Common('man nvidia-settings --help')

def rhythmbox63():
    Popen_Function_Run('rhythmbox')
def rhythmbox63b():
    Popen_Function_Common('man rhythmbox')

def vlc64():
    Popen_Function_Run('vlc')
def vlc64b():
    Popen_Function_Common('man vlc')

def Zoom65():
    Popen_Function_Run('zoom')
def Zoom65b():
    Popen_Function_Url('zoom')

def psensor66():
    Popen_Function_Run('psensor')
def psensor66b():
    Popen_Function_Common('man psensor')




# TAB 1 TEXT & BUTTONS

# fdisk
text1 = Label(tab1, text="fdisk -l", fg="black", font=("Georgia", 10))
text1.place(x=156,y=25)
text1 = Label(tab1, text="lists disk(s) partition(s) table(s) information", fg="black", font=("Georgia", 10))
text1.place(x=530,y=25)
text1.pack

btn1=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=fdisk1)
btn1.place(x=25, y=20)
btn1.pack
btn1b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=fdisk1b)
btn1b.place(x=90, y=20)
btn1b.pack

# nvidia-smi
text2 = Label(tab1, text="nvidia-smi", fg="black", font=("Georgia", 10))
text2.place(x=156,y=53)
text2 = Label(tab1, text="Nvidia GPU driver or device(s) information", fg="black", font=("Georgia", 10))
text2.place(x=530,y=53)
text2.pack

btn2=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=nvidia2)
btn2.place(x=25, y=50)
btn2.pack
btn2b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=nvidia2b)
btn2b.place(x=90, y=50)
btn2b.pack

# inxi
text3 = Label(tab1, text="inxi", fg="black", font=("Georgia", 10))
text3.place(x=156,y=83)
text3 = Label(tab1, text="GPU / Distro repository information", fg="black", font=("Georgia", 10))
text3.place(x=530,y=83)
text3.pack

btn3=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=inxi3)
btn3.place(x=25, y=80)
btn3.pack
btn3b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=inxi3b)
btn3b.place(x=90, y=80)
btn3b.pack

# dmidecode
text4 = Label(tab1, text="dmidecode -t ", fg="black", font=("Georgia", 10))
text4.place(x=156,y=113)
text4 = Label(tab1, text="List DMI table information", fg="black", font=("Georgia", 10))
text4.place(x=530,y=113)
text4.pack

btn4=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dmidecode4)
btn4.place(x=25, y=110)
btn4.pack
btn4b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dmidecode4b)
btn4b.place(x=90, y=110)
btn4b.pack

# xinput
text5 = Label(tab1, text="xinput", fg="black", font=("Georgia", 10))
text5.place(x=156,y=143)
text5 = Label(tab1, text="List of available input devices", fg="black", font=("Georgia", 10))
text5.place(x=530,y=143)
text5.pack

btn5=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=xinput5)
btn5.place(x=25, y=140)
btn5.pack
btn5b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=xinput5b)
btn5b.place(x=90, y=140)
btn5b.pack

# df
text6 = Label(tab1, text="df", fg="black", font=("Georgia", 10))
text6.place(x=156,y=173)
text6 = Label(tab1, text="List file systems", fg="black", font=("Georgia", 10))
text6.place(x=530,y=173)
text6.pack

btn6=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=df6)
btn6.place(x=25, y=170)
btn6.pack
btn6b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=df6b)
btn6b.place(x=90, y=170)
btn6b.pack

# uname
text7 = Label(tab1, text="uname", fg="black", font=("Georgia", 10))
text7.place(x=156,y=202)
text7 = Label(tab1, text="List system information", fg="black", font=("Georgia", 10))
text7.place(x=530,y=202)
text7.pack

btn7=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=uname7)
btn7.place(x=25, y=200)
btn7.pack
btn7b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=uname7b)
btn7b.place(x=90, y=200)
btn7b.pack

# hostname
text8 = Label(tab1, text="hostname", fg="black", font=("Georgia", 10))
text8.place(x=156,y=234)
text8 = Label(tab1, text="My host name or ip address", fg="black", font=("Georgia", 10))
text8.place(x=530,y=234)
text8.pack

btn8=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hostname8)
btn8.place(x=25, y=230)
btn8.pack
btn8b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hostname8b)
btn8b.place(x=90, y=230)
btn8b.pack

# pip3
text9 = Label(tab1, text="pip3 list", fg="black", font=("Georgia", 10))
text9.place(x=156,y=263)
text9 = Label(tab1, text="List installed packages", fg="black", font=("Georgia", 10))
text9.place(x=530,y=263)
text9.pack

btn9=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=pip39)
btn9.place(x=25, y=260)
btn9.pack
btn9b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=pip39b)
btn9b.place(x=90, y=260)
btn9b.pack

# python3
text10 = Label(tab1, text="python3 -V", fg="black", font=("Georgia", 10))
text10.place(x=156,y=293)
text10 = Label(tab1, text="Python's version", fg="black", font=("Georgia", 10))
text10.place(x=530,y=293)
text10.pack

btn10=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=python310)
btn10.place(x=25, y=290)
btn10.pack
btn10b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=python310b)
btn10b.place(x=90, y=290)
btn10b.pack

# lpstat
text11 = Label(tab1, text="lpstat", fg="black", font=("Georgia", 10))
text11.place(x=156,y=324)
text11 = Label(tab1, text="Printer info [make sure printer is online]", fg="black", font=("Georgia", 10))
text11.place(x=530,y=324)
text11.pack

btn11=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lpstat11)
btn11.place(x=25, y=320)
btn11.pack
btn11b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lpstat11b)
btn11b.place(x=90, y=320)
btn11b.pack

# whoami
text12 = Label(tab1, text="whoami", fg="black", font=("Georgia", 10))
text12.place(x=156,y=354)
text12 = Label(tab1, text="Who am I", fg="black", font=("Georgia", 10))
text12.place(x=530,y=354)
text12.pack

btn12=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=whoami12)
btn12.place(x=25, y=350)
btn12.pack
btn12b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=whoami12b)
btn12b.place(x=90, y=350)
btn12b.pack

# dpkg
text13 = Label(tab1, text="dpkg -l", fg="black", font=("Georgia", 10))
text13.place(x=156,y=384)
text13 = Label(tab1, text="List all packages", fg="black", font=("Georgia", 10))
text13.place(x=530,y=384)
text13.pack

btn13=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dpkg13)
btn13.place(x=25, y=380)
btn13.pack
btn13b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dpkg13b)
btn13b.place(x=90, y=380)
btn13b.pack

# free
text14 = Label(tab1, text="free -h", fg="black", font=("Georgia", 10))
text14.place(x=156,y=414)
text14 = Label(tab1, text="Display free & used memory", fg="black", font=("Georgia", 10))
text14.place(x=530,y=414)
text14.pack

btn14=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=free14)
btn14.place(x=25, y=410)
btn14.pack
btn14b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=free14b)
btn14b.place(x=90, y=410)
btn14b.pack

# lshw
text15 = Label(tab1, text="lshw", fg="black", font=("Georgia", 10))
text15.place(x=156,y=444)
text15 = Label(tab1, text="List all hardware", fg="black", font=("Georgia", 10))
text15.place(x=530,y=444)
text15.pack

btn15=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lshw15)
btn15.place(x=25, y=440)
btn15.pack
btn15b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lshw15b)
btn15b.place(x=90, y=440)
btn15b.pack

# lspci
text16 = Label(tab1, text="lspci -tv", fg="black", font=("Georgia", 10))
text16.place(x=156,y=475)
text16 = Label(tab1, text="List all PCI devices", fg="black", font=("Georgia", 10))
text16.place(x=530,y=475)
text16.pack

btn16=Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lspci16)
btn16.place(x=25, y=470)
btn16.pack
btn16b=Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lspci16b)
btn16b.place(x=90, y=470)
btn16b.pack



# TAB 2 TEXT & BUTTONS

# ps
text21 = Label(tab2, text="ps", fg="black", font=("Georgia", 10))
text21.place(x=156,y=25)
text21 = Label(tab2, text="List all user processes", fg="black", font=("Georgia", 10))
text21.place(x=530,y=25)
text21.pack

btn21=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ps21)
btn21.place(x=25, y=20)
btn21.pack
btn21b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ps21b)
btn21b.place(x=90, y=20)
btn21b.pack

# pstree
text22 = Label(tab2, text="pstree", fg="black", font=("Georgia", 10))
text22.place(x=156,y=53)
text22 = Label(tab2, text="Show process tree", fg="black", font=("Georgia", 10))
text22.place(x=530,y=53)
text22.pack

btn22=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=pstree22)
btn22.place(x=25, y=50)
btn22.pack
btn22b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=pstree22b)
btn22b.place(x=90, y=50)
btn22b.pack

# du
text23 = Label(tab2, text="du", fg="black", font=("Georgia", 10))
text23.place(x=156,y=83)
text23 = Label(tab2, text="List disk usage", fg="black", font=("Georgia", 10))
text23.place(x=530,y=83)
text23.pack

btn23=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=du23)
btn23.place(x=25, y=80)
btn23.pack
btn23b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=du23b)
btn23b.place(x=90, y=80)
btn23b.pack

# lsblk
text24 = Label(tab2, text="lsblk", fg="black", font=("Georgia", 10))
text24.place(x=156,y=113)
text24 = Label(tab2, text="List all block devices", fg="black", font=("Georgia", 10))
text24.place(x=530,y=113)
text24.pack

btn24=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsblk24)
btn24.place(x=25, y=110)
btn24.pack
btn24b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsblk24b)
btn24b.place(x=90, y=110)
btn24b.pack

# ifconfig
text25 = Label(tab2, text="ifconfig", fg="black", font=("Georgia", 10))
text25.place(x=156,y=143)
text25 = Label(tab2, text="Show IP information", fg="black", font=("Georgia", 10))
text25.place(x=530,y=143)
text25.pack

btn25=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ifconfig25)
btn25.place(x=25, y=140)
btn25.pack
btn25b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ifconfig25b)
btn25b.place(x=90, y=140)
btn25b.pack

# netstat
text26 = Label(tab2, text="netstat", fg="black", font=("Georgia", 10))
text26.place(x=156,y=173)
text26 = Label(tab2, text="Kernel interface/routing tables", fg="black", font=("Georgia", 10))
text26.place(x=530,y=173)
text26.pack

btn26=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=netstat26)
btn26.place(x=25, y=170)
btn26.pack
btn26b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=netstat26b)
btn26b.place(x=90, y=170)
btn26b.pack

# ip
text27 = Label(tab2, text="ip", fg="black", font=("Georgia", 10))
text27.place(x=156,y=202)
text27 = Label(tab2, text="Show ip addresses or routing table", fg="black", font=("Georgia", 10))
text27.place(x=530,y=202)
text27.pack

btn27=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ip27)
btn27.place(x=25, y=200)
btn27.pack
btn27b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ip27b)
btn27b.place(x=90, y=200)
btn27b.pack

# ss
text28 = Label(tab2, text="ss", fg="black", font=("Georgia", 10))
text28.place(x=156,y=234)
text28 = Label(tab2, text="Investigate sockets", fg="black", font=("Georgia", 10))
text28.place(x=530,y=234)
text28.pack

btn28=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ss28)
btn28.place(x=25, y=230)
btn28.pack
btn28b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ss28b)
btn28b.place(x=90, y=230)
btn28b.pack

# lscpu
text29 = Label(tab2, text="lscpu", fg="black", font=("Georgia", 10))
text29.place(x=156,y=264)
text29 = Label(tab2, text="Show CPU architecture", fg="black", font=("Georgia", 10))
text29.place(x=530,y=264)
text29.pack

btn29=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lscpu29)
btn29.place(x=25, y=260)
btn29.pack
btn29b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lscpu29b)
btn29b.place(x=90, y=260)
btn29b.pack

# lsusb
text39 = Label(tab2, text="lsusb", fg="black", font=("Georgia", 10))
text39.place(x=156,y=294)
text39 = Label(tab2, text="Show USB devices", fg="black", font=("Georgia", 10))
text39.place(x=530,y=294)
text39.pack

btn30=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsusb30)
btn30.place(x=25, y=290)
btn30.pack
btn30b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsusb30b)
btn30b.place(x=90, y=290)
btn30b.pack

# env
text40 = Label(tab2, text="env", fg="black", font=("Georgia", 10))
text40.place(x=156,y=324)
text40 = Label(tab2, text="Display environmental variables", fg="black", font=("Georgia", 10))
text40.place(x=530,y=324)
text40.pack

btn31=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=env31)
btn31.place(x=25, y=320)
btn31.pack
btn31b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=env31b)
btn31b.place(x=90, y=320)
btn31b.pack

# ufw
text41 = Label(tab2, text="ufw", fg="black", font=("Georgia", 10))
text41.place(x=156,y=354)
text41 = Label(tab2, text="Firewall status", fg="black", font=("Georgia", 10))
text41.place(x=530,y=354)
text41.pack

btn32=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ufw32)
btn32.place(x=25, y=350)
btn32.pack
btn32b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ufw32b)
btn32b.place(x=90, y=350)
btn32b.pack

# lsscsi
text42 = Label(tab2, text="lsscsi", fg="black", font=("Georgia", 10))
text42.place(x=156,y=384)
text42 = Label(tab2, text="List SCSI disks", fg="black", font=("Georgia", 10))
text42.place(x=530,y=384)
text42.pack

btn34=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsscsi34)
btn34.place(x=25, y=380)
btn34.pack
btn34b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsscsi34b)
btn34b.place(x=90, y=380)
btn34b.pack

# w
text43 = Label(tab2, text="w", fg="black", font=("Georgia", 10))
text43.place(x=156,y=414)
text43 = Label(tab2, text="Who is logged in & doing what", fg="black", font=("Georgia", 10))
text43.place(x=530,y=414)
text43.pack

btn35=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=w35)
btn35.place(x=25, y=410)
btn35.pack
btn35b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=w35b)
btn35b.place(x=90, y=410)
btn35b.pack

# hwinfo
text44 = Label(tab2, text="hwinfo --disk", fg="black", font=("Georgia", 10))
text44.place(x=156,y=444)
text44 = Label(tab2, text="Probe for hardware", fg="black", font=("Georgia", 10))
text44.place(x=530,y=444)
text44.pack

btn36=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hwinfo36)
btn36.place(x=25, y=440)
btn36.pack
btn36b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hwinfo36b)
btn36b.place(x=90, y=440)
btn36b.pack

# dmesg
text45 = Label(tab2, text="dmesg", fg="black", font=("Georgia", 10))
text45.place(x=156,y=474)
text45 = Label(tab2, text="Display Kernal ring buffer messages", fg="black", font=("Georgia", 10))
text45.place(x=530,y=474)
text45.pack

btn37=Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dmesg37)
btn37.place(x=25, y=470)
btn37.pack
btn37b=Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dmesg37b)
btn37b.place(x=90, y=470)
btn37b.pack



# TAB 3 TEXT & BUTTONS

# blkid
text50 = Label(tab3, text="blkid", fg="black", font=("Georgia", 10))
text50.place(x=156,y=25)
text50 = Label(tab3, text="locate/print block device attributes", fg="black", font=("Georgia", 10))
text50.place(x=530,y=25)
text50.pack

btn50=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=blkid50)
btn50.place(x=25, y=20)
btn50.pack
btn50b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=blkid50b)
btn50b.place(x=90, y=20)
btn50b.pack

# ps
text51 = Label(tab3, text="ps -au", fg="black", font=("Georgia", 10))
text51.place(x=156,y=55)
text51 = Label(tab3, text="Display a list of all users' processes", fg="black", font=("Georgia", 10))
text51.place(x=530,y=55)
text51.pack

btn51=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ps51)
btn51.place(x=25, y=50)
btn51.pack
btn51b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ps51b)
btn51b.place(x=90, y=50)
btn51b.pack

# findmnt
text52 = Label(tab3, text="findmnt", fg="black", font=("Georgia", 10))
text52.place(x=156,y=85)
text52 = Label(tab3, text="List all mounted filesystems", fg="black", font=("Georgia", 10))
text52.place(x=530,y=85)
text52.pack

btn52=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=findmnt52)
btn52.place(x=25, y=80)
btn52.pack
btn52b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=findmnt52b)
btn52b.place(x=90, y=80)
btn52b.pack

# ufw
text53 = Label(tab3, text="ufw", fg="black", font=("Georgia", 10))
text53.place(x=156,y=115)
text53 = Label(tab3, text="Show ufw status verbose", fg="black", font=("Georgia", 10))
text53.place(x=530,y=115)
text53.pack

btn53=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ufw53)
btn53.place(x=25, y=110)
btn53.pack
btn53b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ufw53b)
btn53b.place(x=90, y=110)
btn53b.pack

# parted
text54 = Label(tab3, text="parted", fg="black", font=("Georgia", 10))
text54.place(x=156,y=145)
text54 = Label(tab3, text="Lists partition layout on all block devices", fg="black", font=("Georgia", 10))
text54.place(x=530,y=145)
text54.pack

btn54=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=parted54)
btn54.place(x=25, y=140)
btn54.pack
btn54b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=parted54b)
btn54b.place(x=90, y=140)
btn54b.pack

#  who
text55 = Label(tab3, text="who", fg="black", font=("Georgia", 10))
text55.place(x=156,y=175)
text55 = Label(tab3, text="List uses logged on", fg="black", font=("Georgia", 10))
text55.place(x=530,y=175)
text55.pack

btn55=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=who55)
btn55.place(x=25, y=170)
btn55.pack
btn55b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=who55b)
btn55b.place(x=90, y=170)
btn55b.pack

# lsb_release -a
text56 = Label(tab3, text="lsb_release -a", fg="black", font=("Georgia", 10))
text56.place(x=156,y=205)
text56 = Label(tab3, text="Distribution specific information", fg="black", font=("Georgia", 10))
text56.place(x=530,y=205)
text56.pack

btn56=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsb_release56)
btn56.place(x=25, y=200)
btn56.pack
btn56b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsb_release56b)
btn56b.place(x=90, y=200)
btn56b.pack

# os-release
text57 = Label(tab3, text="os-release", fg="black", font=("Georgia", 10))
text57.place(x=156,y=235)
text57 = Label(tab3, text="Operating system identification", fg="black", font=("Georgia", 10))
text57.place(x=530,y=235)
text57.pack

btn57=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=osrelease57)
btn57.place(x=25, y=230)
btn57.pack
btn57b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=osrelease57b)
btn57b.place(x=90, y=230)
btn57b.pack

# lslogins
text58 = Label(tab3, text="lslogins", fg="black", font=("Georgia", 10))
text58.place(x=156,y=265)
text58 = Label(tab3, text="Show all logins", fg="black", font=("Georgia", 10))
text58.place(x=530,y=265)
text58.pack

btn58=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lslogins58)
btn58.place(x=25, y=260)
btn58.pack
btn58b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lslogins58b)
btn58b.place(x=90, y=260)
btn58b.pack

# Psensor
text59 = Label(tab3, text="Psensor", fg="black", font=("Georgia", 10))
text59.place(x=156,y=295)
text59 = Label(tab3, text="Temperature monitoring application", fg="black", font=("Georgia", 10))
text59.place(x=530,y=295)
text59.pack

btn59=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=psensor66)
btn59.place(x=25, y=290)
btn59.pack
btn59b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=psensor66b)
btn59b.place(x=90, y=290)
btn59b.pack

# hcitool
text69 = Label(tab3, text="hcitool", fg="black", font=("Georgia", 10))
text69.place(x=156,y=325)
text69 = Label(tab3, text="Bluetooth connections", fg="black", font=("Georgia", 10))
text69.place(x=530,y=325)
text69.pack

btn69=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hcitool69)
btn69.place(x=25, y=320)
btn69.pack
btn69b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hcitool69b)
btn69b.place(x=90, y=320)
btn69b.pack

# cat /proc/cpuinfo.txt
text70 = Label(tab3, text="cat /proc/cpuinfo", fg="black", font=("Georgia", 10))
text70.place(x=156,y=355)
text70 = Label(tab3, text="CPU info all cores", fg="black", font=("Georgia", 10))
text70.place(x=530,y=355)
text70.pack

btn70=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=cpuinfo70)
btn70.place(x=25, y=350)
btn70.pack
btn70b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=cpuinfo70b)
btn70b.place(x=90, y=350)
btn70b.pack

# cat /proc/sysctl.conf
text71 = Label(tab3, text="cat /etc/sysctl.conf", fg="black", font=("Georgia", 10))
text71.place(x=156,y=385)
text71 = Label(tab3, text="Show all system variables", fg="black", font=("Georgia", 10))
text71.place(x=530,y=385)
text71.pack

btn71=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl71)
btn71.place(x=25, y=380)
btn71.pack
btn71b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl71b)
btn71b.place(x=90, y=380)
btn71b.pack

# sysctl
text72 = Label(tab3, text="sysctl -a", fg="black", font=("Georgia", 10))
text72.place(x=156,y=415)
text72 = Label(tab3, text="Show all kernel parameters & values", fg="black", font=("Georgia", 10))
text72.place(x=530,y=415)
text72.pack

btn72=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl72)
btn72.place(x=25, y=410)
btn72.pack
btn72b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl72b)
btn72b.place(x=90, y=410)
btn72b.pack

# sysctl -a | grep (choice)
text73 = Label(tab3, text="sysctl -a (select)", fg="black", font=("Georgia", 10))
text73.place(x=156,y=445)
text73 = Label(tab3, text="Show all selected parameters & values", fg="black", font=("Georgia", 10))
text73.place(x=530,y=445)
text73.pack

btn73=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl73)
btn73.place(x=25, y=440)
btn73.pack
btn73b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl73b)
btn73b.place(x=90, y=440)
btn73b.pack

# ls List installed packages
text74 = Label(tab3, text="list applications", fg="black", font=("Georgia", 10))
text74.place(x=156,y=475)
text74 = Label(tab3, text="List installed application packages & version", fg="black", font=("Georgia", 10))
text74.place(x=530,y=475)
text74.pack

btn74=Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ls74)
btn74.place(x=25, y=470)
btn74.pack
btn74b=Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ls74b)
btn74b.place(x=90, y=470)
btn74b.pack



# TAB 4 TEXT & BUTTON

# ls bin
text70 = Label(tab4, text="ls bin", fg="black", font=("Georgia", 10))
text70.place(x=156,y=25)
text70 = Label(tab4, text="List files in 'bin'", fg="black", font=("Georgia", 10))
text70.place(x=530,y=25)
text70.pack

btn70=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsbin70)
btn70.place(x=25, y=20)
btn70.pack
btn70b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsbin70b)
btn70b.place(x=90, y=20)
btn70b.pack

# ls etc
text71 = Label(tab4, text="ls etc", fg="black", font=("Georgia", 10))
text71.place(x=156,y=55)
text71 = Label(tab4, text="List files in 'etc'", fg="black", font=("Georgia", 10))
text71.place(x=530,y=55)
text71.pack

btn71=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsetc71)
btn71.place(x=25, y=50)
btn71.pack
btn71b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsetc71b)
btn71b.place(x=90, y=50)
btn71b.pack

# ls sbin
text72 = Label(tab4, text="ls sbin", fg="black", font=("Georgia", 10))
text72.place(x=156,y=85)
text72 = Label(tab4, text="List files in 'sbin'", fg="black", font=("Georgia", 10))
text72.place(x=530,y=85)
text72.pack

btn72=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lssbin72)
btn72.place(x=25, y=80)
btn72.pack
btn72b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lssbin72b)
btn72b.place(x=90, y=80)
btn72b.pack

# list all .conf
text73 = Label(tab4, text="locate", fg="black", font=("Georgia", 10))
text73.place(x=156,y=115)
text73 = Label(tab4, text="Locate '.conf' files", fg="black", font=("Georgia", 10))
text73.place(x=530,y=115)
text73.pack

btn73=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=listconf73)
btn73.place(x=25, y=110)
btn73.pack
btn73b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=listconf73b)
btn73b.place(x=90, y=110)
btn73b.pack


# top
text75 = Label(tab4, text="top", fg="black", font=("Georgia", 10))
text75.place(x=156,y=145)
text75 = Label(tab4, text="Display Linux processes (once)", fg="black", font=("Georgia", 10))
text75.place(x=530,y=145)
text75.pack

btn75=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=top75)
btn75.place(x=25, y=140)
btn75.pack
btn75b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=top75b)
btn75b.place(x=90, y=140)
btn75b.pack

# locate extenions
text76 = Label(tab4, text="locate", fg="black", font=("Georgia", 10))
text76.place(x=156,y=175)
text76 = Label(tab4, text="Locate extensions", fg="black", font=("Georgia", 10))
text76.place(x=530,y=175)
text76.pack

btn76=Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=locateext75)
btn76.place(x=25, y=170)
btn76.pack
btn76b=Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=locateext75b)
btn76b.place(x=90, y=170)
btn76.pack



# TAB 5 Run & BUTTONS

# xed
text60 = Label(tab5, text="xed", fg="black", font=("Georgia", 10))
text60.place(x=156,y=25)
text60 = Label(tab5, text="Text editor (root)", fg="black", font=("Georgia", 10))
text60.place(x=530,y=25)
text60.pack

btn60=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=xed60)
btn60.place(x=25, y=20)
btn60.pack
btn60b=Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=xed60b)
btn60b.place(x=90, y=20)
btn60b.pack

# gparted
text61 = Label(tab5, text="gparted", fg="black", font=("Georgia", 10))
text61.place(x=156,y=55)
text61 = Label(tab5, text="Partition editor (caution)", fg="black", font=("Georgia", 10))
text61.place(x=530,y=55)
text61.pack

btn61=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=gparted61)
btn61.place(x=25, y=50)
btn61.pack
btn61b=Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=gparted61b)
btn61b.place(x=90, y=50)
btn61b.pack

# nvidia server settings
text62 = Label(tab5, text="Nvidia", fg="black", font=("Georgia", 10))
text62.place(x=156,y=85)
text62 = Label(tab5, text="Server settings", fg="black", font=("Georgia", 10))
text62.place(x=530,y=85)
text62.pack

btn62=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=nvidia62)
btn62.place(x=25, y=80)
btn62.pack
btn62b=Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=nvidia62b)
btn62b.place(x=90, y=80)
btn62b.pack

# rhythmbox
text62 = Label(tab5, text="rhythmbox", fg="black", font=("Georgia", 10))
text62.place(x=156,y=115)
text62 = Label(tab5, text="rhythmbox music player", fg="black", font=("Georgia", 10))
text62.place(x=530,y=115)
text62.pack

btn62=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=rhythmbox63)
btn62.place(x=25, y=110)
btn62.pack
btn62b=Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=rhythmbox63b)
btn62b.place(x=90, y=110)
btn62b.pack

# vlc media player
text63 = Label(tab5, text="vlc", fg="black", font=("Georgia", 10))
text63.place(x=156,y=145)
text63 = Label(tab5, text="vlc media player", fg="black", font=("Georgia", 10))
text63.place(x=530,y=145)
text63.pack

btn63=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=vlc64)
btn63.place(x=25, y=140)
btn63.pack
btn63b=Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=vlc64b)
btn63b.place(x=90, y=140)
btn63b.pack

# Zoom
text64 = Label(tab5, text="Zoom", fg="black", font=("Georgia", 10))
text64.place(x=156,y=175)
text64 = Label(tab5, text="Zoom Meetings - video teleconferencing", fg="black", font=("Georgia", 10))
text64.place(x=530,y=175)
text64.pack

btn64=Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=Zoom65)
btn64.place(x=25, y=170)
btn64.pack
btn64b=Button(tab5, text="Url", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=Zoom65b)
btn64b.place(x=90, y=170)
btn64b.pack




# TAB 6 Run & BUTTONS

# ?
text80 = Label(tab6, text="?", fg="black", font=("Georgia", 10))
text80.place(x=156,y=25)
text80 = Label(tab6, text="?", fg="black", font=("Georgia", 10))
text80.place(x=530,y=25)
text80.pack

btn80=Button(tab6, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=NONE)
btn80.place(x=25, y=20)
btn80.pack
btn80b=Button(tab6, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=NONE)
btn80b.place(x=90, y=20)
btn80b.pack


# menus
menubar = Menu(root, bg="#A9A9A9", relief=FLAT)
filemenu = Menu(menubar, tearoff='off')

#filemenu.add_command(label="Open", font=("Georgia", 10), activeforeground="#FF00FF", command=NONE)
filemenu.add_command(label="Exit", font=("Georgia", 10), activeforeground="#FF00FF", command=buttonquithandler)
menubar.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu)

editmenu = Menu(menubar, tearoff='off')
menubar.add_cascade(label="Help", font=("Georgia", 10), activeforeground="#FF00FF", menu=editmenu)
editmenu.add_command(label="About", font=("Georgia", 10), activeforeground="#FF00FF", command=openNewWindow)

mintmenu = Menu(menubar, tearoff='off')
menubar.add_command(label="!Mint Forum", font=("Georgia", 10), activeforeground="#FF00FF",command=urlmint)

distrosmenu = Menu(menubar, tearoff='off')
menubar.add_command(label="!Distros Watch", font=("Georgia", 10), activeforeground="#FF00FF",command=urldistros)

whoami = Menu(menubar, tearoff='off')
menubar.add_command(label='    Login name: ' + findme, font=("Georgia", 10), foreground="cyan",command=NONE)

root.config(menu=menubar)
root.mainloop()
