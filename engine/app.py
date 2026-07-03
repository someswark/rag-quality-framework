from core.config_loader import ConfigLoader

config = ConfigLoader().get()

print("\nFramework Configuration\n")

print(config["framework"]["name"])

print(config["application"]["name"])

print(config["llm"]["model"])