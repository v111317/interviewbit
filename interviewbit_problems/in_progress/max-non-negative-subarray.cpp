#include<iostream>
#include<vector>

using namespace std;

vector<int> vectorSol() {
    // vector<int> A { -1, -1, -1, -1, -1}; 
    vector<int> A { 0, 0, -1, 0}; 

    int i = 0;
    int sum = 0;
    int maxSum = 0;
    int start = 0;
    int startMax = -1;
    int endMax = -1;

    for(i=0;i<=A.size();i++) {
        if(i==A.size() || A[i] < 0) {
            
            if(sum>=maxSum) {
                maxSum=sum;
                startMax = start;
                endMax = i - 1;
                
            }
            start = i + 1;
            sum = 0;
        } else {
            if (A[i]>=0) {
                sum += A[i];
            }
        }
    }

    vector<int> result;
    cout << startMax << " " << endMax << "\n";
    if(startMax>=0) {
        for(i=startMax;i<=endMax;i++) {
            result.push_back(A[i]);
        }
    }
    return result;
}


int main() {
    vector<int> result;
    result = vectorSol();
    for(int i=0;i<result.size();i++) {
        cout << result[i] << " ";
    }
    cout << "\n";
    return 0;
}

