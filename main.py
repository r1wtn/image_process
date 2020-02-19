import argparse
import os
from default_config import get_default_config, transformer_init_kwargs, visualizer_init_kwargs
from core.transfomer import Transformer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config_file', type=str, help='path to config file')
    parser.add_argument('--opts', default=None, nargs=argparse.REMAINDER,
                        help='Modify config options using the command-line')
    args = parser.parse_args()

    cfg = get_default_config()
    if args.config_file:
        cfg.merge_from_file(args.config_file)
    if args.opts:
        cfg.merge_from_list(args.opts)

    transformer = Transformer(**transformer_init_kwargs(cfg))
    transformer.transform()
    if cfg.io.save:
        transformer.save_images()
