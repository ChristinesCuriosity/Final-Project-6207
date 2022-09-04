# Final-Project-6207
This past year I introduced the Crickit hat into my robotics curriculum to go along with the Circuit Playground Expresses that I was already using. I have been using javascript through MakeCode to instruct my students on how to use the microcomputers, as I did not want the code to be too intimidating for students who were new to it. So, I have a number of Circuit Playground Express microcontrollers around and I have been meaning to dig into using CircuitPython to code them. 

We have been through a once in a lifetime, unparalleled crisis over the past two and a half years teaching through COVID. I believe in preventative measures for all to keep students and teachers healthy and in school. I am inspired to create a program using CircuitPython and the Circuit Playground Express to help with the time needed to wash your hands at the sink. I thought that this process could be greatly improved especially considering how I shudder to think how many students do not wash their hands at all! (Thank goodness for 1:1 chromebooks!) The CDC says to thoroughly clean your hands you must, “Scrub your hands for at least 20 seconds. Need a timer? Hum the “Happy Birthday” song from beginning to end twice.” There must be a better timer than humming Happy Birthday twice. 

For this project I will be using the light sensor built into the circuit playground to initiate a timer. This timer will have two outputs, a neopixel light countdown and a .wav song to wash along to. When a user waves their hand in front of the circuit playground (light sensor) the timer will trigger. All 8 neopixels will light indicating the successful start of the program. Following that the lights will slowly turn off one by one as a visual timer while also playing a 20 second sound clip. 

Special Thanks to https://github.com/Neradoc 