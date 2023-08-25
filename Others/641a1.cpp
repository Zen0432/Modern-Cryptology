#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

string replace(const string &s, const int &n, const string &f_table, const vector <pair <int, char> > &arr){
    string ans = s;
    vector <bool> check(n, 0);
    for(int i=0;i<26;i++){
        for(int j=0;j<n;j++){
            if(ans[j] == arr[25-i].second && !check[j]){
                check[j] = 1;
                ans[j] = f_table[i];
            }
            else if(ans[j] == arr[25-i].second-'A'+'a' && !check[j]){
                check[j] = 1;
                ans[j] = f_table[i]-'A'+'a';
            }
        }
    }
    return ans;
}

int main(){
    string s = "omkf pi hdn cmgef icphsck .H krg vphqkc c, fic mco kqgf ioqag eo qfcmckf oq ficpihdn cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg mfio kdck kha cokh kodjuck vn k fofvfo gqpojicmoqli opiyoa of kihsc nccqki oefc ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya flofigvffic xvgfck. Fio kokfice";
    int n = s.length();
    // pair <int, char> p = {0, ' '};
    vector <pair <int, char> > arr(26);

    for(int i=0;i<26;i++){
        arr[i]=make_pair(0, 'A' + i);
    }
    for(int i=0;i<n;i++){
        if(s[i]>='a' && s[i]<='z'){
            arr[s[i]-'a'].first++;
            arr[s[i]-'a'].second = 'A'+s[i]-'a';
        }
        if(s[i]>='A' && s[i]<='Z'){
            arr[s[i]-'A'].first++;
            arr[s[i]-'A'].second = s[i];
        }
    }
    sort(arr.begin(), arr.end());
    cout << "The frequencies of letters in decreasing order : " << endl;
    for(int i=25;i>-1;i--){
        cout << arr[i].second << " " << arr[i].first /* <<  " " << f_table[25-i]*/ << endl;
    }
    cout << endl;
    
    // TEMP IS THE STRING WHICH CONTAINS LETTERS FROM HIGHEST TO LOWEST FREQUENCY
    string temp = "CFKOIGMHQPVNDYEUALJXRSZWTB";
    string f_table = "ETSIHORANCUBMDFLGWPQYVZWTB";
    // FREQ. TABLE IS OBTAINED BY MULTIPLE ATTEMPTS TO FORM A MEANINGFUL MAPPING BETWEEN PLAIN TEXT SPACE AND CIPHER TEXT SPACE
    
    cout << "The string after substitution is : " << endl;
    cout << endl;
    cout << replace(s, n, f_table, arr) << endl;
    
    return 0;
}