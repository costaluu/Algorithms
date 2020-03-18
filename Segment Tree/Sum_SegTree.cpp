#include<bits/stdc++.h>

using namespace std;

// Sum segment tree;

long long int *segtree, *arr, size;

void BuildTree(int pos, int start, int end){
    if(start == end) segtree[pos] = arr[start];
    else{
        int mid = start + (end - start)/2;
        BuildTree(2*pos + 1, start, mid);
        BuildTree(2*pos + 2, mid+1, end);
        segtree[pos] = segtree[2*pos+1] + segtree[2*pos + 2];
    }
}

long long int Query(int pos, int start, int end, int l, int r){
    if(r < start || l > end) return 0;
    else if(l <= start && r >= end) return segtree[pos];
    int mid = start + (end - start)/2;
    return Query(2*pos + 1, start, mid, l, r) + Query(2*pos + 2, mid+1, end, l, r);
}

void Update(int pos, int start, int end, int Q, int val){
    if(Q < start || Q > end) return;
    if(start == end && pos == (size - 1) + Q){
        segtree[pos] = val;
        arr[Q] = val;
    }
    else{
        int mid = start + (end - start)/2;
        Update(2*pos + 1, start, mid, Q, val);
        Update(2*pos + 2, mid + 1, end, Q, val);
        segtree[pos] = segtree[2*pos + 1] + segtree[2*pos + 2];
    }
}


int main(){
    cin >> size;
    arr = new long long int[size+1];
    segtree = new long long int[2*size + 1];
    for(int i = 0; i < size; i++) cin >> arr[i];
    BuildTree(0, 0, size-1);
    for(int i = 0; i < 2*size - 1; i++) cout << segtree[i] << ' ';
    return 0;
}