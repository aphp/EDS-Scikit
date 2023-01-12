import pandas as pd
from databricks import koalas as ks

from eds_scikit.utils.typing import DataFrame

from .cut import cut


class CustomImplem:
    """
    A collection of custom pandas and koalas methods.

    All public facing methods must be stateless and defined as classmethods.
    """

    @classmethod
    def cache(cls, obj: DataFrame, backend=None) -> None:
        """Run df.cache() for Koalas. No-op for pandas."""
        if backend is pd:
            return
        elif backend is ks:
            obj.spark.cache()
            return
        else:
            raise ValueError(f"Unknown backend {backend}")

    @classmethod
    def add_unique_id(
        cls,
        obj: DataFrame,
        col_name: str = "id",
        backend=None,
    ) -> DataFrame:
        """Add an ID column for koalas or pandas."""
        if backend is pd:
            obj[col_name] = range(obj.shape[0])
            return obj
        elif backend is ks:
            return obj.koalas.attach_id_column(id_type="distributed", column=col_name)
        else:
            raise ValueError(f"Unknown backend {backend}")

    @classmethod
    def cut(
        cls,
        x,
        bins,
        right: bool = True,
        labels=None,
        retbins: bool = False,
        precision: int = 3,
        include_lowest: bool = False,
        duplicates: str = "raise",
        ordered: bool = True,
        backend=None,  # unused because koalas only
    ):
        """koalas version of pd.cut

        Notes
        -----
        Simplified vendoring from:
        https://github.com/pandas-dev/pandas/blob/v1.5.2/pandas/core/reshape/tile.py#L50-L305
        """
        return cut(
            x,
            bins,
            right,
            labels,
            retbins,
            precision,
            include_lowest,
            duplicates,
            ordered,
        )
