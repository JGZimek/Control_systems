import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

samples_number = 1000
time_horizon = 50
variance = 2

list_MSE = []
list_MSE2 = []
list_MSE3 = []
list_VAR = []
list_VAR2 = []
list_Hopt = []

x = np.linspace(0, 6 * np.pi, samples_number)
sin = np.sin(x)

def sin_noise_generator(sin, samples_number, variance):
    noise = (np.random.rand(samples_number) - 0.5) * np.sqrt(12 * variance)
    return sin + noise

def time_horizon_setter(iterator, time_horizon):
    if iterator < time_horizon:
        return 0
    else:
        return iterator - time_horizon


def func_MSE_H(sin, samples_number, variance, time_horizon):
    sin_noise = sin_noise_generator(sin, samples_number, variance)

    for h in range (1, time_horizon + 1):
        sin_denoised = []
        
        for i in range (1, len(sin_noise) + 1):
            sin_denoised.append(np.mean(sin_noise[time_horizon_setter(i,h):i]))
        
        MSE = np.mean((sin_denoised-sin)**2)
        list_MSE.append(MSE)

    print('Najmniejszy MSE: ', min(list_MSE), 'dla H: ', list_MSE.index(min(list_MSE))+1)
    print('Horyzont czasowy ustawiony na: ',len(list_MSE))

    plt.scatter(range(1,time_horizon+1),list_MSE,s=2 ,label='MSE(H)')
    plt.scatter(list_MSE.index(min(list_MSE))+1,min(list_MSE),s=6,color='red', label='Hopt')
    plt.xlabel('H')
    plt.ylabel('MSE')
    plt.legend(loc='lower right')
    plt.savefig('./Images/wykres_MSE(H)')
    plt.clf()
    
func_MSE_H(sin, samples_number, variance, time_horizon)

def func_MSE_VAR(sin, samples_number, variance, time_horizon):
    for v in np.arange(0.1, variance + 0.1, 0.02):
        sin_denoised = []
        sin_noise = sin_noise_generator(sin, samples_number, v)
        
        for i in range(1, len(sin_noise) + 1):
            sin_denoised.append(np.mean(sin_noise[time_horizon_setter(i, time_horizon):i]))

        MSE = np.mean((sin_denoised - sin) ** 2)
        list_MSE2.append(MSE)
        list_VAR.append(v)

    slope, intercept, r_value, p_value, std_err = stats.linregress(list_VAR, list_MSE2)
    best_fit_line = slope * np.array(list_VAR) + intercept
    
    plt.scatter(list_VAR, list_MSE2, s=1, label='MSE(var z_k)')
    plt.plot(list_VAR, best_fit_line, color = 'green', label='reglin MSE(var z_k)')
    plt.xlabel('var z_k')
    plt.ylabel('MSE')
    plt.legend()
    plt.savefig('./Images/wykres_MSE(var)')
    plt.clf()

func_MSE_VAR(sin,samples_number,variance,time_horizon)

def func_Hopt_VAR(sin, samples_number, variance, time_horizon):
    for v in np.arange(0.1, variance + 0.1, 0.02):
        sin_noise = sin_noise_generator(sin, samples_number, v)
        list_MSE3 = []        
        for h in range (1, time_horizon + 1):
            sin_denoised = []
            for i in range (1, len(sin_noise) + 1):
                sin_denoised.append(np.mean(sin_noise[time_horizon_setter(i,h):i]))
            
            MSE = np.mean((sin_denoised-sin)**2)
            list_MSE3.append(MSE)
            Hopt = list_MSE3.index(min(list_MSE3))+1
        
        list_Hopt.append(Hopt)
        list_VAR2.append(v)


    slope, intercept, r_value, p_value, std_err = stats.linregress(list_VAR2, list_Hopt)
    best_fit_line = slope * np.array(list_VAR2) + intercept

    plt.scatter(list_VAR2, list_Hopt, s=1, label='H_opt(var z_k)')
    plt.plot(list_VAR2, best_fit_line, color='green', label='reglin H_opt(var z_k)')
    plt.xlabel('var z_k')
    plt.ylabel('H_opt')
    plt.legend()
    plt.savefig('./Images/wykres_Hopt(var)')
    plt.clf()
        
func_Hopt_VAR(sin, samples_number, variance, time_horizon)


