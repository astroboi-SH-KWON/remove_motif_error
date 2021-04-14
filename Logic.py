
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
                if tot == 0:
                    tmp_arr.append(0.0)
                else:
                    tmp_arr.append(int(val_arr[idx]) / tot)
                tmp_arr.append(val_arr[-1])
                result_list.append(tmp_arr)
        return result_list

    def make_merged_list_to_dict_for_motiff_err(self, merged_list, key_idx, scnd_key_arr, deli_ch, val_idx):
        result_dict = {}
        for val_arr in merged_list:
            key = val_arr[key_idx]
            scnd_key = ""
            for i in scnd_key_arr:
                tmp_val = val_arr[i] + deli_ch
                scnd_key += tmp_val

            if key in result_dict:
                if scnd_key in result_dict[key]:
                    result_dict[key][scnd_key] += int(val_arr[val_idx])
                else:
                    result_dict[key].update({scnd_key: int(val_arr[val_idx])})
            else:
                result_dict.update({key: {scnd_key: int(val_arr[val_idx])}})

        return result_dict

    def recount_total_proportion_merged_dict_by_dictkey(self, motif_err_dict, deli_ch):
        result_list = []
        for key, val_dict in motif_err_dict.items():
            tot = 0
            for cnt in val_dict.values():
                tot += int(cnt)

            for scnd_key, cnt_val in val_dict.items():
                tmp_arr = [key]
                seq_motif_sub_arr = scnd_key.split(deli_ch)
                #add Seq, Motif
                tmp_arr += seq_motif_sub_arr[:2]
                # cnt
                tmp_arr.append(cnt_val)
                # new total
                tmp_arr.append(tot)
                # new proportion
                if tot == 0:
                    tmp_arr.append(0.0)
                else:
                    tmp_arr.append(int(cnt_val) / tot)
                #add Substitution
                tmp_arr.append(seq_motif_sub_arr[2])
                result_list.append(tmp_arr)
        return result_list
