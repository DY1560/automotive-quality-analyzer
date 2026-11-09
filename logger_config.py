import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOG_DIR = PROJECT_ROOT / "outputs" / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "quality_analyzer.log"


logging.basicConfig(
    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("automotive_quality_analyzer")