from yacs.config import CfgNode as CN
import os


def get_default_config():
    cfg = CN()

    # io
    cfg.io = CN()
    cfg.io.input_dir = "data/"
    cfg.io.output_dir = "output/"
    cfg.io.save = True

    # domain
    cfg.domain = CN()
    cfg.domain.image_list = [
        "example.jpg"
    ]
    cfg.domain.vertices_list = [
        [[12, 210], [373, 27], [955, 202], [678, 635]]
    ]

    # codomain
    cfg.codomain = CN()
    cfg.codomain.image_size = [420, 594]

    return cfg


def transformer_init_kwargs(cfg):
    data = dict()
    for image_name, vertices in zip(cfg.domain.image_list, cfg.domain.vertices_list):
        data.setdefault(image_name, vertices)
    return {
        "input_dir": cfg.io.input_dir,
        "output_dir": cfg.io.output_dir,
        "data": data,
        "image_size": cfg.codomain.image_size
    }
