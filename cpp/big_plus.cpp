#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char * add(char *a, char*b) {
	int la = strlen(a);
	int lb = strlen(b);
	char result[la+lb+2];
	int p_r = 0;
	memset(result, 0, sizeof(result));
	int crease = 0;
	while (la-- && lb--) {
		int tmp = int(a[la] - '0' + b[lb] - '0') + crease;
		result[p_r] = (tmp % 10) + '0';
		crease = tmp / 10;
		p_r++;	
	}
	while (la>=0) {
		int tmp = crease + int(a[la] - '0');
		result[p_r] = (tmp%10) + '0';
		crease = tmp/ 10;
		p_r++;
		la--;
	}
	while (lb>=0) {
		int tmp = crease + int(b[lb] - '0');
		result[p_r] = (tmp%10) + '0';
		crease = tmp/ 10;
		p_r++;
		lb--;
	}
	if ( crease > 0 ){
		result[p_r] = crease + '0';
		p_r++;
	}
	result[p_r]='\0';
	for (int i=0; i<strlen(result)/2; ++i) {
		char tmp = result[strlen(result)-i-1];
		result[strlen(result)-i-1] = result[i];
		result[i] = tmp;
	}
	return result;
}
int main(int argc, char** argv) {
	char *a = "1234";
	char *b = "99";
	char *result = add(a,b);
	printf("%s+%s=%s\n",a,b,result);
	return 0;
}
