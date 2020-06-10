'''
Created on Mar 15, 2019

'''
import torch

import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/data_IO')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/Interpolation')


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from data_IO.Load_data import *
# from sensitivity_analysis.logistic_regression.Logistic_regression import test_X
    from sensitivity_analysis.DNN.utils import *
#     from sensitivity_analysis.linear_regression.evaluating_test_samples import *
    from sensitivity_analysis.DNN.DNN import *

except ImportError:
    from Load_data import *
# from sensitivity_analysis.logistic_regression.Logistic_regression import test_X
    from utils import *
#     from evaluating_test_samples import *
    from DNN import *






if __name__ == '__main__':
    
    
    configs = load_config_data(config_file)
    
    git_ignore_folder = configs['git_ignore_folder']
    
    sys_args = sys.argv

    origin_model = torch.load(git_ignore_folder + 'model_without_noise')
        
    alpha = torch.load(git_ignore_folder + 'alpha')
    
#     beta = torch.load(git_ignore_folder + 'beta')
    
    max_epoch = torch.load(git_ignore_folder+'epoch')
    
    X = torch.load(git_ignore_folder+'noise_X')
    
    Y = torch.load(git_ignore_folder+'noise_Y')
    
    test_X = torch.load(git_ignore_folder + 'test_X')
    
    test_Y = torch.load(git_ignore_folder + 'test_Y')
    
    hidden_dim = torch.load(git_ignore_folder + 'hidden_dims')
    
    
    input_dim = X.shape[1]
    
    num_class = torch.unique(Y).shape[0]
    
    output_dim = num_class
    
    model = DNNModel(input_dim, hidden_dim, output_dim)
    
    init_model(model, list(origin_model.parameters()))
    
    error = nn.CrossEntropyLoss()


    learning_rate = 0.1
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    
    model = model_update_standard_lib(max_epoch, X, Y, test_X, test_Y, alpha, error, model)
    
    print_model_para(model)
    
    
#     compute_model_para_diff(origin_model, model)
    
    
    torch.save(model, git_ignore_folder + 'model_standard_lib')    
    
    
    model_base_line = torch.load(git_ignore_folder + 'model_base_line')
    
    compute_model_para_diff(list(origin_model.parameters()), list(model.parameters()))

    
    
#     num_of_output = Y.shape[1]
#     
#     dim = X.shape
#     
#     print(X.shape)
#     
#     Y = Y.type(torch.DoubleTensor)
#     
#     sys_args = sys.argv
# 
#     
#     delta_num = int(10000)
# 
#     
#      
# #     delta_data_ids = random_generate_subset_ids(X.shape, delta_num)     
# #     torch.save(delta_data_ids, git_ignore_folder+'delta_data_ids')
# 
#     delta_data_ids = torch.load(git_ignore_folder + 'noise_data_ids')
#     
#     print(delta_data_ids.shape[0])
#     
#     max_epoch = torch.load(git_ignore_folder+'epoch')
#     
#     print(max_epoch)
# #     num_class = torch.unique(Y).shape[0]
#     
# #     delta_data_ids = torch.load(git_ignore_folder+'delta_data_ids')
#     
#     update_X, selected_rows = get_subset_training_data(X, X.shape, delta_data_ids)
#     
#     print(selected_rows.shape)
#     
#     update_Y, s_rows = get_subset_training_data(Y, Y.shape, delta_data_ids)
#     
#     #     res1 = update_model_parameters_from_the_scratch(update_X, update_Y)
#     
#     t1 = time.time()
#     
#     lr = initialize(update_X.shape, num_of_output)
# #     update_x_sum_by_class = compute_x_sum_by_class(update_X, update_Y, num_class, update_X.shape)
#     #     update_X_Y_mult = update_X.mul(update_Y)
#     #     res1 = update_model_parameters_from_the_scratch(update_X, update_Y)dim, theta,  X, Y, X_sum_by_class, num_class
#     res2 = linear_regression_standard_library(update_X, update_Y, lr, update_X.shape, max_epoch, alpha, beta)
# 
#     
#     t2 = time.time()
#     
#     
#     torch.save(res2, git_ignore_folder+'model_standard_lib')
#     
#     
#     test_X = torch.load(git_ignore_folder + 'test_X')
#     
#     test_Y = torch.load(git_ignore_folder + 'test_Y')
#     
#     print('training_accuracy::', compute_accuracy2(update_X, update_Y, res2))
#     
#     print('test_accuracy::', compute_accuracy2(test_X, test_Y, res2))
#     
#     print('training_time_standard_lib::', t2 - t1)
#     
#     print(res2)
    
    
    
    
    
    