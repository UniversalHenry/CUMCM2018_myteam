function state = get_state_init(machine_type,varargin)
if strcpm(machine_type,'RGV')
    state.timer = 0;
    state.type = 'stay';%'stay','move','hold','clean'�ֱ����
    state.place = 1;%1,2,3,4�ֱ����
    state.move = [1,1];%[��ʼλ�ã���ֹλ��]
    state.hold.CNC = 0;%0��ʾδ�����ϣ�1,2,3,4,5,6,7,8��ʾCNC��
    state.hold.thing = 0;%0��ʾδ�����ϣ�n��ʾ��n������ԭ��
end
if strcmp(machine_type,'CNC')
    state.order=varargin{1};
    state.timer = 0;
    state.thing = 0;%0��ʾ���ϣ�n��ʾ��n������ԭ�� 
    state.type = 'stay';%'stay','work','error'
end
end