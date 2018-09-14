function attr = get_attr(setorder,contain_err,num_process,varargin)
attr.contain_err = contain_err;
attr.process.num = num_process;
data = load_data(setorder);
attr.RGV.steptime{1} = data.RGV.time1step;
attr.RGV.steptime{2} = data.RGV.time2step;
attr.RGV.steptime{3} = data.RGV.time3step;
if num_process == 1
    attr.CNC.process.time{1} = data.CNC.time1in1;
end
if num_process == 2
    attr.CNC.process.time{1} = data.CNC.time1in2;
    attr.CNC.process.time{2} = data.CNC.time2in2;
end
if contain_err
    for i = 1:numel(attr.CNC.process.time)
        attr.CNC.process.err{i} = get_err_pro(attr.CNC.process.time{i});
    end
end
end