from simple_checkout import run as run_simple_checkout
from complex_checkout import run as run_complex_checkout

def main () -> None:
    print("=" * 30)
    print("This is the simple checkout.\n")
    run_simple_checkout()
    print("=" * 30)
    print("This is the complex checkout.\n")
    run_complex_checkout()


if __name__ == "__main__":
    main()    