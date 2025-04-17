import yaml

def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return (
        config.get("start_urls", []),
        config.get("patterns", []),
        config.get("semaphore_limit", 10)  # default to 10 if not set
    )