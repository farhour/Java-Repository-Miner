def remove_duplicate_commits(list_of_changes):
    d = dict()
    for change in list_of_changes:
        old_hash = change[0]
        old_path = change[1]
        new_hash = change[2]
        new_path = change[3]
        if old_hash not in d:
            d[old_hash] = [old_path]
        else:
            if old_path not in d[old_hash]:
                d[old_hash].append(old_path)
        if new_hash not in d:
            d[new_hash] = [new_path]
        else:
            if new_path not in d[new_hash]:
                d[new_hash].append(new_path)
    return d


def dictionary_of_spoon_output(spoon_output):
    final_dict = dict()
    for line in spoon_output:
        hash_of_commit = line[0]
        path_of_file = line[1]
        if hash_of_commit not in final_dict:
            final_dict[hash_of_commit] = {path_of_file: {}}
        else:
            final_dict[hash_of_commit][path_of_file] = {}
        count = len(line)-3
        methods_of_file = dict()
        for index in range(count):
            index_of_parentheses = line[index+2].find('(')
            method_name = line[index+2][:index_of_parentheses]
            method_arguments = line[index+2][index_of_parentheses:]
            methods_of_file[method_name] = method_arguments
        final_dict[hash_of_commit][path_of_file] = methods_of_file
    return final_dict
