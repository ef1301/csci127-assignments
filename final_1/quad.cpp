#include <iostream>
#include <math.h>

int discriminant(int a, int b, int c){
  int result;
  result = (b*b) - 4*(a*c);
  return result;
}

double quadsolve(int a, int b, int c){
  double d;
  d = discriminant(a,b,c);
  if(d>=0){
    return (-b+sqrt(d))/(2*a);
  }
  else{
    return 0;
  }
}

int main(){
  std::cout << "Your discriminant is " <<  discriminant(1,2,3) << std::endl;
  std::cout << "Your discriminant is " << discriminant(6,10,-1) << std::endl;
  std::cout << "Your discriminant is " << discriminant(1,6,-14) << std::endl;
  std::cout << "Your discriminant is " << discriminant(8,14,-15) << std::endl;
  std::cout << quadsolve(1,2,3) << std::endl;
  std::cout << quadsolve(6,10,-1) << std::endl;
  std::cout << quadsolve(1,6,-14) << std::endl;
  std::cout << quadsolve(8,14,-15) << std::endl;
  return 0;
}


