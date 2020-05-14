# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:23:07 2018

@author: Saniyah
"""
   
import glob
import os
       
def tabs(n):
    return "  " * n

def end_div():
    return "</div>"

def qu(s):
    return "\'" + str(s) + "\'"

def dqu(s):
    return "\"" + str(s) + "\""

def openModal(names, images, caption, modal):
    s = "openModal(" + qu(names) + ", " + qu(images) + ", " + qu(caption) + ", " + qu(modal) + ")"
    return s

def imagediv(names, images, filename, tabinit, totalnum):
    s = tabs(tabinit) + "<div class=" + dqu(names) + ">" + "\n"
    s = s + tabs(tabinit + 1) + "<div class=\"numbertext\">" + "?" + " / "+ str(totalnum) + end_div() + "\n"
    s = s + tabs(tabinit + 1) + "<img class=" + dqu(images) + " src=" + dqu(filename) + " style=\"width:100%\" alt=\"\">" + "\n"
    s = s + tabs(tabinit) + end_div()
    return s
    
def mkgal(names, images, caption, modal, imgfoldr, pathfromloc):
    print("<!-- Photo Gallery -->")
    print("<div class=\"col-sm-4 sm-margin-b-50\">")
    print(tabs(1) + "<div class=\"margin-b-20\">")
    print(tabs(2) + "<div class=\"wow zoomIn\" data-wow-duration=\".3\" data-wow-delay=\".1s\">")
    print(tabs(3) + "<img src=\"FIRST IMAGE\" style=\"width:100%\" onclick=\"" + openModal(names, images, caption, modal) + ";currentSlide(1)\" class=\"hover-shadow cursor\">")
    print(tabs(2) + end_div())
    print(tabs(2) + "<div id=" + dqu(modal) + " class=\"modal\">")
    print(tabs(3) + "<span class=\"close cursor\" onclick=\"closeModal(" + qu(modal) + ")\">&times;</span>")
    print(tabs(4) + "<div class=\"modal-content\">")
    # get images and alt text
    os.chdir(imgfoldr)
    filelist = glob.glob("*.jpg")
    filelist.extend(glob.glob('*.png'))
    total = len(filelist)
    for f in filelist:
        #print(f)
        print(imagediv(names, images, pathfromloc + f, 5, total))
    print(tabs(5) + "<a class=\"prev\" onclick=\"plusSlides(-1)\">&#10094;</a>")
    print(tabs(5) + "<a class=\"next\" onclick=\"plusSlides(1)\">&#10095;</a>")
    print(tabs(5) + "<div class=\"caption-container\">")
    print(tabs(6) + "<p id=" + dqu(caption) + "></p>")
    print(tabs(5) + end_div())
    print(tabs(4) + end_div())
    print(tabs(3) + end_div())
    print(tabs(2) + end_div())
    print(tabs(1) + "<h4 style=\"text-align: center;\">YOUR TITLE HERE</h4>")
    print(tabs(1) + "<p> Description </p>")
    print(tabs(1) + " <a class=\"link\" href="" onclick=\"" +  openModal(names, images, caption, modal) + ";currentSlide(1)\" style=\"float: right\">View Gallery</a>")
    print(end_div())
    print("<!-- End Photo Gallery -->")