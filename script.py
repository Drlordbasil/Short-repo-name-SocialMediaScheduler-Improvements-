The code you have provided looks good overall. However, there are a few improvements that can be made:

1. Use a more specific Exception catch:
   In the `main` function, catch only the specific exception that the code might raise, rather than using a generic `Exception` catch-all. This way, you can handle specific errors and leave other unexpected errors uncaught.

   ```python
   except SpecificException as e:
       print(f"An error occurred: {e}")
   ```

2. Encapsulate the execution logic and error handling into a separate function:
   Move the code inside the `try-except` block in the `main` function to a new function, such as `run_scheduler()`. This way, you can separate the concerns of creating the scheduler and running it, making the code more modular.

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

3. Improve error handling inside the `SocialMediaScheduler` class:
   Currently, if an invalid platform or schedule is provided, the code does not handle it. You can add appropriate error handling inside the `add_schedule` method to raise an exception or handle it gracefully.

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

By implementing these improvements, you will have a more readable, modular, and robust codebase.