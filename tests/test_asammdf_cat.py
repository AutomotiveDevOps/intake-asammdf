import os

import intake

from .utils import df
from .utils import df2
from .utils import temp_db
from intake_asammdf.sql_cat import SQLCatalog

here = os.path.abspath(os.path.dirname(__file__))

# pytest imports this package last, so plugin is not auto-added
intake.registry["sql_cat"] = SQLCatalog


def test_cat(temp_db):
    table, table_nopk, uri = temp_db
    cat = SQLCatalog(uri)
    assert table in cat
    assert table_nopk in cat
    d2 = getattr(cat, table).read()
    assert df.equals(d2)
    d_noindex = getattr(cat, table_nopk).read()
    assert df2.equals(d_noindex)


def test_yaml_cat(temp_db):
    table, table_nopk, uri = temp_db
    os.environ["TEST_SQLITE_URI"] = uri  # used in catalog default
    cat = intake.Catalog(os.path.join(here, "cat.yaml"))
    assert "tables" in cat
    cat2 = cat.tables()
    assert isinstance(cat2, SQLCatalog)
    assert table in list(cat2)
    assert table_nopk in list(cat2)
    d2 = cat.tables.temp.read()
    assert df.equals(d2)
    d_noindex = getattr(cat.tables, table_nopk).read()
    assert df2.equals(d_noindex)
