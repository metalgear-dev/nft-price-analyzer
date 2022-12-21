import configparser
from postgres_handler import PostgresHandler


def main(configuration_file):
    config = configparser.RawConfigParser()
    config.read(configuration_file)

    psHandler = PostgresHandler(config)


if __name__ == "__main__":
    main("setting.ini")
