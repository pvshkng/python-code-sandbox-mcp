from importlib.metadata import packages_distributions

def list_packages():
    keys = list(packages_distributions().keys())
    formatted = [key.replace("\\", ".") for key in keys]
    return "Available packages: " + ", ".join(formatted)

if __name__ == "__main__":
    packages = list_packages()
    print(f"Packages: {packages}")
