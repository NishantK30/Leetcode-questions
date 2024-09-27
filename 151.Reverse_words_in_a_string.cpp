#include<string>
#include<stack>
#include<algorithm>

//best implementation
std::string reverseWords(std::string s) {
        
        reverse(s.begin(),s.end());

        int n=s.size();
        int left=0;
        int right=0;
        int i=0;

        while(i<n){

            while(i<n && s[i]==' ')i++;
            if(i==n)break; 

            while(i<n && s[i]!=' '){
                s[right++]=s[i++];
            }

            reverse(s.begin()+left,s.begin()+right);

            s[right++]=' ';
            left=right;
            i++;

        }
        s.resize(right-1);
        return s;
    }

//my implementation
std::string myreverseWords(std::string s) {
        std::stack<std::string> st;
        std::string word="",ans="";
        for(int i=0;i<s.length();i++){
            if(s[i]==' ' && word!=""){
                st.push(word);
                word="";
            }
            else if(s[i]==' ' && word=="")
                continue;
            else
                word+=s[i];
        }
        if(word!="") st.push(word);
        while(!st.empty()){
            ans+=st.top();
            st.pop();
            if(!st.empty())
                ans+=" ";
        }
        return ans;
    }