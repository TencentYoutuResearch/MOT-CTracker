import os
import numpy as np
 
root_dir = 'train/'
result_csv = 'train_annots.csv'

fout = open(result_csv, 'w')

for data_name in os.listdir(root_dir):
	print(data_name)
	gt_path = os.path.join(root_dir, data_name, 'gt', 'gt.txt')
	# print(gt_path)
	data_raw = np.loadtxt(gt_path, delimiter=',', dtype='float', usecols=(0,1,2,3,4,5,6,7,8))

	data_sort = data_raw[np.lexsort(data_raw[:,::-1].T)]
	visible_raw = data_sort[:,8]
	# print(data_sort)
	# print(data_sort[-1, 0])
	img_num = data_sort[-1, 0]

	# print(data_sort.shape[0])
	box_num = data_sort.shape[0]

	person_box_num = np.sum(data_sort[:,6] == 1)
	# print(person_box_num)

	for i in range(box_num):
		c = int(data_sort[i, 6])
		v = visible_raw[i]
		if c == 1 and v > 0.1:
			img_index = int(data_sort[i, 0])
			img_name = data_name + '/img1/' + str(img_index).zfill(6) + '.jpg'
			print(root_dir + img_name + ', ' + str(int(data_sort[i, 1])) + ', ' + str(data_sort[i, 2]) + ', ' + str(data_sort[i, 3]) + ', ' + str(data_sort[i, 2] + data_sort[i, 4]) + ', ' + str(data_sort[i, 3] + data_sort[i, 5]) + ', person\n')
			fout.write(root_dir + img_name + ', ' + str(int(data_sort[i, 1])) + ', ' + str(data_sort[i, 2]) + ', ' + str(data_sort[i, 3]) + ', ' + str(data_sort[i, 2] + data_sort[i, 4]) + ', ' + str(data_sort[i, 3] + data_sort[i, 5]) + ', person\n')

fout.close()