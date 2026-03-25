import os

def environment_callback(request):
    """
    Returns environment name and color based on the ENV setting.
    Used by Unfold to show a badge in the admin header.
    """
    env = os.getenv("ENV", "dev")
    env_mapping = {
        "prod": ["Production", "danger"],
        "staging": ["Staging", "warning"],
        "dev": ["Development", "info"],
        "local": ["Local", "success"],
    }
    return env_mapping.get(env, ["Unknown", "info"])
