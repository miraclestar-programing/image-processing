#include<stdio.h>
#include<stdlib.h>

int main(void){
    FILE *fp;
    char filename1[20];
    char filename2[20];
    printf("MAXプーリング処理したいファイルを選択してください：");
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
    int a,b=0;

    //分割する大きさ table_h:縦の大きさ table_w:横の大きさ
    int table_h=5;
    int table_w=5;

    int max[3];

    unsigned char table[3][5][5];

    for(j=0;j<height;j=j+table_h){
        for(h=0;h<width;h=h+table_w){
            for(a=0;a<table_h;a++){
                for(b=0;b<table_w;b++){
                    for(i=2;i>=0;i--){
                        table[i][a][b]=(int)imgin[i][h+a][j+b];
                    }
                    for(i=2;i>=0;i--){
                        if(a==0 && b==0){
                            max[i]=table[i][a][b];
                        }
                        else if(table[i][a][b]>max[i]){
                            max[i]=table[i][a][b];
                        }
                    }
                }
            }
            for(a=0;a<table_h;a++){
                for(b=0;b<table_w;b++){
                    for(i=2;i>=0;i--){
                        imgout[i][h+a][j+b]=(unsigned char)max[i];
                    }
                }
            }
            for(i=2;i>=0;i--){
                max[i]=0;
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
