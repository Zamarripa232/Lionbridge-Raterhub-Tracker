#!/bin/env/ python
"""Automation of time tracking for Lionbridge Raterhub."""

__author__ = "Floyd Zamarripa"
__copyright__ = "Copyright 2019, Floydasaur.us"

# This a real rough faux-code of what
# I want this damn script to accomplish.
# import openyxl    # I operate in an Excel world, CSV could be done too I suppose if that's easier.
#
# AET = 1 # Probably the most common AET
# startXKey = key to look for to StartTimeX
# stopTimeKey = key to look for to EndTimer
# probably a start time for S as well, but I've never seen one actually come up.
#
# open workbook # must be in current working directory (cwd). os.getcwd() or os.chdir()
# make the sheet1 active if that's necessary # sheet = openpyxl.load_workbook('example.xlsx').get_sheet_by_name('Sheet1')
# sheet = wb.active
#
# Column Headers: ADate | BStart | CProject | DAET | EEnd | FTotal Time
# ListenForKeypress()
# 
# StartTimeX
# On keypress(mouse7){
#    sheet['A1'] = today's date
#    sheet['B1'] = today's time # Start Time
#    sheet['C1'] = "x"
#    sheet['D1'] = getAET()
# }
#
# EndTimer
# On keypress(mouse9){ # my preferred mousebuttons
#     sheet['E1'] = today's time # End Time
#     sheet['F1'] = sheet['A5'].value - sheet['A2'].value # right?
#     
#
# setAET(value){
#     AET = value
# }
#
# getAET(){
#     return AET;
# }
# 
# I guess at some point save the worksheet? how the f does openpyxl do this.
