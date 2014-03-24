#include<string.h>
#include<algorithm>
#include<utility>
using namespace std;

class String{
public:
	String():data_(new char[1]){
		*data_ = '\0';
	}
	String(const char*nstr):data_(new char[strlen(nstr)+1]) {
		strcpy(data_,nstr);
	}
	~String() {delete[] data_;}

	String & operator=(String s) {
		swap(s);
		return *this;
	}
	void swap(String& rhs) {
		std::swap(data_, rhs.data_);
	}
private:
	char *data_;
};
int main(int argc, char** argv) {
	String s1("Hello");
	String s2(s1);
	return 0;
}

