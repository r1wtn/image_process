import numpy as np
import cv2
import os


class Transformer(object):
    def __init__(self, input_dir=None, output_dir=None, data=None, image_size=None):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.image_name = data.keys()
        self.data = data
        self.image_size = tuple(image_size)
        self.dist_vertices = np.asarray(
            [[0, 0], [image_size[0], 0], [image_size[0], image_size[1]], [0, image_size[1]]])
        # transformed images
        self.image_set = dict()

    def transform(self):
        for image_name in self.image_name:
            image_path = os.path.join(self.input_dir, image_name)
            image = cv2.imread(image_path)
            src_vertices = np.asarray(self.data[image_name])
            M = cv2.getPerspectiveTransform(
                src_vertices.astype(np.float32), self.dist_vertices.astype(np.float32))
            image = cv2.warpPerspective(
                image, M, self.image_size).astype(np.uint8)
            self.image_set.setdefault(image_name, image)

    def save_images(self):
        for image_name in self.image_name:
            out_name = image_name.split(".")[0] + "_out.jpg"
            out_path = os.path.join(self.output_dir, out_name)
            out_image = self.image_set[image_name]
            cv2.imwrite(out_path, out_image)
