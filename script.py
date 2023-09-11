commit 1: Use specific exception catch in main()

```python
try:
    run_scheduler()
except SpecificException as e:
    print(f"An error occurred: {e}")
```

commit 2: Encapsulate execution logic in a separate function

```python


def run_scheduler():
    scheduler = SocialMediaScheduler()
    scheduler.add_post("Hello, world!")
    scheduler.add_post("Hello, world2!")
    scheduler.add_schedule("Twitter", "every 1 day")
    scheduler.add_schedule("Facebook", "every 2 days")
    scheduler.schedule_posts()


def main():
    try:
        run_scheduler()
    except SpecificException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

commit 3: Improve error handling inside SocialMediaScheduler class

```python


def add_schedule(self, platform: str, schedule: str) -> None:
    if not self._is_valid_platform(platform):
        raise ValueError(f"Invalid platform: {platform}")

    if not self._is_valid_schedule(schedule):
        raise ValueError(f"Invalid schedule: {schedule}")

    self.schedules[platform] = schedule


@staticmethod
def _is_valid_platform(platform: str) -> bool:
    # Add platform validation logic here
    return True


@staticmethod
def _is_valid_schedule(schedule: str) -> bool:
    # Add schedule validation logic here
    return True


```
