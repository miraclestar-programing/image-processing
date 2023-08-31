#include<stdio.h>
#include<stdlib.h>

int main(void){
    FILE *fp;
    char filename1[20];
    char filename2[20];
    printf("減色処理したいファイルを選択してください：");
    scanf("%s",filename1);

    if(filename1==NULL){
        printf("入力してください\n");
        exit(1);
    }

    unsigned char header[54];
    unsigned char imgin[3][512][512];
    unsigned char imgout[3][512][512];

    if(filename1==NULL){
        printf("ファイルをオープンできませんでした\n");
        exit(1);
    }

    int i=0,j=0,h=0;

    fp=fopen(filename1,"rb");

    for(i=0;i<54;i++){
        header[i]=fgetc(fp);
    }



    int width=header[21]*16777216+header[20]*65536+header[19]*256+header[18];
    int height=header[25]*16777216+header[24]*65536+header[23]*256+header[22];

    printf("ファイルをオープンしました.\n\n");
    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=2;i>=0;i--){
                imgin[i][h][j]=fgetc(fp);
            }
        }
    }
    fclose(fp);


//実行部分ここから

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

//実行部分ここまで

    printf("出力ファイル名を入力して下さい:");
    scanf("%s",filename2);
    fp=fopen(filename2,"wb");
    printf("ファイルをオープンしました.\n");
    /*ヘッダ部のデータheaderを移す*/
    for(i=0;i<54;i++){
        fputc(header[i],fp);
    }
    /*データ部のデータを移す*/
    for(j=0;j<height;j++){
        for(h=0;h<width;h++){
            for(i=2;i>=0;i--){
                fputc(imgout[i][h][j],fp);
            }
        }
    }
    fclose(fp);
    printf("ファイルをクローズしました.\n");
    return 0;
}
