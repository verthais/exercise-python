from typing import List
import re

def find_top_ip_address(lines: List[str]) -> str:
    """ Given an Apache log file, return IP address(es) which accesses the site most often.

            Our log is in this format (Common Log Format). One entry per line and it starts with an IP address which accessed the site,
            followed by a whitespace.

            10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] "GET /a.gif HTTP/1.0" 200 234

            Log file entries are passed as a list.
    
                  one to three digits ending with dot
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  repeated three
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓  followed by tree digits
                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓   ▓▓▓▓▓▓▓▓▓▓  one time     """
    patter = re.compile('([0-9]{1,3}\.{1}){3}([0-9]{1,3}){1}')
    
    counts = {}
    freak_cout = 0
    freak_ip = ''
    
    for line in lines:
        result = patter.match(line)
        
        if result is None:
            continue

        ip = line[:result.end()]

        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1

        if freak_cout < counts[ip]:
            freak_cout = counts[ip]
            freak_ip = ip

    return freak_ip
    

def eq(exp, res):
    if exp == res:
        print("test passed")
        return True
    else:
        print(f"test failed: expected:{exp} result:{res}")
        return False

    
def do_tests_pass() -> None:
    """Returns True if the test passes. Otherwise returns False."""

    lines = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234"]

    lines2 = []

    lines3 = ["10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234",
             "10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234"]
    
    
    lines4 = ["??.??.??.??- frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234",
             "10.0.0.1 - frank [10/Dec/2000:12:34:56 -0500] \"GET /a.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - frank [10/Dec/2000:12:34:57 -0500] \"GET /b.gif HTTP/1.0\" 200 234",
             "10.0.0.2 - nancy [10/Dec/2000:12:34:58 -0500] \"GET /c.gif HTTP/1.0\" 200 234"]

    eq("10.0.0.2",find_top_ip_address(lines))
    eq("", find_top_ip_address(lines2))
    eq("10.0.0.1", find_top_ip_address(lines3))
    eq("10.0.0.2", find_top_ip_address(lines4))

if __name__ == "__main__":
    do_tests_pass()
