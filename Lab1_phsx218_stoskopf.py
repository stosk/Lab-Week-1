
# coding: utf-8

# $\alpha = \Delta L$ 

# In[6]:


import numpy as np
def rule3(errA,errB):
    errQ = np.sqrt(errA**2 + errB**2)
    return errQ

errT_i = 0.3 #C
errT_f = 0.1 #C

err_Delta_T = rule3(errT_i,errT_f)

print (err_Delta_T)
def rule4(Q,m,errA,A,n,errB,B,p,errC,C):
    errQ=Q*np.sqrt((m*(errA/A))**2+(n*(errB/B))**2+(p*(errC/C))**2)
    return errQ


# Will Stoskopf
# Jan 17, 2019
# Synthetic Data Thermal Expansion:
# Week 1 Lab

# $\alpha = \Delta L*L^{-1}*\Delta T^{-1}$ 

# $ \delta \alpha = \alpha\sqrt{(\frac{\delta \Delta L}{\Delta L})^2 + (\frac{- \delta L}{L})^2 + (\frac {- \delta \Delta T} {\Delta T})^2} $

# In[7]:


L=1.05 #m
err_L=0.001 #m
deltaL=0.00125 #m
err_deltaL=0.00001 #m
T_initial=23.4 
T_final=92.5
errT_initial=0.3
errT_final=0.1

Delta_T = T_final - T_initial
alpha = deltaL/(L*Delta_T)

print ("alpha=",alpha)


# In[12]:


delta_alpha = rule4(alpha,1,err_deltaL,deltaL,-1,err_L,L,-1,Delta_T,err_Delta_T)
print ("delta_alpha=", delta_alpha)

