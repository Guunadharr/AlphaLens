from app.core.config import APP_NAME, APP_VERSION
from app.core.constants import LINE
from app.core.logger import logger


def main():

    print(LINE)
    print(f"🚀 {APP_NAME} v{APP_VERSION}")
    print("AI Investment Research Assistant")
    print(LINE)

    logger.info("Loading configuration...")
    logger.info("Configuration loaded.")

    logger.info("Starting AlphaLens...")
    logger.info("AlphaLens started successfully.")


if __name__ == "__main__":
    main()