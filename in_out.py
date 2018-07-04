##########################################################################
#                     INPUT AND OUTPUT ROUTINES                          #
##########################################################################
# Purpose:                                                               #
#          - A python module handling input and output.                  #
#                                                                        #
##########################################################################
# written by: Elke Fasshauer May 2018                                    #
##########################################################################

import sciconv
import numpy as np
from sys import exit

#-------------------------------------------------------------------------
#   input
def read_input(inputfile):
    f = open(inputfile, 'r')
    
    lines = f.readlines()
    
    for line in lines:
        words = line.split()
        if (words[0] == 'rdg_au'):
            rdg_au = float(words[2])
            print 'rdg_au = ', rdg_au
        elif (words[0] == 'cdg_au'):
            cdg_au = float(words[2])
            print 'cdg_au = ', cdg_au
    
    # energy parameters of the system
        elif (words[0] == 'Er_eV'):
            Er_eV = float(words[2])
            print 'Er_eV = ', Er_eV
        elif (words[0] == 'E_fin_eV'):
            E_fin_eV = float(words[2])
            print 'E_fin_eV = ', E_fin_eV
        elif (words[0] == 'tau_s'):
            tau_s = float(words[2])
            print 'tau_s = ', tau_s
    
    # exciting laser parameters
        elif (words[0] == 'Omega_eV'):
            Omega_eV = float(words[2])
            print 'Omega_eV = ', Omega_eV
        elif (words[0] == 'n_X'):
            n_X = float(words[2])
            print 'n_X = ', n_X
        elif (words[0] == 'I_X'):
            I_X = float(words[2])
            print 'I_X = ', I_X
    
    # dressing laser parameters
        elif (words[0] == 'omega_eV'):
            omega_eV = float(words[2])
            print 'omega_eV = ', omega_eV
        elif (words[0] == 'n_L'):
            n_L = float(words[2])
            print 'n_L = ', n_L
        elif (words[0] == 'I_L'):
            I_L = float(words[2])
            print 'I_L = ', I_L
        elif (words[0] == 'delta_t_s'):
            delta_t_s = float(words[2])
            print 'delta_t_s = ', delta_t_s
        elif (words[0] == 'phi'):
            phi = float(words[2])
            print 'phi = ', phi
        elif (words[0] == 'q'):
            q = float(words[2])
            print 'q = ', q
    
    # parameters of the simulation
        elif (words[0] == 'tmax_s'):
            tmax_s = float(words[2])
            print 'tmax_s = ', tmax_s
        elif (words[0] == 'timestep_s'):
            timestep_s = float(words[2])
            print 'timestep_s = ', timestep_s
        elif (words[0] == 'E_step_eV'):
            E_step_eV = float(words[2])
            print 'E_step_eV = ', E_step_eV
    
        elif (words[0] == 'E_min_eV'):
            E_min_eV = float(words[2])
            print 'E_min_eV = ', E_min_eV
        elif (words[0] == 'E_max_eV'):
            E_max_eV = float(words[2])
            print 'E_max_eV = ', E_max_eV
    
    f.close()
    return (rdg_au, cdg_au,
            Er_eV, E_fin_eV, tau_s,
            Omega_eV, n_X, I_X,
            omega_eV, n_L, I_L, delta_t_s, phi, q,
            tmax_s, timestep_s, E_step_eV,
            E_min_eV, E_max_eV)

#-------------------------------------------------------------------------
def check_input(Er, E_fin, Gamma,
                Omega, TX, n_X, A0X,
                omega, TL, A0L, delta_t,
                tmax, timestep, E_step):
    print 'Input Check'

    if (E_fin > Omega):
        exit('Warning: E_fin > Omega' + '\n'
             + 'Stopping Script')

    print 'Input fullfills requirements'

    return 0
    

#-------------------------------------------------------------------------
#   output
def prep_output(I, Omega_au, t_au):
#    square = np.absolute(I)**2
    Omega_eV = sciconv.hartree_to_ev(Omega_au)
    t_s = sciconv.atu_to_second(t_au)
    string = str(Omega_eV) + '   ' + format(t_s, '.18f') + '   ' + format(I, '.15f')
    return string

def doout(t_au, outlines):
    # output filename will give the time in ps
    t_s = sciconv.atu_to_second(t_au)
    t_ps = t_s * 1E12
    if t_ps < 0.0:
        t_ps = np.absolute(t_ps)
        filename = 'm' + format(t_ps, '.8f') + '.dat'
    else:
        filename = format(t_ps, '.8f') + '.dat'
    outfile = open(filename, mode='w')
    res_lines = '\n'.join(outlines)
    outfile.write(res_lines)
    outfile.close

def doout_1f(filename, outlines):
    res_lines = '\n'.join(outlines)
    res_lines = res_lines + '\n' + '' + '\n'
    filename.write(res_lines)
    #outfile.close
