""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2

Jeremy Domino 100919249 TPRG 2131-02

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
# Import Modules
import math

# Get values from user
def user_input(message):
    user = float(input(message))
    while user <= 0.0:
        user = float(input("The value must be greater than zero\n" + message))
        return user
    return user

# Calculate resonant frequency
def frequency(l,c):
    resfreq = 1 / (2 * math.pi * math.sqrt((l * 1.0e-3) * (c * 1.0e-6)))
    return resfreq

# Calculate Q factor
def qfactor(l,c,r):
    qfact = 1 / r * math.sqrt((l * 1.0e-3) / (c * 1.0e-6))
    return qfact

# Calculate bandwidth
def bandwidth(f,q):
    bandwidth = f / q
    return bandwidth

# Calculate the resistance if the circuit is in series or parallel
def resitance(sp, res1, res2):
    res = 0
    if sp == 's':
        res = res1 + res2
        return res
    else:
        res = 1 / ((1/res1) + (1/res2))
        return res

# Main program to calculate the bandwidth
def main():
    
    print("Series resonant circuit calculator\n(CTRL-C to quit)")

    while True:
        ser_par = input("Are the resistors in (s)eries or (p)arallel?: ")
        induct = user_input("What is the inductance in mH?: ")
        cap = user_input("What is the capacitance in uF?: ")
        res1 = user_input("What is the resistance of the first resistor in ohms?: ")
        res2 = user_input("What is the resistance of the second resistor in ohms?: ")
        resistance = resitance(ser_par, res1, res2)
        freq = frequency(induct, cap)
        qfact= qfactor(induct, cap, resistance)
        band = bandwidth(freq, qfact)
        
       
        print('The resonant frequency is', round(freq, 2))
        print('The Q factor is', round(qfact ,2))
        print('The bandwidth is', round(band ,2))

if __name__ == "__main__":
    main()
