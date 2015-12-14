#include <iostream.h>

void main()
{
   long m[21][21][2];
   int l;
   int n;
   cin >>n;
   for (l=1;l<=n;l++)
   {
     int i,j;
     int s,t;
     cin >>s>>t;
     for (i=1;i<=s;i++)
       for (j=1;j<=s;j++)
       {
	 m[i][j][0]=0;
	 m[i][j][1]=0;
       }
     int mm[21];
     for (i=1;i<=20;i++)
       mm[i]=i;
     for (i=1;i<=s;i++)
     {
       if (i==1)
       {
	 m[i][1][0]=1;
	 m[i][1][1]=1;
       }
       else
       {
	 int j,k;
	 for (j=1;j<=i;j++)
	   for (k=1;k<=i-1;k++)
	   {
	     if (k>=j) m[i][j][0]+=m[i-1][k][1];
	     else m[i][j][1]+=m[i-1][k][0];
	     if (m[i][j][0]>40000) m[i][j][0]=40000;
	     if (m[i][j][1]>40000) m[i][j][1]=40000;
	   }
       }
     }
     long g=0,h=0;
     int k;
     while (t-g>0)
     {
       h++;
       g+=m[s][h][0]+m[s][h][1];
     }
     g=g-m[s][h][0];
     if (t-g>0) k=0;
     else { g=g-m[s][h][1]; k=1; }
     t-=g;
     cout <<h<<' ';
     for (int ll=h;ll<=s;ll++) mm[ll]++;
     for (int lt=s-1;lt>=1;lt--)
     {
       if (k==1) k=0; else k=1;
       long g=0,h=0;
       while (t-g>0)
       {
	 h++;
	 g+=m[lt][h][k];
       }
       g-=m[lt][h][k];
       t-=g;
       cout <<mm[h]<<' ';
       for (int lll=h;lll<=s;lll++)
	   mm[lll]=mm[lll+1];
     }
   }
}