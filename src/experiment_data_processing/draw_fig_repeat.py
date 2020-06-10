'''
Created on Oct 16, 2019

'''


import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

# higgs = np.array([1933.2504305839539, 304.152063369751, 184.0976972579956])

higgs = np.array([1933.2504305839539, 184.0976972579956])

cov = np.array([493.1432611942291, 106.6413266658783])

heartbeat = np.array([359.67488622665405, 111.03895092010498])


# cov_large_mem_use = np.array([12277039559.1111, 875520000])
# 
# higgs_mem_use = np.array([8398066574.22222, 5441662520.88889])
# 
# rc1_mem_use = np.array([291399286.949495, 250458567.111111])
# 
# lr_mem_use_less = np.array([247801628.444444, 242606080])
# 
# lr_mem_use_more = np.array([24462539889.7778, 5538706318.22222])





# mem_usage_list = np.array([1435711715.55556, 833290695.111111])

mem_usage_list = np.vstack([higgs, cov, heartbeat])

print(mem_usage_list.shape)

color_list = ['#ffb3ba', '#baffc9', '#b2cefe']

label_list = ['BaseL', 'PrIU-opt']


hatch_list = ['\\\\', '*', '//']


# dataset_labels = ['HIGGS']
dataset_labels = ['HIGGS (extended)', 'Cov (extended)', 'heartbeat (extended)']


# mem_usage_list = mem_usage_list


barWidth = 0.25
figure(figsize=(14,4))

r1 = np.arange(mem_usage_list.shape[0])

all_font_size = 20

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : all_font_size}
plt.rc('font', **font)


for i in range((mem_usage_list.shape[1])):
    if i > 0:
        r2 = [x + barWidth for x in r1]
        r1 = r2
        
    bars = plt.bar(r1, mem_usage_list[:,i], color=color_list[i], width=barWidth, edgecolor='black', label=label_list[i], hatch = hatch_list[i])

#     patterns = ('\\\\', '//')
#     for bar, pattern in zip(bars, patterns):
#         bar.set_hatch(pattern)
        

# objects = ('PrIU', 'BaseL')
# y_pos = np.arange(len(objects))
# 
# plt.xticks(y_pos, objects)


# plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(dataset_labels))], dataset_labels)


plt.ylabel('Execution time (s)', fontweight='bold')




plt.legend(loc = 'best')









# performance = [10,8,6,4,2,1]

# bars = plt.bar(y_pos, mem_usage_list, align='center', edgecolor='black', alpha=0.5, color=['#ffb3ba', '#baffc9'])



# plt.title('Memory usage comparison')
plt.savefig('../../scripts/repeated_run.eps', format='eps')
plt.show()