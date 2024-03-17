#include<iostream>
#include<vector>

using namespace std;

// class Solution {
// public:
//     vector<int> spiralOrder(vector<vector<int> >& matrix) {
//         for(int i=0;i<matrix.size(); i++) {
//             for(int j=0;j<matrix[0].size(); j++) {
//                 cout << matrix[i][j] << " ";
//             }
//             cout << "\n";
//         }
//     }
//     // vector<int> result{1,2};
//     // return result;
// };

void vectorSol() {
    vector<vector<int> > A
    { 
        /* Element one with 2 values in it. */
        {1, 2, 3},  
        
        /* Element two with 3 values in it. */
        {4, 5, 6},  
        
         /* Element three with 4 values in it. */
        {7, 8, 9}  
    }; 

    int i = 0;
    int j = 0;
    int colTraveled = 1;
    int rowTraveled = 1;
    int count = 0;
    int rows = A.size();
    int cols = A[0].size();
    std::cout << rows << "\n";
    std::cout << cols << "\n";
    bool right = true;
    bool left = false;
    bool down = false;
    bool up = false;
    vector<int> result;
    int k = 0;
    int total = rows*cols;
    for(k=0;k<total;k++) {
        result.push_back(A[i][j]);
        if(right) {
            j++;
            colTraveled++;
            if(colTraveled>cols) {
                rows--;
                right = false;
                down = true;
                j--;
                i++;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(down) {
            i++;
            rowTraveled++;
            if(rowTraveled>rows) {
                cols--;
                down = false;
                left = true;
                i--;
                j--;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(left) {
            j--;
            colTraveled++;
            if(colTraveled>cols) {
                rows--;
                left = false;
                up = true;
                j++;
                i--;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(up) {
            i--;
            rowTraveled++;
            if(rowTraveled>rows) {
                cols--;
                up = false;
                right = true;
                i++;
                j++;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
    }

    for(i=0;i<total;i++) {
        // for(j=0;j<cols;j++) {
        std::cout << result[i] << " ";
        // }
    }
    std::cout << "\n";
}


int main() {

    vectorSol();

    // int matrix[][3] = {
    //     {1,2,3},
    //     {4,5,6},
    //     {7,8,9}
    // };

    int matrix[][3] = {
        {1,2},
        {3,4},
        {5,6}
    };

    int i = 0;
    int j = 0;
    int colTraveled = 1;
    int rowTraveled = 1;
    int count = 0;
    int rows = 3;
    int cols = 2;
    bool right = true;
    bool left = false;
    bool down = false;
    bool up = false;
    int result[6];
    int k = 0;
    for(k=0;k<6;k++) {
        result[k] = matrix[i][j];
        // cout << right << " " << down << " " << left << " " << up << "\n";
        // cout << i << " " << j << "\n";
        // cout << " => " << rowTraveled << ", " << colTraveled << "\n";
        // cout << "\n";
        //cout << k << "\n";
        if(right) {
            j++;
            colTraveled++;
            if(colTraveled>cols) {
                rows--;
                right = false;
                down = true;
                j--;
                i++;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(down) {
            i++;
            rowTraveled++;
            if(rowTraveled>rows) {
                cols--;
                down = false;
                left = true;
                i--;
                j--;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(left) {
            j--;
            colTraveled++;
            if(colTraveled>cols) {
                rows--;
                left = false;
                up = true;
                j++;
                i--;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
        if(up) {
            i--;
            rowTraveled++;
            if(rowTraveled>rows) {
                cols--;
                up = false;
                right = true;
                i++;
                j++;
                colTraveled = 1;
                rowTraveled = 1;
            }
            continue;
        }
    }

    // for(i=0;i<6;i++) {
    //     cout << result[i] << " ";
    // }
    // cout << "\n";
        
    return 0;
}

