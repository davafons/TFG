# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

from typing import Optional

from dial_core.datasets import Dataset  # noqa: F401


class DatasetsGroup:
    def __init__(
        self,
        name: str,
        train: Optional["Dataset"] = None,
        test: Optional["Dataset"] = None,
        validation: Optional["Dataset"] = None,
    ):
        self.name = name

        self.train = train
        self.test = test
        self.validation = validation

    def to_dict(self):
        def extract_dataset_info(dataset):
            return (
                {"x_type": str(dataset.x_type), "y_type": str(dataset.y_type)}
                if dataset
                else {}
            )

        return {
            "dataset": {"name": self.name},
            "train": extract_dataset_info(self.train),
            "test": extract_dataset_info(self.test),
            "validation": extract_dataset_info(self.validation),
        }
