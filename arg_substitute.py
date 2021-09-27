#! /pkg/qct/software/python/3.4.2/bin/python

import argparse
import os
import re
import sys
import collections
import logging,subprocess,json

from subprocess import Popen, PIPE

#Inputs Arg Template (ArgTemplate):
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block <block_name> -platform UFLEX -skip_check -update
#
#Input Arg value(ArgValue):
#	<block_name> TDF_ATPG_CTR TDF_ATPG_CTL TDF_ATPG_DDR TDF_ATPG_LPA TDF_ATPG_TOP
#		
#Expected Output:
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block TDF_ATPG_CTR -platform UFLEX -skip_check -update
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block TDF_ATPG_CTL -platform UFLEX -skip_check -update
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block TDF_ATPG_DDR -platform UFLEX -skip_check -update
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block TDF_ATPG_LPA -platform UFLEX -skip_check -update
#	gen_burst_with_microcode -chip bitra -rev r1_sec8lpu -block TDF_ATPG_TOP -platform UFLEX -skip_check -update



#Usage:
#Scaenario1:
#very first time
#t cd /prj/vlsi/pete/ptetools/dev/testcases/tss @@ tss testcase
#creates 
#~/ttag/cd.tag 
#/prj/vlsi/pete/ptetools/dev/testcases/tss @@ tss testcase
#empty file /prj/vlsi/pete/ptetools/dev/testcases/ttags/cd.tag if not present
#successive usage
#t cd test
#it will change the current dir to /prj/vlsi/pete/ptetools/dev/testcases/tss

#initialize tag directories ~/ttags/, /prj/vlsi/pete/ptetools/dev/testcases/ttags/
#assign default tag file
def initialize():
    global localTagPath,commonTagPath
    localTagPath = "~/ttags/"
    commonTagPath = "/prj/vlsi/pete/ptetools/dev/testcases/ttags/"
    #commonTagPathWin = "" #"\\qctdfsrt\prj\vlsi\pete\ptetools\dev\testcases\ttags\"
    binAreas = "/prj/vlsi/pete/ptetools/prod/bin,/prj/vlsi/pete/scripts/ptetools/bin"
    #binAreasWin = "\\qctdfsrt\prj\vlsi\pete\ptetools\prod\bin\,\\qctdfsrt\prj\vlsi\pete\scripts\ptetools\bin\"
    
#check if command has a tag file in the argument given
#else check if the cmd exists in binary area (binAreas)
#seperate the command and assign it as tag file
#def GetTags(CmdLineOpts): 
#    arguments_list = CmdLineOpts.split()
#	cmd = arguments_list[0]
#    global commonTagFile, localTagFile
	#p = subprocess.Popen(["which " + cmd],  stdout=PIPE, stderr=PIPE)          #else check for the cmd* file in binAreas
    #stdout, stderr = p.communicate()
    #command_args = stdout.decode("utf-8")
	#if stdout contains "cmd not found"
	#	commonTagFile = commonTagPath + "t.tag"
	#	localTagFile = localTagPath + "t.tag"
	#else
	#	if os.path.isfile(commonTagPath + cmd + "{0}.tag".format(cmd)):
	#		commonTagFile = commonTagPath + "{0}.tag"
	#	if os.path.isfile(localTagPath + "{0}.tag".format(arguments_list[0])):
	#		localTagFile = localTagPath + "{0}.tag"
#create tag file if not exists
	#if os.path.isnotfile(commonTagPath + commonTagFile):
	#	create (commonTagPath + cmd + commonTagFile)
	#if os.path.isnotfile(localTagPath + cmd + "{0}.tag".format(cmd)):
	#	create (localTagPath + localTagFile)
	
#def GetSearchKeys():
	#check if arguments contains @@ to save then split search key @@ result
	#else assign the search key
	
#def SearchNUpdate():
#check if search info is present and read the line, do a find and replace using sed
#else if update_flag is set then append at last

#def 
if __name__ == "__main__":
    cmdparser = argparse.ArgumentParser(
        description='Script to run the test cases. ')
    cmdparser.add_argument('-t', action='store', dest='ArgTemplate', default= None,
                           help='<t>. Provide command.', required=True)
    cmdparser.add_argument('-v', action='store', dest='ArgValue', default= None,
                           help='<v>. Provide command.', required=True)
    cmdparser.add_argument('-o', action='store', dest='out_file_arg', default= os.path.join(os.getcwd(), 'output_file_to_run'),
                           help='<o>. Provide command.', required=False)
    cmdlineopts = cmdparser.parse_args()
    ArgTemplate = cmdlineopts.ArgTemplate #.split()[0]
    ArgValue = ""
    if not os.path.isfile(cmdlineopts.ArgValue):
        ArgValue = cmdlineopts.ArgValue
    output_file = cmdlineopts.out_file_arg    
    #print (ArgTemplate.replace("<block_name>",ArgValue))
	
    pwd = os.getcwd()
    print (pwd + " " + cmdlineopts.ArgValue)
    #output_file = os.path.join(pwd, 'output_file_to_run')
    if os.path.isfile(output_file):
        os.remove(output_file)
    
    #i = 0        
    #for arg in arg_list:
       #print (arg)
     #  i = i+1
      # if i == 1: findStr = arg
       #if i > 1: print (cmdlineopts.ArgTemplate.replace(findStr,arg))
    if not ArgValue:
        template_file = open(cmdlineopts.ArgTemplate,'r')
        template = template_file.read()
        template_file.close()
        string_replace = re.findall('<\w+>',template)[0]
        list_file = open(cmdlineopts.ArgValue,'r')
        list_fi_data = list_file.readlines()
        list_file.close()
        arg_header = ""
        for arg_name in list_fi_data:
            if arg_header == "":
                arg_header = arg_name
            else:
                i = 0
                ttt = template
                for string_replace in arg_header.strip('\n').split(","):
                    new_string = arg_name.strip('\n').split(",")[i]
                    ttt = ttt.replace('<' + string_replace + '>', new_string)
                    i = i+1
                out_file = open (output_file,'a')
                out_file.write(ttt)
                out_file.close()

    else:
        arg_list = ArgValue.split(",")
        template_file = open(cmdlineopts.ArgTemplate,'r')
        template = template_file.read()
        template_file.close()
        string_replace = re.findall('<\w+>',template)
        for arg_name in arg_list:
            ttt = template.replace(string_replace,arg_name)
            out_file = open (output_file,'a')
            out_file.write(ttt)
            out_file.close()
    print('output created as output_file_to_run')
