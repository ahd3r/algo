'''
Given two arrays of numbers in descending order, write a function that returns a single array sorted in the same order.

E.g.

array1: 4, 2, 1
array2: 7, 6, 5, 3

Result array should be: 7,6,5,4,3,2,1
'''
# O(n)
def sort_two_arrays(arr1, arr2): # [4, 2, 1], [7, 6, 5, 3]
    res = []
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) == 0:
            res += arr2
            break
        if len(arr2) == 0:
            res += arr1 #  [7,6,5,4,3,2,1]
            break
        if arr1[0] > arr2[0]:
            res += [arr1[0]] # [7,6,5,4]
            del arr1[0]
        else:
            res += [arr2[0]] # [7] # [7,6] # [7,6,5] # [7,6,5,4,3]
            del arr2[0]
    return res


'''
/root/k8s/config -> config.txt (1 day old)
/root/k8s/env -> env.txt (7 days old), boot.sh (100 days old)
/root/k8s/main -> empty
/root/k8s/bin -> empty
def clean_dir(dir, older_than_days=30): # dir = "/root/k8s"
  """
    Deletes files older than the given days, and removes empty directories - except the given directory.
 
    Symlinks are treated as regular files. Files that are in use will also be deleted.
 
    This should be run as root.
  """
'''
# get_paths(dir) -> list(str) # 1 level deep, paths == files or dirs
# is_file(path) -> bool
# get_days(file) -> int
# delete_file(path) -> void

def clean_dir(dir, older_than_days=30): # /root/k8s # /root/k8s/config # /root/k8s/env
    paths = get_paths(dir) # [/root/k8s/config,/root/k8s/env,/root/k8s/main, /root/k8s/bin] # [/root/k8s/config/config.txt]
    for p in paths:
        if is_file(p) == False:
            clean_dir(p, older_than_days)
            if len(get_path(p)) == 0:
                delete_file(p)
        else:
            if get_days(p) > older_than_days:
                delete_file(p)
