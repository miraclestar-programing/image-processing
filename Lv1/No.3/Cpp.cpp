#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main(){
    char filename[30];
    cout<<"減色処理したい画像の名前を選択してください：";
    cin>>filename;
    if(!filename){
        cout<<"ファイルをオープンできませんでした。\n";
        return 1;
    }
    else{
        cout<<"ファイルをオープンしました。\n";
    }
    FILE *fp;
    fp=fopen(filename,"rb");
    unsigned char header[54];
    unsigned char imgin[3][256][256];
    unsigned char imgout[3][256][256];
    int i,h,j=0;

    int bit=header[28];  

    for(i=0;i<54;i++){
        header[i]=fgetc(fp);
    }

    int width=header[21]*16777216+header[20]*65536+header[19]*256+header[18];
    int height=header[25]*16777216+header[24]*65536+header[23]*256+header[22];

    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=2;i>=0;i--){
                imgin[i][h][j]=fgetc(fp);
            }
        }
    }

    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=0;i<2;i++){
                if(imgin[i][h][j]<64){
                    imgout[i][h][j]=32;
                }
                else if(imgin[i][h][j]>=64 && imgin[i][h][j]<128){
                    imgout[i][h][j]=96;
                }
                else if(imgin[i][h][j]>=128 && imgin[i][h][j]<192){
                    imgout[i][h][j]=160;
                }
                else{
                    imgout[i][h][j]=224;
                }
            }
        }
    }


    char filename2[30];
    cout<<"出力ファイル名を入力してください：";
    cin>>filename2;
    if(!filename2){
        cout<<"ファイルを開けませんでした。\n";
        return 3;
    }
    fp=fopen(filename2,"wb");
     for(i=0;i<54;i++){
        fputc(header[i],fp);
    }
    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=2;i>=0;i--){
                fputc(imgout[i][h][j],fp);
            }
        }
    }
    fclose(fp);
    cout<<"ファイルをクローズしました\n";
    return 0;
}
