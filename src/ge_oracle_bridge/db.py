"""Oracle ATP connection helper. No SQL runs when this module is imported."""

import oracledb

from .config import OracleConfig


def connect(config: OracleConfig | None = None):
    """Open an Oracle connection using locally configured credentials."""
    cfg = config or OracleConfig.from_environment()
    kwargs = {
        "user": cfg.user,
        "password": cfg.password,
        "dsn": cfg.dsn,
    }
    if cfg.config_dir:
        kwargs["config_dir"] = cfg.config_dir
    if cfg.wallet_password:
        kwargs["wallet_password"] = cfg.wallet_password
    return oracledb.connect(**kwargs)
