from src import test_double, test_sum
from src.config import config

def main():
    print(test_double(config.NUM_EPOCHS))

if __name__ == "__main__":
    main()