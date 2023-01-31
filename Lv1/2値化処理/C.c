#include<stdoi.h>
#include<stdlib.h>

int main(void){
    FILE *fp;
    char filename1[20];
    char filename2[20];
    printf("２値化したいファイルを選択してください：");
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

    for(i=0;i&lt;54;i++){
        header[i]=fgetc(fp);
    }


    int width=header[21]*16777216+header[20]*65536+header[19]*256+header[18];
    int height=header[25]*16777216+header[24]*65536+header[23]*256+header[22];

    printf("ファイルをオープンしました.\n\n");
    for(j=0;j&lt;height;j++){
        for(h=0;h&lt;width;h++){
            for(i=2;i&gt;=0;i--){
                imgin[i][h][j]=fgetc(fp);
            }
        }
    }
    fclose(fp);

    int border;
    printf("閾値を入力してください（0~255）：");
    scanf("%d",&amp;border);

    if(border&gt;255 || border&lt;0){
        printf("0~255の値を入力してください\n");
    }

    unsigned char gray[512][512];
    for(j=0;j&lt;height;j++){
        for(h=0;h&lt;width;h++){
            gray[h][j]=(imgin[0][h][j]+imgin[1][h][j]+imgin[2][h][j])/3;
            if(gray[h][j]&gt;border){
                gray[h][j]=255;
            }
            else{
                gray[h][j]=0;
            }
            imgout[0][h][j]=gray[h][j];
            imgout[1][h][j]=gray[h][j];
            imgout[2][h][j]=gray[h][j];
        }
    }

    printf("出力ファイル名を入力して下さい:");
    scanf("%s",filename2);
    fp=fopen(filename2,"wb");
    printf("ファイルをオープンしました.\n");
    /*ヘッダ部のデータheaderを移す*/
    for(i=0;i&lt;54;i++){
        fputc(header[i],fp);
    }
    /*データ部のデータを移す*/
    for(j=0;j&lt;height;j++){
        for(h=0;h&lt;width;h++){
            for(i=2;i&gt;=0;i--){
                fputc(imgout[i][h][j],fp);
            }
        }
    }
    fclose(fp);
    printf("ファイルをクローズしました.\n");
    return 0;
}
