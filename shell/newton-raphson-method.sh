#!/bin/bash

# Formula: Xn+1 = Xn + C/Xn

# double X0 = 2;
# double C = 5;

# println("Formula: Xn+1 = Xn + C/Xn\n");
# println("X0: " + X0);
# for (int n = 1; n < 11; n++) {
#     double Xn = (X0 + (C /X0))/2;
#     if (Xn == X0) {
#         break;
#     } else {
#         println("X"+ n + ": " + round(Xn));
#         X0 = Xn;
#     }
# }

X0=2
C=5

echo "Formula: Xn+1 = Xn + C/Xn\n";
echo "X0: $X0";

for ((n=1;n<=10;n++))
do
   Xn=`expr $X0 + $C / $X0 / 2`
   if [ $Xn -eq $X0 ]
   then
      break;
   else
      echo "X$n: $Xn";
      $X0=$Xn;
   fi
done