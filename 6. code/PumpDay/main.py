'''
*** Example Defined Target:

1. Reading Target
Goal: Read 40 books/year (Average 200 pages/book)

Recommendation: Read 30 pages/day

Real Life Adjustment: Reading 10 pages/day currently

Adjusted Plan:

Effort: 1/3 of the target effort, achieving 1% of the goal each day

Impact on Schedule: Recalculate to 35 pages/day or adjust the timeline to 2 years to finish 40 books

2. Full Commit History in GitHub
Goal: 1 commit/day for a year

Recommendation:

Plan small, daily tasks or features to commit each day.

Use project management tools to break down tasks into daily commits.

3. Weight Loss
Goal: Lose weight

Daily Routine:

Run: 3 km/day

Workout: 30 minutes/day

Recommendation:

Track your runs and workouts using a fitness app to stay accountable.

Mix in different types of workouts to keep it interesting and prevent burnout.

4. Language Learning
Goal: Learn a new language

Recommendation:

Daily Practice: 20-30 minutes/day using apps like Duolingo or Babbel.

Supplement: Weekly sessions with a language tutor or language exchange partner.

5. Higher Scores
Goal: Improve scores in a specific subject

Recommendation:

Daily Study: Dedicate a specific amount of time each day to studying the subject.

Practice Tests: Regularly take practice tests to track progress and identify areas for improvement.

6. Watching Educational Videos
Goal: Gain knowledge through educational videos

Recommendation:

Daily Viewing: Watch 1 educational video/day (around 20-30 minutes).

Track Progress: Maintain a list of videos watched and notes on key learnings.

7. Journaling
Goal: Maintain a daily journal

Recommendation:

Daily Entry: Spend 10-15 minutes each day writing in your journal.

Topics: Reflect on daily experiences, goals, and thoughts to develop a habit.


Combine all activities (3) Recommend 3 main activities as it will affect 1 day if we dont finish it except working time, please finish at least 1 and maximum 3

To calculate progress and adjust targets dynamically based on actual performance, we'll use formulas for:

Daily Target Progress: How much of the daily goal was achieved.
Effort Impact on Total Target: How the real-life effort affects the total goal and the remaining time.
Adjusted Daily Target: A recalculated daily target to stay on track if the performance lags.

Features:
1. Calculate the targets change -> Prediction for many changes
2. 


First Time: Username, new target, following activities
Track history change
enter the target 


Next Time 
- Keep the session
- Target of the input should be calculate to number for easy calculation. Input the number of the activities change in a day

'''




# from datetime import date

# class PumpDay:
#     def __init__(self, progress, quote, activities):
#         self.activities = activities  # List of Activity objects
#         self.progress = progress      # Progress percentage
#         self.quote = quote            # Quote of the day

#     def cal_remaining_day(self, target_day):
#         """
#         Calculate remaining days from today to the target day.
#         Args:
#             target_day (date): The target date.
#         Returns:
#             int: Number of days remaining.
#         """
#         remaining_day = (target_day - date.today()).days
#         return remaining_day

#     def get_quote_per_day(self, link):
#         """
#         Retrieve or generate a quote for the day.
#         Args:
#             link (str): The source or placeholder link for quote retrieval.
#         """
#         # TODO: Implement quote fetching logic here
#         pass


# class Activity:
#     def __init__(self, name, times=0):
#         self.name = name  # Name of the activity
#         self.times = times  # Number of times the activity was completed

#     def cal_done_activities(self, total):
#         """
#         Calculate completed activities as a percentage.
#         Args:
#             total (int): Total planned activities.
#         Returns:
#             float: Percentage of completed activities.
#         """
#         return (self.times / total) * 100 if total > 0 else 0

#     def cal_undo_activities(self, total):
#         """
#         Calculate uncompleted activities as a percentage.
#         Args:
#             total (int): Total planned activities.
#         Returns:
#             float: Percentage of uncompleted activities.
#         """
#         return 100 - self.cal_done_activities(total) if total > 0 else 0

# # Define activities
# activity1 = Activity(name="Meditation", times=1)
# activity2 = Activity(name="Exercise", times=0)
# activity3 = Activity(name="Learning Python", times=2)

# # List of activities
# activities = [activity1, activity2, activity3]

# # Define a PumpDay object
# today_pump_day = PumpDay(
#     progress=50, 
#     quote="Stay positive, work hard, and make it happen.", 
#     activities=activities
# )

# # Example usage
# target_date = date(2024, 12, 31)
# remaining_days = today_pump_day.cal_remaining_day(target_date)
# print(f"Remaining days to target: {remaining_days}")

# # Calculate progress for an activity
# total_activities = len(activities)
# for activity in activities:
#     done_percentage = activity.cal_done_activities(total_activities)
#     undo_percentage = activity.cal_undo_activities(total_activities)
#     print(f"Activity '{activity.name}': Done {done_percentage:.2f}%, Undone {undo_percentage:.2f}%")

# from datetime import date

class ReadingTracker:
    def __init__(self, total_books, pages_per_book, daily_target):
        self.total_books = total_books
        self.pages_per_book = pages_per_book
        self.daily_target = daily_target
        self.total_target_pages = total_books * pages_per_book
        self.actual_pages_read = 0
        self.days_elapsed = 0

    def log_daily_reading(self, pages_read):
        """
        Logs the pages read in a day and updates progress.
        Args:
            pages_read (int): Pages read in a day.
        """
        self.actual_pages_read += pages_read
        self.days_elapsed += 1

    def calculate_progress(self):
        """
        Calculate progress and remaining days.
        Returns:
            dict: Progress, remaining pages, adjusted daily target, etc.
        """
        daily_progress = (self.actual_pages_read / (self.days_elapsed * self.daily_target)) * 100
        total_progress = (self.actual_pages_read / self.total_target_pages) * 100
        remaining_pages = self.total_target_pages - self.actual_pages_read

        if self.days_elapsed == 0:
            return {
                "daily_progress": 0,
                "total_progress": 0,
                "remaining_pages": remaining_pages,
                "adjusted_daily_target": self.daily_target,
                "remaining_days": None
            }

        remaining_days = (date(date.today().year + 1, 1, 1) - date.today()).days - self.days_elapsed
        adjusted_daily_target = remaining_pages / remaining_days if remaining_days > 0 else float("inf")

        return {
            "daily_progress": round(daily_progress, 2),
            "total_progress": round(total_progress, 2),
            "remaining_pages": remaining_pages,
            "adjusted_daily_target": round(adjusted_daily_target, 2),
            "remaining_days": remaining_days
        }

# # Example Usage
# tracker = ReadingTracker(total_books=40, pages_per_book=200, daily_target=30)

# # Log reading data
# tracker.log_daily_reading(10)  # Day 1: 10 pages read
# tracker.log_daily_reading(20)  # Day 2: 20 pages read

# # Calculate and display progress
# progress = tracker.calculate_progress()
# print(f"Daily Progress: {progress['daily_progress']}%")
# print(f"Total Progress: {progress['total_progress']}%")
# print(f"Remaining Pages: {progress['remaining_pages']}")
# print(f"Adjusted Daily Target: {progress['adjusted_daily_target']} pages/day")
# print(f"Remaining Days: {progress['remaining_days']}")
from datetime import date

# Base Activity class
class Activity:
    def __init__(self, name, target, completed=0):
        self.name = name
        self.target = target  # Overall target (e.g., total hours, total pages, etc.)
        self.completed = completed  # Progress completed so far
        self.days_elapsed = 0

    def log_progress(self, amount):
        """
        Logs progress (how much has been completed today).
        """
        self.completed += amount
        self.days_elapsed += 1

    def calculate_progress(self):
        """
        Calculates overall progress, remaining target, and adjusted daily target.
        Returns:
            dict: Total progress, remaining target, and adjusted daily target.
        """
        if self.target == 0:
            return {"total_progress": 0, "adjusted_daily_target": float("inf"), "remaining_days": None}
        
        total_progress = (self.completed / self.target) * 100
        remaining_target = max(0, self.target - self.completed)
        adjusted_daily_target = remaining_target / 1  # Assuming one day left

        remaining_days = (date(date.today().year + 1, 1, 1) - date.today()).days - self.days_elapsed
        
        if remaining_days > 0:
            adjusted_daily_target = remaining_target / remaining_days
        else:
            adjusted_daily_target = float("inf")

        return {
            "total_progress": round(total_progress, 2),
            "adjusted_daily_target": round(adjusted_daily_target, 2),
            "remaining_target": remaining_target,
            "remaining_days": remaining_days
        }


# Reading Tracker
class ReadingTracker(Activity):
    def __init__(self, total_books, pages_per_book, daily_target):
        total_target_pages = total_books * pages_per_book
        super().__init__(name="Reading Tracker", target=total_target_pages)
        self.daily_target = daily_target
        self.pages_per_book = pages_per_book
        self.total_books = total_books

    def log_progress(self, pages_read):
        super().log_progress(pages_read)

    def calculate_progress(self):
        return super().calculate_progress()


# Language Tracker
class LanguageTracker(Activity):
    def __init__(self, total_words, daily_target):
        total_target_words = total_words
        super().__init__(name="Language Tracker", target=total_target_words)
        self.daily_target = daily_target

    def log_progress(self, words_learned):
        super().log_progress(words_learned)

    def calculate_progress(self):
        return super().calculate_progress()


# Health Tracker (e.g., Weight Loss)
class HealthTracker(Activity):
    def __init__(self, target_weight_loss, daily_target_calories_burned):
        total_target_calories = target_weight_loss * 7700  # Assuming 7700 calories per kg of weight loss
        super().__init__(name="Health Tracker", target=total_target_calories)
        self.daily_target_calories_burned = daily_target_calories_burned

    def log_progress(self, calories_burned):
        super().log_progress(calories_burned)

    def calculate_progress(self):
        return super().calculate_progress()


# Example Usage

# Pump Day and Activities
today = date.today()
pump_day = PumpDay(date=today)

# Add Reading Activity
reading = ReadingTracker(total_books=40, pages_per_book=200, daily_target=30)
reading.log_progress(10)  # Day 1
reading.log_progress(20)  # Day 2
pump_day.add_activity(reading)

# Add Language Learning Activity
language = LanguageTracker(total_words=10000, daily_target=50)
language.log_progress(40)  # Day 1
language.log_progress(60)  # Day 2
pump_day.add_activity(language)

# Add Health (Weight Loss) Activity
health = HealthTracker(target_weight_loss=10, daily_target_calories_burned=500)
health.log_progress(300)  # Day 1
health.log_progress(400)  # Day 2
pump_day.add_activity(health)

# Generate and display summary
summary = pump_day.get_summary()
print(summary)
