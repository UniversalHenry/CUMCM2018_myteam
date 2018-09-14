function state = get_state_init(machine_type,varargin)
if strcpm(machine_type,'RGV')
    state.timer = 0;
    state.type = 'stay';%'stay','move','hold','clean'分别代表
    state.place = 1;%1,2,3,4分别代表
    state.move = [1,1];%[起始位置，终止位置]
    state.hold.CNC = 0;%0表示未上下料，1,2,3,4,5,6,7,8表示CNC数
    state.hold.thing = 0;%0表示未上下料，n表示第n道工序原料
end
if strcmp(machine_type,'CNC')
    state.order=varargin{1};
    state.timer = 0;
    state.thing = 0;%0表示无料，n表示第n道工序原料 
    state.type = 'stay';%'stay','work','error'
end
end