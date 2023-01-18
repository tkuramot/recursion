#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <iterator>
#include <sstream>

using namespace std;

class PriorityQueue{
    public:
        static int left(int i){
            return 2 * i + 1;
        }
        static int right(int i){
            return 2 * i + 2;
        }
        static int parent(int i){
            return (i - 1) / 2;
        }
        static void maxHeapify(vector<int> &maxHeap, int heapEnd, int i){
            int l = left(i);
            int r = right(i);

            int biggest = i;
            if(l <= heapEnd && maxHeap.at(l) > maxHeap.at(biggest)) biggest = l;
            if(r <= heapEnd && maxHeap.at(r) > maxHeap.at(biggest)) biggest = r;

            if(biggest != i){
                swap(maxHeap.at(i), maxHeap.at(biggest));
                maxHeapify(maxHeap, heapEnd, biggest);
            }
        }
        static void buildMaxHeap(vector<int> &arr){
            int middle = parent(arr.size() - 1);

            for(int i = middle; i >= 0; i--){
                maxHeapify(arr, arr.size() - 1, i);
            }
        }
};

vector<int> heapsort(vector<int> intArr){
    // 関数を完成させてください
    PriorityQueue::buildMaxHeap(intArr);
    int heapEnd = intArr.size() - 1;
    while(heapEnd > 0){
        swap(intArr.at(0), intArr.at(heapEnd));
        heapEnd--;
        PriorityQueue::maxHeapify(intArr, heapEnd, 0);
    }
    return intArr;
}