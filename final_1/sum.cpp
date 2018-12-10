#include <iostream>

int sumofsquares(int a, int b){
  int sum;
  while(a<b){
    sum = 0;
    for(a ; a<b+1 ; a = a+1){
      int square = a*a;
      sum = sum + square;
    }
    return sum;
  }
}

int main(){
  std::cout << sumofsquares(5,10) << std::endl;
  std::cout << sumofsquares(1,5) << std::endl;
  std::cout << sumofsquares(3,9) << std::endl;
  return 0;
}
