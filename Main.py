import time
import os
import platform

import Util
import Logic
import LogicPrep
#################### st env ####################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/KimNahye/20210217_ML/WORK_DIR_4_remove_motif_error/"

IN = 'input/'
OU = 'output/'

# input file must be tsv format with ".txt" extension
MOTIF_ERROR_FL = 'RY_ABE8e_V106W_pattern_raw.txt'

os.makedirs(WORK_DIR + IN, exist_ok=True)
os.makedirs(WORK_DIR + OU, exist_ok=True)

#################### en env ####################


def recount_motif_error():
    util = Util.Utils()
    logic = Logic.Logics()
    logic_prep = LogicPrep.LogicPreps()

    motif_err_fl = util.read_tsv_ignore_N_line(WORK_DIR + IN + MOTIF_ERROR_FL)

    # filter out missing values
    flted_1_motif_err_fl = logic_prep.filterout_ele_w_trgt_str(motif_err_fl, 3, '-')
    motif_err_fl.clear()
    # #NAME? is removed
    flted_2_motif_err_fl = logic_prep.filterout_ele_w_trgt_str(flted_1_motif_err_fl, 3, 'N')
    flted_1_motif_err_fl.clear()
    flted_3_motif_err_fl = logic_prep.filterout_ele_w_trgt_str(flted_2_motif_err_fl, 3, 'n')
    flted_2_motif_err_fl.clear()

    motif_err_dict = logic_prep.make_list_to_dict_by_elekey(flted_3_motif_err_fl, 0)

    result_list = logic.recount_total_proportion_by_dictkey(motif_err_dict, 4)

    head = ['Filename', 'INDEX', 'seq', 'Motif', 'Count', 'Total_cnt', 'Proportion', 'Substitution']
    util.make_excel(WORK_DIR + OU + 'new_' + MOTIF_ERROR_FL.replace('.txt', ''), head, result_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    recount_motif_error()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))
