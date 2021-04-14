
from astroboi_bio_tools.ToolLogicPrep import ToolLogicPreps
class LogicPreps(ToolLogicPreps):
    def make_list_to_dict_by_elekey(self, input_list, key_idx):
        result_dict = {}
        for input_arr in input_list:
            if input_arr[key_idx] in result_dict:
                result_dict[input_arr[key_idx]].append(input_arr)
            else:
                result_dict.update({input_arr[key_idx]: [input_arr]})
        return result_dict

    def filterout_ele_w_trgt_str(self, input_list, arr_idx, trgt_str):
        return [input_arr for input_arr in input_list if trgt_str not in input_arr[arr_idx]]


