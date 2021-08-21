f = open('crime_scene.txt', 'r')

all_content = []
for line in f:
    all_content.append(line)

weight_limit = all_content[0].split()[0]
time_limit = all_content[0].split()[1]
number_of_evidences = all_content[1].split()[0]

evidence_ids = []
evidence_weights = []
evidence_times = []
evidence_values = []

for i in all_content[2:]:
    evidence_ids.append(i.split()[0])
    evidence_weights.append(i.split()[1])
    evidence_times.append(i.split()[2])
    evidence_values.append(i.split()[3])

evidences = [evidence_ids, evidence_weights, evidence_times, evidence_values]


def my_sort(my_lst):
    if len(my_lst) <= 1:
        return my_lst
    base = int(my_lst[0])
    i = 1
    j = len(my_lst) - 1
    while True:
        if j < i:
            break
        if int(my_lst[i]) <= base:
            i += 1
            continue
        elif int(my_lst[j]) >= base:
            j -= 1
            continue
        my_lst[i], my_lst[j] = my_lst[j], my_lst[i]
    my_lst[0], my_lst[j] = my_lst[j], my_lst[0]

    my_lst[0:j] = my_sort(my_lst[0:j])
    my_lst[j + 1:] = my_sort(my_lst[j + 1:])
    return my_lst


def write_file(my_tup, solu_file):
    solu_file.write(str(my_tup[0])+'\n')
    my_lst = my_sort(my_tup[1])
    for i in my_lst:
        solu_file.write(str(i)+' ')
    solu_file.close()


def best_timeless(w, k):
    if k == len(evidences[0]):
        return 0, []
    if w - int(evidences[1][k]) >= 0:
        col_val, col_lst = best_timeless(w - int(evidences[1][k]), k+1)
        col_val += int(evidences[3][k])
        col_lst.append(evidences[0][k])
    else:
        col_val = 0
        col_lst = []
    didnt_col_val, didnt_col_lst = best_timeless(w, k+1)

    if col_val > didnt_col_val:
        return col_val, col_lst
    return didnt_col_val, didnt_col_lst


def best_weightless(t, j):
    if j == len(evidences[0]):
        return 0, []
    if t - int(evidences[2][j]) >= 0:
        coll_val, coll_lst = best_weightless(t - int(evidences[2][j]), j+1)
        coll_val += int(evidences[3][j])
        coll_lst.append(evidences[0][j])
    else:
        coll_val = 0
        coll_lst = []
    didnt_coll_val, didnt_coll_lst = best_weightless(t, j+1)
    if coll_val > didnt_coll_val:
        return coll_val, coll_lst
    return didnt_coll_val, didnt_coll_lst


def best(time, weight, m):
    if m == len(evidences[0]):
        return 0, []
    if (time - int(evidences[2][m]) >= 0) and (weight - int(evidences[1][m]) >= 0):
        col_value, col_list = best(time - int(evidences[2][m]), weight - int(evidences[1][m]), m+1)
        col_value += int(evidences[3][m])
        col_list.append(evidences[0][m])
    else:
        col_value = 0
        col_list = []
    not_col_value, not_col_list = best(time, weight, m+1)

    if col_value > not_col_value:
        return col_value, col_list
    return not_col_value, not_col_list


f1 = open('solution_part1.txt', 'w')
write_file(best_timeless(int(weight_limit), 0), f1)

f2 = open('solution_part2.txt', 'w')
write_file(best_weightless(int(time_limit), 0), f2)

f3 = open('solution_part3.txt', 'w')
write_file(best(int(time_limit), int(weight_limit), 0), f3)

f.close()