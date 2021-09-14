import yaml

if __name__ == '__main__':
    with open('./config.yaml') as f:
        config = yaml.safe_load(f)
    print(config)

    training_parameter = config['training_parameter']
    steps = training_parameter['decay_step']
    print(steps)
