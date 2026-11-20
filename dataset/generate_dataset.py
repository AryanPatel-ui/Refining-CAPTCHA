
import numpy as np
import pandas as pd

# Reproducible results
np.random.seed(42)

TOTAL_RECORDS = 10000
HALF = TOTAL_RECORDS // 2

def generate_human_data(n):
    duration = np.random.uniform(10, 180, n)

    return pd.DataFrame({
        "mouse_movement_count": np.random.poisson(
            duration * 1.2
        ),
        "avg_mouse_speed": np.random.lognormal(
            np.log(180), 0.55, n
        ),
        "mouse_direction_changes": np.random.poisson(
            duration * 0.35
        ),
        "click_count": np.random.poisson(
            duration * 0.12
        ),
        "avg_click_interval": np.random.lognormal(
            np.log(850), 0.65, n
        ),
        "typing_speed": np.random.lognormal(
            np.log(180), 0.45, n
        ),
        "scroll_count": np.random.poisson(
            duration * 0.10
        ),
        "session_duration": duration,
        "request_frequency": np.random.lognormal(
            np.log(0.35), 0.55, n
        ),
        "label": 0
    })


def generate_bot_data(n):
    duration = np.random.uniform(2, 120, n)

    # Different bot behavior profiles
    profiles = np.random.choice(
        ["rapid", "paced", "simulated"],
        size=n,
        p=[0.45, 0.30, 0.25]
    )

    mouse_rate = np.select(
        [
            profiles == "rapid",
            profiles == "paced",
            profiles == "simulated"
        ],
        [0.02, 0.15, 0.9]
    )

    click_interval = np.select(
        [
            profiles == "rapid",
            profiles == "paced",
            profiles == "simulated"
        ],
        [100, 700, 450]
    )

    typing_interval = np.select(
        [
            profiles == "rapid",
            profiles == "paced",
            profiles == "simulated"
        ],
        [30, 160, 120]
    )

    request_rate = np.select(
        [
            profiles == "rapid",
            profiles == "paced",
            profiles == "simulated"
        ],
        [3.0, 0.5, 1.2]
    )

    return pd.DataFrame({
        "mouse_movement_count": np.random.poisson(
            duration * mouse_rate
        ),
        "avg_mouse_speed": np.random.lognormal(
            np.log(220), 0.65, n
        ),
        "mouse_direction_changes": np.random.poisson(
            duration * mouse_rate * 0.3
        ),
        "click_count": np.random.poisson(
            duration * 0.15
        ),
        "avg_click_interval": np.random.lognormal(
            np.log(click_interval), 0.6, n
        ),
        "typing_speed": np.random.lognormal(
            np.log(typing_interval), 0.55, n
        ),
        "scroll_count": np.random.poisson(
            duration * 0.06
        ),
        "session_duration": duration,
        "request_frequency": np.random.lognormal(
            np.log(request_rate), 0.65, n
        ),
        "label": 1
    })


# Generate both classes
human = generate_human_data(HALF)
bot = generate_bot_data(HALF)

# Combine and shuffle
dataset = pd.concat(
    [human, bot],
    ignore_index=True
)

dataset = dataset.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save dataset
dataset.to_csv(
    "captcha_dataset.csv",
    index=False
)

print("Dataset generated successfully!")
print("Dataset shape:", dataset.shape)
print("\nClass distribution:")
print(dataset["label"].value_counts())
print("\nFirst five records:")
print(dataset.head())

