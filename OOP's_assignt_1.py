"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element available in list
7 . Try to extract all the value element form dict available in list
"""

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)-s:%(message)s',
                    filename="assignt.log_info")


class assignt:

    def reverse(self, list):
        """
        Reverse Methond
        :param list: list
        :return: reverse the value
        """
        logging.info("list assignment1: %s" % list)
        try:
            list1 = list[::-1]
            logging.info("list assignment1: %s" % list1)
            return list1
        except Exception as e:
            logging.error("error: %s" % e)

    def extract_list(self, list1):
        """
        Extract number or string out from list
        :param list1: list
        :return: number or string
        """
        logging.info("list assignment1: %s" % list1)
        a = eval(
            input("Enter the number or string which want to extract from list: "))

        try:
            for i in list1:
                if i == a:
                    logging.info("Extracting from list: %s" % i)
                    return i
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == a:
                            logging.info("Extracting from list: %s", j)
                            return j
                if type(i) == dict:
                    for j in i.values():
                        if j == a:
                            logging.info("Extracting from list: %s", j)
                            return j
                    for j in i.keys():
                        if j == a:
                            logging.info("Extracting from list: %s", j)
                            return j
                    for i in list1:
                        if type(i) == dict:
                            for j in i.items():
                                for k in j:
                                    if type(k) == list or type(k) == tuple or type(k) == set:
                                        for x in k:
                                            if x == a:
                                                logging.info(
                                                    "Extracting from list: %s", x)
                                                return x
        except Exception as e:
            logging.error("Issue in for loop in extract_list method", e)

    def type_extract(self, name1, type1):
        """
        Extract the data type from variable
        :param name1: varibale name
        :param type1: type of variable
        :return: list or tupe or set or dict
        """
        logging.info("type_extract: %s", name1)

        for i in name1:
            if type(i) == type1:
                logging.info("Data Type %s, %s", type1, i)
                continue
            else:
                pass

    def dict_values(self, name1):
        """
        Extract the dictionary values
        :param name1: list(dictionary)
        :return: dict.values() from the list
        """
        try:
            for i in name1:
                try:
                    if type(i) == dict:
                        return logging.info("Dictonary values inside from list : --> %s", list(i.values()))
                except Exception as e:
                    logging.info("Issue in dict_values %", e)
        except Exception as e:
            logging.info("Issue in for loop in dict_values method", e)

    def dict_keys(self, name1):
        """
        Extract the dictionary keys
        :param name1: list(dictionary)
        :return: dict.keys() from the list
        """
        try:
            for i in name1:
                try:
                    if type(i) == dict:
                        return logging.info("Dictonary values inside from list : --> %s", list(i.keys()))
                except Exception as e:
                    logging.info("Issue in dict_keys %", e)
        except Exception as e:
            logging.info("Issue in for loop in dict_keys method", e)

    def dict_items(self, name1):
        """
        Extract the dictionary items
        :param name1: list(dictionary)
        :return: dict.items() from the list
        """
        try:
            for i in name1:
                try:
                    if type(i) == dict:
                        return logging.info("Dictonary values inside from list : --> %s", list(i.items()))
                except Exception as e:
                    logging.info("Issue in dict_items %", e)
        except Exception as e:
            logging.info("Issue in for loop in dict_items method", e)


l = [3, 4, 5, 6, 7,
     [23, 456, 67, 8, 78, 78],
     [345, 56, 87, 8, 98, 9],
     (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]


obj = assignt()
# obj.reverse(l)
# obj.extract_list(l)
# obj.type_extract(l, list)
# obj.dict_values(l)
# obj.dict_keys(l)
# obj.dict_items(l)
