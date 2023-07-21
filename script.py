import datetime
from typing import List, Dict


class SocialMediaScheduler:
    def __init__(self):
        self.posts: List[str] = []
        self.schedules: Dict[str, str] = {}

    def add_post(self, post: str) -> None:
        self.posts.append(post)

    def add_schedule(self, platform: str, schedule: str) -> None:
        self.schedules[platform] = schedule

    def schedule_posts(self) -> None:
        for platform, schedule in self.schedules.items():
            if schedule:
                self._schedule_post(platform, schedule)

    @staticmethod
    def _schedule_post(platform: str, schedule: str) -> None:
        print(f'Scheduled post "{platform}" for {schedule}')


def main():
    try:
        scheduler = SocialMediaScheduler()
        scheduler.add_post("Hello, world!")
        scheduler.add_post("Hello, world2!")
        scheduler.add_schedule("Twitter", "every 1 day")
        scheduler.add_schedule("Facebook", "every 2 days")
        scheduler.schedule_posts()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()