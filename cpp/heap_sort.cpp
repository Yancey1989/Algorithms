#include<iostream>
#include<algorithm>
using namespace std;
void HeapAdjust(int *a, int i, int size) {
	int l_child = i*2;
	int r_child = i*2+1;
	//叶子节点不做调整
	if (i <= size/2) {
		int min_index = i;
		if (l_child <= size && a[l_child] > a[min_index]) {
			min_index = l_child;
		}
		if (r_child <= size && a[r_child] > a[min_index]) {
			min_index = r_child;
		}
		// 如果需要调整
		if (min_index != i) {
			swap(a[i], a[min_index]);
			HeapAdjust(a, min_index, size);
		}
	}
}
void HeapSort(int *a, int size) {
	//建堆
	for(int i=size/2; i>=1; --i) {
		HeapAdjust(a, i, size);
	}
	for(int i=size; i>1; --i) {
		swap(a[1], a[i]);
		HeapAdjust(a, 1, i-1);
	}
}
int main(int argc, char** argv){
	int a[]={0,16,20,3,11,17,8};
	int size = sizeof(a) / sizeof(int);
	cout << size <<endl;
	HeapSort(a, size);
	for (int i=0; i<size; ++i) {
		cout << a[i] << " ";
	}
	cout << endl;
	return 0;
}
