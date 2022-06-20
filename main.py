#!usr/bin/python3
if __name__ == __main__:
    def safe_print_list(my_list=[], x=0):
        a = 0
        for x in range(0, 10):
            try:
                return my_list[a:x]
            except (IndexError):
                return my_list