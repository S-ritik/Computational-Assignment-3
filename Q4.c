//g++ -o Q4 main.cpp -lfftw3
//Q4- To compute the FT of guassian function and plot the result
#include<stdlib.h>
#include<complex.h>
#include<fftw3.h>
#include<math.h>
int main()
{
int n=512;
double* in=fftw_malloc(sizeof(double)*512);
fftw_complex* out=fftw_malloc(sizeof(fftw_complex)*512);
for(int i=0;i<512;i++)
{
 in[i]=exp(-1*i*i);
}
fftw_plan plan_forward=fftw_plan_dft_r2c_1d(n,in,out,FFTW_ESTIMATE);
fftw_execute(plan_forward);
FILE *f;
f=fopen("Q4data.csv","w");
for(int i=0;i<512;i++)
{
fprintf(f,"%f",out[i]);
fputs("\n",f);
}
fclose(f);
return 0;
}
