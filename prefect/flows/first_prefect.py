from prefect import flow, task

@task
def say_hello(name):
    return f"Hello, {name}!"

@flow
def greet():
    result = say_hello("Rajesh Boss.")
    print(result)

if __name__ == "__main__":
    greet()
