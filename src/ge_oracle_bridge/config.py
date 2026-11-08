"""Load Oracle connection settings from local environment variables."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class OracleConfig:
    user: str
    password: str
    dsn: str
    config_dir: str | None = None
    wallet_password: str | None = None

    @classmethod
    def from_environment(cls) -> "OracleConfig":
        required = ("ORACLE_USER", "ORACLE_PASSWORD", "ORACLE_DSN")
        missing = [key for key in required if not os.getenv(key)]
        if missing:
            raise RuntimeError(
                "Missing required environment variables: "
                + ", ".join(missing)
                + ". Copy .env.example to .env and configure it locally."
            )
        return cls(
            user=os.environ["ORACLE_USER"],
            password=os.environ["ORACLE_PASSWORD"],
            dsn=os.environ["ORACLE_DSN"],
            config_dir=os.getenv("ORACLE_CONFIG_DIR") or None,
            wallet_password=os.getenv("ORACLE_WALLET_PASSWORD") or None,
        )
