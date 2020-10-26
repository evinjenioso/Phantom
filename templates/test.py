#!/usr/bin/env python3
from ics import Calendar, icalendar
from urllib.request import urlopen
import requests, urllib3
import arrow, datetime, argparse, random
import re, os, os.path, pathlib, shutil



### Support calendar items only
support_url = "https://linode4.humanity.com/ical/_449c24ca4dd0316a0653bcd383071b27.ics"
support_cal = Calendar(urlopen(support_url).read().decode('iso-8859-1'))
st = support_cal.timeline

today = arrow.now() # Set today as constant for current date&time
tomorrow = today + datetime.timedelta(days=1)
today_str = today.strftime("%B %d, %Y") # String the date to human-readable 
tom_str = tomorrow.strftime("%B %d, %Y")
this_magic_moment = today.strftime("%H")

date_list = [] # Empty list to append with raw dates
date_list_str = []  # Make empty list to append with date strings

def main():
    hour_range1 = this_magic_moment
    hour_range2 = 24
    today_low_coverage = []
    tom_low_coverage = []
    date_range1 = 0
    date_range2 = 2
    #print(this_magic_moment)
    #print(today_str)

## -------- Today -------- ##
    #print("\n" + today_str)
    for i in range(int(hour_range1), int(hour_range2)): # Check the window of 
        schedule_window = today.replace(hour=i, minute=5) 
        hour_string = schedule_window.format('hh a')
        low_hour_string = schedule_window.format('h a')
        peeps = 0

        for person in st.at(schedule_window.to('UTC')): # Check just Support schedule timeline (st)
            #print(support.name)      
            if(("Support" in person.name) and ("Senior" not in person.name and "Academy" not in person.name and "Leadership" not in person.name and "Shadow" not in person.name and "Leon" not in person.name)):
                peeps = peeps + 1 
                # Increase "peeps" by 1 for each Support member in schedule_window
                #support_on_now.append(person.name)
        if peeps < 4:
            today_low_coverage.append(low_hour_string)
            #print(hour_string)

## -------- Tomorrow -------- ##
    #print("\n" + tom_str)
    for i in range(0, 24): # Check full 24hrs for tomorrow
        schedule_window = tomorrow.replace(hour=i, minute=5) 
        hour_string = schedule_window.format('hh a')
        tom_low_hour_string = schedule_window.format('h a')
        peeps = 0

        for person in st.at(schedule_window.to('UTC')): # Check just Support schedule timeline (st)
            #print(support.name)      
            if(("Support" in person.name) and ("Senior" not in person.name and "Academy" not in person.name and "Leadership" not in person.name and "Shadow" not in person.name and "Leon" not in person.name)):
                peeps = peeps + 1 
                # Increase "peeps" by 1 for each Support member in schedule_window
                #support_on_now.append(person.name)
        if peeps < 4:
            tom_low_coverage.append(tom_low_hour_string)
            #print(hour_string)

    data = {"text":f"Hours of low coverage: \n{today_str}: \n{today_low_coverage} \n\n{tom_str}: {tom_low_coverage}"}
    mc2_hook = 'https://hooks.slack.com/services/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'
    response = requests.post(mc2_hook, json=data)

if __name__ == '__main__':
    main()