from controllers import display_inventory
from database import create_database, migrate_data


def main():
    create_database()
    migrate_data()
    display_inventory()
    

if __name__ == "__main__":
    main()