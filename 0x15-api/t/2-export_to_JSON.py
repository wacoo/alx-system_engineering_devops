#!/usr/bin/python3

""" show employee todo list progress and export to JSON """

if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import json

    idd = int(argv[1])
    emp_url = "https://jsonplaceholder.typicode.com/users/" + str(idd)
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    emp = urllib.request.urlopen(emp_url)
    todos = urllib.request.urlopen(todos_url)
    d_emp = json.loads(emp.read())
    d_todos = json.loads(todos.read())
    t_title = []
    t_count = 0
    t_owned = []
    det = []
    done_count = 0
    for td in d_todos:
        if td["userId"] == idd:
            if td["completed"]:
                done_count += 1
                t_title.append(td["title"])
            t_count += 1
            tsks = {"task": td["title"], "completed": td["completed"],
                    "username": d_emp["username"]}
            det.append(tsks)
    t_owned = {idd: det}
    print("Employee {} is done with tasks({}/{}):".format(d_emp["name"],
          done_count, t_count))
    for i in t_title:
        print("\t {}".format(i))

    with open("{}.json".format(idd), 'w') as f:
        json.dump(t_owned, f)
