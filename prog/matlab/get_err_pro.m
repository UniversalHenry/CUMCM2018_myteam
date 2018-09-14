function err_pro_1s = get_err_pro(time_1run)
err_pro_1time = 0.01;
err_pro_1s = 1 - (1-err_pro_1time).^(1./(time_1run));
end