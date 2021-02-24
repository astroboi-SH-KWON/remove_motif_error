
from astroboi_bio_tools.ToolLogic import ToolLogics
class Logics(ToolLogics):
    def recount_total_proportion_by_dictkey(self, motif_err_dict, idx):
        result_list = []
        for key, val_list in motif_err_dict.items():
            tot = 0
            for val_arr in val_list:
                tot += int(val_arr[idx])

            for val_arr in val_list:
                tmp_arr = val_arr[:5]
                # new total
                tmp_arr.append(tot)
                # new proportion
                tmp_arr.append(int(val_arr[idx]) / tot)
                tmp_arr.append(val_arr[-1])
                result_list.append(tmp_arr)
        return result_list
