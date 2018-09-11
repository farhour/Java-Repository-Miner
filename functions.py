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
