# python argparse and yaml example

example of argparse and yaml for config

#### argparse

- argparse_ex.py

```
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epoch', type=int, default=10)
    parser.add_argument('--data_root', type=str, default='D:\data\coco')
    parser.add_argument('--lr', type=float, default=1e-2)
    parser.add_argument('--batch_size', type=int, default=256)
    parser.add_argument('--momentum', type=float, default=0.9)
    parser.add_argument('--weight_decay', type=float, default=5e-4)
    opts = parser.parse_args()
    print(opts)

    epoch = opts.epoch
    print(epoch)
```

#### yaml

- config.yaml
```
training_parameter:
  decay_step :
    - 30
    - 60
    - 90
  epoch: 10
  data_root: 'D:\data\coco'
  lr: 1e-2
  batch_size: 256
  momentum: 0.9
  weight_decay: 5e-4

```

- yaml_ex.py
```
import yaml

if __name__ == '__main__':
    with open('./config.yaml') as f:
        config = yaml.safe_load(f)
    print(config)

    training_parameter = config['training_parameter']
    steps = training_parameter['decay_step']
    print(steps)

```