import random
from datetime import date, timedelta


class Student:
    def __init__(self, name: str):
        self.name = name
        self.presentation_count = 0

    def increment_count(self):
        self.presentation_count += 1

    def __repr__(self):
        return f"Student('{self.name}')"

    def __str__(self):
        return self.name


class PresentationSlot:
    """Represents a single Tuesday presentation session."""

    def __init__(self, week_number: int, date_str: str, presenters: list[Student]):
        self.week_number = week_number
        self.date_str = date_str
        self.presenters = presenters  # Always 3 students

    def display(self):
        print(f"  📅 Week {self.week_number} — Tuesday {self.date_str}")
        for i, student in enumerate(self.presenters, start=1):
            print(f"     {i}. {student.name}")
        print()


class Scheduler:
    """Handles scheduling logic — picks 3 random students per week."""

    PRESENTATIONS_PER_WEEK = 3

    def __init__(self, students: list[Student]):
        if len(students) < self.PRESENTATIONS_PER_WEEK:
            raise ValueError(
                f"Need at least {self.PRESENTATIONS_PER_WEEK} students to schedule."
            )
        self.students = students
        self.schedule: list[PresentationSlot] = []

    def _next_tuesday(self, from_date: date) -> date:
        """Returns the next Tuesday on or after a given date."""
        days_ahead = (1 - from_date.weekday()) % 7  # Tuesday = weekday 1
        if days_ahead == 0:
            days_ahead = 7
        return from_date + timedelta(days=days_ahead)

    def generate_schedule(self, weeks: int, start_date: date = None) -> list[PresentationSlot]:
        """
        Generates a fair, randomised schedule for `weeks` Tuesdays.
        Uses a rotating pool so everyone presents roughly equally before repeating.
        """
        if start_date is None:
            start_date = date.today()

        self.schedule.clear()

        # Reset counts
        for student in self.students:
            student.presentation_count = 0

        current_date = self._next_tuesday(start_date)
        pool = []  # Rotating pool for fairness

        for week in range(1, weeks + 1):
            # Refill pool when it runs low
            if len(pool) < self.PRESENTATIONS_PER_WEEK:
                refill = self.students.copy()
                random.shuffle(refill)
                pool.extend(refill)

            # Pick the next 3 from the pool (no duplicates in same week)
            chosen = []
            temp_pool = pool.copy()
            while len(chosen) < self.PRESENTATIONS_PER_WEEK and temp_pool:
                pick = temp_pool.pop(0)
                if pick not in chosen:
                    chosen.append(pick)
                    pool.remove(pick)

            # Update counts
            for student in chosen:
                student.increment_count()

            slot = PresentationSlot(
                week_number=week,
                date_str=current_date.strftime("%d %b %Y"),
                presenters=chosen,
            )
            self.schedule.append(slot)
            current_date += timedelta(weeks=1)

        return self.schedule

    def display_schedule(self):
        if not self.schedule:
            print("No schedule generated yet.")
            return
        print("\n" + "=" * 45)
        print("   📋  TUESDAY PRESENTATION SCHEDULE")
        print("=" * 45 + "\n")
        for slot in self.schedule:
            slot.display()

    def display_stats(self):
        if not self.schedule:
            print("No schedule generated yet.")
            return
        print("=" * 45)
        print("   📊  PRESENTATION COUNT PER STUDENT")
        print("=" * 45)
        sorted_students = sorted(
            self.students, key=lambda s: s.presentation_count, reverse=True
        )
        for student in sorted_students:
            bar = "█" * student.presentation_count
            print(f"  {student.name:<20} {student.presentation_count:>2}x  {bar}")
        print()


class PresentationApp:
    """Main application — ties everything together."""

    def __init__(self):
        self.scheduler = None

    def run(self):
        print("\n" + "=" * 45)
        print("   🎓  SCHOOL PRESENTATION SCHEDULER")
        print("=" * 45)

        # --- Input students ---
        students = self._input_students()
        self.scheduler = Scheduler(students)

        # --- Input weeks ---
        weeks = self._input_weeks()

        # --- Input start date ---
        start_date = self._input_start_date()

        # --- Generate & display ---
        self.scheduler.generate_schedule(weeks=weeks, start_date=start_date)
        self.scheduler.display_schedule()
        self.scheduler.display_stats()

        # --- Optional reshuffle ---
        while True:
            again = input("🔄  Regenerate with a new random order? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                self.scheduler.generate_schedule(weeks=weeks, start_date=start_date)
                self.scheduler.display_schedule()
                self.scheduler.display_stats()
            else:
                print("\n✅  Schedule saved. Good luck with the presentations!\n")
                break

    def _input_students(self) -> list[Student]:
        print("\nEnter student names one by one.")
        print("(Type 'done' when finished — minimum 3 students)\n")
        students = []
        while True:
            name = input(f"  Student {len(students) + 1}: ").strip()
            if name.lower() == "done":
                if len(students) < 3:
                    print("  ⚠️  Please enter at least 3 students first.")
                else:
                    break
            elif name:
                students.append(Student(name))
        return students

    def _input_weeks(self) -> int:
        while True:
            try:
                weeks = int(input("\nHow many weeks to schedule? (e.g. 10): ").strip())
                if weeks < 1:
                    print("  ⚠️  Please enter a positive number.")
                else:
                    return weeks
            except ValueError:
                print("  ⚠️  Please enter a valid number.")

    def _input_start_date(self) -> date:
        print("\nEnter the start date to find the first Tuesday from.")
        print("(Press Enter to use today's date)\n")
        while True:
            raw = input("  Start date (DD/MM/YYYY) or Enter: ").strip()
            if raw == "":
                return date.today()
            try:
                return date(
                    int(raw[6:10]),
                    int(raw[3:5]),
                    int(raw[0:2]),
                )
            except (ValueError, IndexError):
                print("  ⚠️  Invalid format. Use DD/MM/YYYY.")


# ── Entry point ──────────────────────────────────────────
if __name__ == "__main__":
    app = PresentationApp()
    app.run()