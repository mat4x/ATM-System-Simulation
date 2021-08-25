#include <iostream>
#include <fstream>

using namespace std;

int main(){

    ifstream file;
    file.open("Works.txt");
    string content;

    if (file.is_open()){
        while (!file.eof()){
            getline(file, content);
            cout << content << endl;
        }
    }

    file.close();

    return 0;
}
