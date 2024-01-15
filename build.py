import os

def get_data_files():
    data_files = []

    base_path = os.path.dirname(__file__)

    # Collect data files for audio directory
    audio_path = os.path.join(base_path, "audio")
    if os.path.exists(audio_path):
        audio_files = [(os.path.join("audio", file), "audio") for file in os.listdir(audio_path)]
        data_files.extend(audio_files)
    else:
        print(f"Warning: Audio directory not found at {audio_path}")

    # Collect data files for code directory
    code_files = [(file, "code") for file in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, file))]
    data_files.extend(code_files)

    # Collect data files for graphics directory
    graphics_path = os.path.join(base_path, "graphics")
    if os.path.exists(graphics_path):
        graphics_files = [(os.path.join("graphics", file), "graphics") for file in os.listdir(graphics_path)]
        data_files.extend(graphics_files)
    else:
        print(f"Warning: Graphics directory not found at {graphics_path}")

    # Collect data files for map directory
    map_path = os.path.join(base_path, "map")
    if os.path.exists(map_path):
        map_files = [(os.path.join("map", file), "map") for file in os.listdir(map_path)]
        data_files.extend(map_files)
    else:
        print(f"Warning: Map directory not found at {map_path}")

    return data_files

if __name__ == "__main__":
    print(get_data_files())
