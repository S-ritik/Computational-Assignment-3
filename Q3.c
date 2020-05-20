//Q3 To compute FT using gsl library Note-This is based on example in gsl library
#include<stdio.h>
#include<math.h>
#include<gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])

int main (void)
{
  gsl_fft_complex_wavetable * wavetable;
  gsl_fft_complex_workspace * workspace;
  int i; double data[2*512];
 REAL(data,0) = 1; IMAG(data,0) = 0.0;
  for (i = 1; i < 512; i++)
    {
       REAL(data,i)=sin(i)/i; IMAG(data,i) = 0.0;
    }

  for (i = 0; i < 512; i++)
    {
      printf ("%d %e %e\n", i,
              REAL(data,i), IMAG(data,i));
    }
  printf ("\n\n");
wavetable = gsl_fft_complex_wavetable_alloc (512);
  workspace = gsl_fft_complex_workspace_alloc (512);
  int t=gsl_fft_complex_forward(data,1,512, wavetable, workspace);
      FILE *f;
      f=fopen("Q3data.csv","w");

  for (i = 0; i <512; i++)
    {
      fprintf(f,"%f",REAL(data,i));
      fputs("\n",f);
      printf ("%d %e %e\n", i,REAL(data,i),IMAG(data,i));
    }
  fclose(f);
  return 0;
}
