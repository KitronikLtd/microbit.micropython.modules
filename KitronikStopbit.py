# microbit-module: kitronikStopbit@1.0.0
# A module for the Kitronik Stopbit
# Copyright (c) Kitronik Ltd 2019. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from microbit import pin0
from microbit import pin1
from microbit import pin2

class Stopbit:
 # turn each LED on or off individually
 def Light(colour, illuminate):    
  if colour == "Red": 
   if illuminate == "On":
    pin0.write_digital(1)
   elif illuminate == "Off":
    pin0.write_digital(0)
  elif colour == "Yellow":
   if illuminate == "On":
    pin1.write_digital(1)
   elif illuminate == "Off":
    pin1.write_digital(0)  
  elif colour == "Green":
   if illuminate == "On":
    pin2.write_digital(1)
   elif illuminate == "Off":
    pin2.write_digital(0)     

 # turn each LED on or off individually
 def State(state): 
  if state == "stop":
   pin0.write_digital(1)
   pin1.write_digital(0)
   pin2.write_digital(0)
  elif state == "getReady":
   pin0.write_digital(1)
   pin1.write_digital(1)
   pin2.write_digital(0) 
  elif state == "go":
   pin0.write_digital(0)
   pin1.write_digital(0)
   pin2.write_digital(1)    
  elif state == "readyToStop":
   pin0.write_digital(0)
   pin1.write_digital(1)
   pin2.write_digital(0)    
