#include <iostream>
#include <fstream>

using namespace std;

int main(){

    ifstream file;

    string f_name;
    cout << "File Name: ";   cin >> f_name;
    file.open(f_name);
    string content;

    if (file.is_open()){
        while (!file.eof()){
            getline(file, content);
            cout << content << endl;
        }
    }

    file.close();

    ofstream ofile;

    ofile.open("Output.txt");

    for (int i=0; i<5; i++){
        ofile << i << endl;
    }
    ofile.close();

    return 0;
}
