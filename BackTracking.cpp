#include <iostream>
#define N 5
using namespace std;

int matrix[N][N];

bool isSafe(int x, int y ){
    return x>=0 && y>=0 && x <= N-1 && y <= N-1;
}

int dfs(int x,int y, int cnt){
    // x,y la do dai cac buoc di tren truc Oxy
    // moi buoc di la hop le khi |x| + |y| = 3 => khi do o mot vi tri bat ky thi co 8 duong co the di chuyen
    int xMove[8] = {2, 1, -1, -2, -2, -1,  1,  2 };
    int yMove[8] = {1, 2,  2,  1, -1, -2, -2, -1};
    for (int i =0 ; i<8; i++){
        int nextX = x + xMove[i];
        int nextY = y + yMove[i];
        if(cnt == N*N){
            return 1;       //tim ra con duong khi diem dau bang kich thuoc ban co
        }
        if(isSafe(nextX,nextY)){
            if(matrix[nextX][nextY] == -1){    //neu diem do chua di toi se danh dau la -1
                matrix[nextX][nextY] = cnt + 1;
                if ((dfs(nextX,nextY,cnt+1) == 1)){     
                    return 1;
                }
                else{
                    matrix[nextX][nextY] = -1;
                }
                
            }
        }
    }
    return 0;       // tra ve 0 neu Ma di toi duong cut va danh dau diem di qua tu vi tri truoc la chua di qua
}

int main(int argc, const char * argv[]){
    std::cout << "The Knight's tour problem \n" ; 

    for(int i=0; i < N; i++){
        for(int j=0;j < N; j++){
            matrix[i][j] = -1;
        }
    }
    matrix[0][0] = 1;
    dfs(0,0,1);


    for (int i = 0;i < N; i++){
        for(int j=0; j < N; j++){
            cout << matrix[i][j] << "-";
        }
        cout << "\n" <<endl;
      }
    return 0;
}