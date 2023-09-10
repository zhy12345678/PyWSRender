def robot_map(num, *args, **kwargs):
    robot_type = 'Articulated'
    env_type = 'off'

    if 'Type' in kwargs:
        opt_type = kwargs['Type']
    else:
        opt_type = 'Robot'

    if opt_type == 'Robot':
        index_name = ['Articulated', 'Spherical', 'Cylindrical', 'Catersian', 'SCARA', 'Underactuated', 'Redandant', 'dVRK', 'Omni', 'HamlynCRM', 'MIS',
                      'puma560', 'stanford', 'Kuka_KR5', 'irb140', 'ABB_Yumi', 'ABB_irb140', 'Defined']
        index_num = list(range(1, len(index_name) + 1))
        robot_map = dict(zip(index_num, index_name))
        robot_type = robot_map.get(num, 'Articulated')
    elif opt_type == 'Environment':
        index_name = ['off', 'Desk_On', 'Frame_On', 'Both_On']
        index_num = [1, 2, 3, 4]
        environment_map = dict(zip(index_num, index_name))
        env_type = environment_map.get(num, 'off')

    return robot_type, env_type
