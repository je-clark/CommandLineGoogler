import sys, dns.resolver


def main():
    help_text = '''
    This script takes in an ASCII-encoded text file with a list of
    hosts (one per line) and provides console output and text file
    output with all the A and AAAA records for each host.

    Proper usage:

    dnsresolve <text file relative path>

    Optional usage:

    dnsresolve --help (Displays this text)
    '''

    if "--help" in sys.argv:
        print(help_text)
        sys.exit()
    if not sys.argv[1].endswith(".txt"):
        print("Improper input file. Input must be .txt")  
        sys.exit() 

    myResolver = dns.resolver.Resolver()
    myResolver.nameservers = ['1.1.1.1']
    with open(sys.argv[1]) as input_file:
        queries = input_file.readlines()

    output_fn = sys.argv[1].replace(".txt", "_with_output.txt")
    output_file = open(output_fn, 'w')

    for query in queries:
        query = query.rstrip()
        output_file.write(query+"\n")
        print(query)
        answers = myResolver.query(query, "A")
        try:
            output_file.write("A records:"+"\n")
            print("A records:")
            for ip in answers:
                output_file.write(str(ip)+"\n")
                print(ip)
            answers = myResolver.query(query, 'AAAA')
            output_file.write("AAAA records:"+"\n")
            print("AAAA records:")
            for ip in answers:
                output_file.write(str(ip)+"\n")
                print(ip)
        except:
            pass
    
    output_file.close()


if __name__ == "__main__":
    main()