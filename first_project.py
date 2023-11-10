import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

samples_number = 1000
time_horizon = 50
variance = 1

list_H = []
list_MSE = []
list_VAR = []
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
    
def sin_denoise_filter(sin_noise, h):
    sin_denoised = []
    for i in range (1, len(sin_noise) + 1):
        sin_denoised.append(np.mean(sin_noise[time_horizon_setter(i,h):i]))
    return sin_denoised

def linear_regress(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    best_fit_line = slope * np.array(x) + intercept
    return best_fit_line

def chart_ploter(list_x, list_y, chart_label, x_label, y_label, chart_name):
    plt.scatter(list_x, list_y, s = 1, label = chart_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig('./Charts_first_project/{}'.format(chart_name), transparent=True)
    plt.clf()
    print('Wykres {} wygenerowany.'.format(chart_name))

def func_MSE_H(sin, samples_number, variance, time_horizon):
    sin_noise = sin_noise_generator(sin, samples_number, variance)

    for h in range (1, time_horizon + 1):
        sin_denoised = sin_denoise_filter(sin_noise, h)
        MSE = np.mean((sin_denoised-sin)**2)
        list_MSE.append(MSE)
        list_H.append(h)

    print("Najmniejszy MSE: {:.4f} dla H: {}".format(min(list_MSE), list_MSE.index(min(list_MSE))+1))
    plt.scatter(list_MSE.index(min(list_MSE))+1,min(list_MSE), s=6, color='red', label='Hopt')
    chart_ploter(list_H, list_MSE, 'MSE(H)', 'H', 'MSE', 'MSE(H)')

    list_MSE.clear()
    list_H.clear()

def func_MSE_VAR(sin, samples_number, variance, time_horizon):
    for v in np.arange(0.1, variance + 0.1, 0.02):
        sin_noise = sin_noise_generator(sin, samples_number, v)
        
        sin_denoised = sin_denoise_filter(sin_noise, time_horizon)
        MSE = np.mean((sin_denoised - sin) ** 2)
        list_MSE.append(MSE)
        list_VAR.append(v)

    best_fit_line = linear_regress(list_VAR, list_MSE)
    plt.plot(list_VAR, best_fit_line, color = 'green', label='reglin MSE(var z_k)')
    chart_ploter(list_VAR, list_MSE, 'MSE(var z_k)', 'var z_k', 'MSE', 'MSE(var)')

    list_MSE.clear()
    list_VAR.clear()

def func_Hopt_VAR(sin, samples_number, variance, time_horizon):
    for v in np.arange(0.1, variance + 0.1, 0.02):
        sin_noise = sin_noise_generator(sin, samples_number, v)
        list_MSE.clear()        
        for h in range (1, time_horizon + 1):
            sin_denoised = sin_denoise_filter(sin_noise, h)     
            MSE = np.mean((sin_denoised-sin)**2)
            list_MSE.append(MSE)
            Hopt = list_MSE.index(min(list_MSE))+1
        
        list_Hopt.append(Hopt)
        list_VAR.append(v)

    best_fit_line = linear_regress(list_VAR,list_Hopt)
    plt.plot(list_VAR, best_fit_line, color='green', label='reglin H_opt(var z_k)')
    chart_ploter(list_VAR, list_Hopt, 'H_opt(var z_k)', 'var z_k', 'H_opt', 'Hopt(var)')

    list_MSE.clear()
    list_VAR.clear() 
    list_Hopt.clear()

func_MSE_H(sin, samples_number, variance, time_horizon)
func_MSE_VAR(sin,samples_number, variance, time_horizon)
func_Hopt_VAR(sin, samples_number, variance, time_horizon)