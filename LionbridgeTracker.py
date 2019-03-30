#!/bin/env/ python
"""Automation of time tracking for Lionbridge Raterhub."""

__author__ = "Floyd Zamarripa"
__copyright__ = "Copyright 2019, Floydasaur.us"

# This a real rough faux-code of what
# I want this damn script to accomplish.
#
# import openyxl    # I operate in an Excel world, CSV could be done too I suppose if that's easier.
# 
# open workbook # must be in current working directory (cwd). os.getcwd() or os.chdir()
# make the sheet1 active if that's necessary # sheet = openpyxl.load_workbook('example.xlsx').get_sheet_by_name('Sheet1')
# sheet = wb.active
#
# Column Headers: Date | Start | Project | AET | End | Total Time
# ListenForKeypress()
# 
# StartTimeX
# On keypress(mouse7){
#    sheet['A1'] = today's date
#    sheet['A2'] = today's time # Start Time
#    sheet['A3'] = "x"
#    sheet['A4'] = getAET()
# }
#
# EndTimer
# On keypress(mouse9){ # my preferred mousebuttons
#     sheet['A5'] = today's time # End Time
#     sheet['A6'] = sheet['A5'].value - sheet['A2'].value # right?
#     
#
# getAET(){
#     return AET;
# }
