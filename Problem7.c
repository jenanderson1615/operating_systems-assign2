//Jen Anderson
//anderjen@oregonstate.edu
//CS311-400
//Homework2
//Problem7

#include <stdio.h>
#include <getopt.h>
#include <sys/utsname.h>
#include <time.h>
#include <sys/stat.h>
#include <unistd.h>

int main (int argc, char *argv[])
{
	int opt;
//	char c;
	struct utsname uname_pointer;
	time_t time_raw_format;
	struct stat s;

	opt = getopt (argc, argv, "htf:");
 	while (opt != -1)
 	{
    		switch (opt)
   		{
    			case 'h':
	               		uname(&uname_pointer);
				printf("Hostname = %s \n", uname_pointer.nodename);
				break;
			case 't':
				time(&time_raw_format);
				printf("The current local time: %s",
				ctime(&time_raw_format));
				break;
      			case 'f':
				if (stat(optarg, &s) == 0)
				{
					printf("size of file '%s' is %d bytes\n", optarg, (int) s.st_size);
				}
				else
				{
					printf("file '%s' not found\n", optarg);
				}
               			break;
   		}
		opt = getopt (argc, argv, "htf:"); 
	 }
  	return 0;
}
