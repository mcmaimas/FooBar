2.2
def solution(l):
    factor_list = [10000,100,1]
    version_dictionary = {}
    for version_number in l:
        value_list = version_number.split('.')
        value = 0
        for idx, val in enumerate(value_list):
            value = value + (int(val) * factor_list[idx])
            version_dictionary[version_number] = value
            sort_by_k_v = sorted(sorted(version_dictionary.items()), key=lambda x: x[1])
            sorted_version_list = []
            for version_tuple in sort_by_k_v:
                sorted_version_list.append(version_tuple[0]) 
            return sorted_version_list
