def hello():
    print("Hello, World!")

def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
    try:
        print("Press Ctrl+C to exit...")
        while True:
            pass
    except KeyboardInterrupt:
        print("\nGoodbye!")
    