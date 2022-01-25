#!/bin/env python3

import csv

def main():
    roles = []
    with open('nist_role.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            roles.append(row)
        
    with open('tksa.csv', mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0], rows[1]) for rows in reader)
    return (roles, mydict)


if __name__ == '__main__':
    titles = ["工作角色名称", "工作角色ID", "专业领域", "类别", "工作角色描述", "任务", "知识", "技能", "能力"]
    roles, dic = main()
    for row in roles:
        i = 0
        for itm in row:
            if i <= 4:
                print(titles[i] + ": " + itm)
            else:
                print(titles[i] + ": ")
                arr = itm.split(',')
                for item in arr:
                    print(dic[item])
            i += 1
        print("-------------------------------------------------------------------------------------------------------\n")