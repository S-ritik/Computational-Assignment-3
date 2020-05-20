//Q2-To compute FT using FFTW library
#include<stdlib.h>
#include<complex.h>
#include<fftw3.h>
#include<math.h>
#include<stdio.h>
#include<string.h>
void main()
{
int n=512;
double* in=fftw_malloc(sizeof(double)*512);
fftw_complex* out=fftw_malloc(sizeof(fftw_complex)*512);
for(int i=0;i<512;i++)
{
 if(i==0)
  in[i]=1;
 else
  in[i]=sin(i)/i;
}
fftw_plan plan_forward=fftw_plan_dft_r2c_1d(n,in,out,FFTW_ESTIMATE);
fftw_execute(plan_forward);
FILE *f;
f=fopen("Q2data.csv","w");
for(int i=0;i<512;i++)
{
fprintf(f,"%f",&out[i]);
fputs("\n",f);
}
fftw_destroy_plan(plan_forward);
fclose(f);
}
