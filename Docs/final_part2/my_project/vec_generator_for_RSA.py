import time
start_time = time.time()

## Coversion between decimal number and binary number
def dec_to_bin (num,width):
    the_num = num
    bin_str = ''
    if (num < 0 or num >= 2 ** width):
            print('the parameter must be [0,' + str(2 ** width - 1) + ']!')
    else:
        for num in range(width):
            bin_str = str(the_num % 2) + ' ' + bin_str 
            the_num = int(the_num / 2)
        return bin_str

## Judges if two integers are coprime pair
## Returns True or False
def isCoprime(num_a, num_b) :
    t = 0
    while num_b >0 :
        t = num_a % num_b
        num_a = num_b
        num_b = t
    if num_a == 1 :
        return True
    else :
        return False  

## Gets values of sk and rk based on Extended Euclidean Algorithm: a * sk + b * tk = 1
## Returns a list: [sk, tk]
## For this lab, int_a = R, int_b = N
def getEucildean(int_a, int_b) :
    r0 = int_a; r1 = int_b; s0 = 1; s1 = 0; t0 = 0; t1 = 1; q = int(r0 /r1)
    while r1 != 0 :
        r_temp = r1; r1 = r0 -q * r1; r0 = r_temp 
        s_temp = s1; s1 = s0 - q * s1; s0 = s_temp
        t_temp = t1; t1 = t0 - q * t1; t0 = t_temp
        if r1 != 0 :
            q = int(r0 / r1)
    return [s0, t0]

## Generated the valus of R_inverse and N_inverse based on value of R and N 
## Used by MM block
## Returns [R_inverse, N_inverse]
def getRInverse_NInverse_for_MM (r, n) :
    temp = getEucildean(r, n)
    if ((temp[0] > 0)  and (temp[1] < 0)) :
        return [temp[0], -temp[1]]
    else :
        return [temp[0] + n, r - temp[1]]
 
def getP_inv_Q_inv(p,q) :
    temp = getEucildean(p,q)
    num_pi = 0; num_qi = 0
    if temp[0] >= 0 :
        num_pi = temp[0]
    else :
        num_pi = temp[0] + q
    if temp[1] >= 0 :
        num_qi = temp[1]
    else :
        num_qi = temp[1] + p

    return [num_pi, num_qi]


## Return the random number of inputs and the results of outputs (kept in order)
def getRandom(inputs,outputs) :
    import random
    out = [None] * (len(inputs) + len(outputs))
    num_r = 2 ** 7
    ############CUSTOMIZED THE INPUT################
    num_c = 6757 ##dummy value
    num_d = 6593 ##dummy value
    num_p = 103 ##dummy value
    num_q = 89 ##dummy value
    ##################################################

    ############Generation of other inputs based on the inputs c, d, p, q which are given by user###########################################
    num_pm1 = num_p - 1
    num_qm1 = num_q - 1
    num_pr = int((2**14) / num_p)
    num_qr = int((2**14) / num_q)
    num_pm1r = int((2**14) / num_pm1)
    num_qm1r = int((2**14) / num_qm1)
    num_pmm = getRInverse_NInverse_for_MM(num_r, num_p)[1]
    num_qmm = getRInverse_NInverse_for_MM(num_r, num_q)[1]
    (num_pi, num_qi) = getP_inv_Q_inv(num_p, num_q) 
    num_rp = (num_r ** 2) % num_p
    num_rq = (num_r ** 2) % num_q
    num_cp = num_c % num_p
    num_cq = num_c % num_q
    num_dp = num_d % (num_pm1)
    num_dq = num_d % (num_qm1)
    num_mp = (num_cp ** num_dp) % num_p
    num_mq = (num_cq ** num_dq) % num_q

    if (num_mp - num_mq) >=0 :
        num_h = (num_qi * (num_mp - num_mq)) % num_p
    else :
        num_h = (num_qi * (num_mp - num_mq + num_p)) % num_p
    num_m = num_q * num_h + num_mq

    num_n = num_p * num_q
    num_check = num_p * num_pi + num_qi * num_q
    if num_check % num_n == 1 :
        print('Bazout identity satisfied!!')
    else :
        print('Bazout identity failed to check!')
    

    ##########################################################################################################################################
    #"""
    out[inputs.index('P')] = num_p
    out[inputs.index('Q')] = num_q
    out[inputs.index('P-1')] = num_pm1
    out[inputs.index('Q-1')] = num_qm1
    out[inputs.index('P_R')] = num_pr
    out[inputs.index('Q_R')] = num_qr
    out[inputs.index('P-1_R')] = num_pm1r
    out[inputs.index('Q-1_R')] = num_qm1r
    out[inputs.index('C')] = num_c
    out[inputs.index('D')] = num_d
    out[inputs.index('Q_I')] = num_qi
    out[inputs.index('P_MM')] = num_pmm
    out[inputs.index('Q_MM')] = num_qmm
    out[inputs.index('Rp')] = num_rp
    out[inputs.index('Rq')] = num_rq
    out[outputs.index('M') + len(inputs)] = num_m
    return out
    #""""

    
def vec_generator (inputs = ['P','Q','P-1','Q-1','P_R','Q_R','P-1_R','Q-1_R','C','D','Q_I','P_MM','Q_MM','Rp','Rq'], inputs_width = [7,7,7,7,14,14,14,14,14,14,7,7,7,7,7], outputs = ['M'], outputs_width = [7],  number = 30, 
                    clk = 20, delay = 2, unit = 'ns', slope = 0.01, vih = 1.8, vil = 0,
                    file_path = '/Users/yihaowang/Desktop', file_name = 'super_test_final_3.vec'):
    if (len(inputs) != len(inputs_width)) or (len(outputs_width) != len(outputs)) or (number < 0) or (clk <= 0) or (delay < 0) or(slope < 0) :
        print('Parameter Error!')
    else :
        import os
        import random

        os.chdir(file_path)
        with open(file_name, 'w') as the_file, open(file_name.split('.')[0] + '_golden.txt', 'w') as the_golden :
        
            print('radix', end = ' ', file = the_file)
            length = 0
            for i in inputs_width :
                length += i
            for i in range(length) :
                print('1', end = ' ', file = the_file)
        
            print('\nio', end = ' ', file = the_file)
            for i in range(length) :
                print('i', end = ' ', file = the_file)
        
            print('\nvname', end = ' ', file = the_file)
            for i in range(len(inputs)) :
                for j in range(inputs_width[i]) :
                    print(inputs[i] + '<' + str(inputs_width[i] - j - 1) + '>', end = ' ', file = the_file)
            print('\ntunit ' + unit , file = the_file)
            print('slope ' + str(slope), file = the_file)
            print('vih ' + str(vih), file = the_file)
            print('vil ' + str(vil), file = the_file)

            time = delay 
            for i in range(number) :

                random_num = getRandom(inputs, outputs)

                print('\n' + str(time), end = '    ', file = the_golden)
                print('\n' + str(time), end = '    ', file = the_file)
                for j in range(len(inputs)) :
                    print(inputs[j] + '=' + str(random_num[j]), end = ' ', file = the_golden)
                    print(dec_to_bin(random_num[j], inputs_width[j]), end = ' ', file = the_file)
                for j in range(len(outputs)) :
                    print(outputs[j] + '=' + str(random_num[len(inputs) + j]), end = '', file = the_golden)
                time += clk
        
            print('Successfully Gnererated!')


vec_generator(number = 1, clk = 20, delay = 5)

#print(getRInverse_NInverse_for_MM(128,113))
#getRandom([],[])

end_time = time.time()
print('Run Time: %.6fs'%(end_time - start_time))





            
            
            
            
                
        
        
    

