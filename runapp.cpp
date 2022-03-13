#include <iostream>
int main()
{
  char yorn;
  std::cout << "instealled";
  std::cin >> yorn;
  cout << yorn;
  if(yorn == 'y') {
system("python3 __main__.py");
  };
  if(yorn == 'n') {
    system("bash install.sh");
  }
}
