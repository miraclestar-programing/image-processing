#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main(){
    char filename[30];
    cout<<"２値化したい画像の名前を選択してください：";
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
    unsigned char imgin[256][256][3];
    unsigned char imgout[256][256][3];
    int i,h,j=0;

    int bit=header[28];  

    for(i=0;i<54;i++){
        header[i]=fgetc(fp);
    }

    int width=header[21]*16777216+header[20]*65536+header[19]*256+header[18];
    int height=header[25]*16777216+header[24]*65536+header[23]*256+header[22];

    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=0;i<3;i++){
                imgin[h][j][i]=fgetc(fp);
            }
        }
    }

    int border;
    cout<<"しきい値を入力してください：";
    cin>>border;
    if(border<0 || border>255){
        cout<<"0~255の値を入力してください：\n";
        return 2;
    }
    unsigned char gray[256][256];

    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            gray[h][j]=(imgin[h][j][0]+imgin[h][j][1]+imgin[h][j][2])/3;
            if(gray[h][j]>border){
                gray[h][j]=255;
            }
            else{
                gray[h][j]=0;
            }
            imgout[h][j][0]=gray[h][j];
            imgout[h][j][1]=gray[h][j];
            imgout[h][j][2]=gray[h][j];
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
            for(i=0;i<3;i++){
                fputc(imgout[h][j][i],fp);
            }
        }
    }
    fclose(fp);
    cout<<"ファイルをクローズしました\n";
    return 0;
}
