from basic_Matlab_to_Python.functions.basic_functions.Generate_Joint import generate_joint
from basic_Matlab_to_Python.functions.basic_functions.Reachable_ws_new import reachable_ws_new
from basic_Matlab_to_Python.functions.basic_functions.GlobalEvalution import global_evaluate
def workspace_analysis(robot, joint_num, type_robot):
    # Robot Workspace Analysis
    couple_flag = 0
    dynamic_flag = 0
    flag = [couple_flag, dynamic_flag]

    # Generate joint configurations
    qs, count = generate_joint(robot, flag, joint_num=joint_num, path=type_robot)

    # Reachable workspace + Local Evaluate
    indice_group = ["Manipulability", "Inverse Condition Number", "Minimum Singular Value"] \
        if type_robot != "HumanArm_Sim" else []

    dex, path, o_volume = reachable_ws_new(robot, qs, flag, indice=indice_group, opt_on='On', path=type_robot)

    if type_robot == "HumanArm_Sim":
        dex[:, 3] = 1

    # General form for Global Evaluation
    indices, global_indices = global_evaluate(dex, count, dynamic_flag, indice=indice_group)

    return global_indices, dex, o_volume
