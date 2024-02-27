#define _GNU_SOURCE
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#define call(fun) errno = 0; fun; perror(#fun)
int main(int argc, char **argv) {
  uid_t ruid = -1, euid = -1, suid = -1;
  getresuid(&ruid, &euid, &suid);
  printf("> ruid=%d, euid=%d, suid=%d\n", ruid, euid, suid);
  
  call(seteuid(1000));
  getresuid(&ruid, &euid, &suid);
  printf("> ruid=%d, euid=%d, suid=%d\n", ruid, euid, suid);
  
  call(seteuid(0));
  getresuid(&ruid, &euid, &suid);
  printf("> ruid=%d, euid=%d, suid=%d\n", ruid, euid, suid);
  
  
  return 0;
}