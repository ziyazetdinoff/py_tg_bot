import bot_core as bot
import storage
import yaml


def yaml_parse():
    with open('credentials.yaml', 'r') as stream:
        loaded_data = yaml.safe_load(stream)
    return loaded_data


if __name__ == '__main__':
    data = yaml_parse()
    print(data)
    Store = storage.Store()
    bot.main(Store, data['TOKEN'])
