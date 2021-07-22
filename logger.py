def log(arg):
    with open(".\logs\logs.txt","a") as f:
        f.write(f"{arg}\n")