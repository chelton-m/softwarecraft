from typing import List
import time


class RealWorldExamples:

    def remove_duplicates_inplace(self, nums: List[int]) -> int:
        """The core algorithm we learned"""
        if not nums:
            return 0

        unique_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_count] = nums[i]
                unique_count += 1
        return unique_count

    def example_1_user_analytics(self):
        """Example 1: User Analytics - Remove duplicate user visits"""
        print("=== EXAMPLE 1: USER ANALYTICS ===")
        print("Scenario: You have sorted user IDs who visited your website.")
        print("Need to count unique visitors (memory-efficient).\n")

        # Sorted user IDs with duplicates (from log files)
        user_visits = [1001, 1001, 1001, 1002, 1002, 1003, 1004, 1004, 1005]
        original_size = len(user_visits)

        print(f"Original visits: {user_visits}")
        print(f"Total records: {original_size}")

        unique_visitors = self.remove_duplicates_inplace(user_visits)

        print(f"After deduplication: {user_visits}")
        print(f"Unique visitors: {unique_visitors}")
        print(f"Unique visitor IDs: {user_visits[:unique_visitors]}")
        print(f"Memory saved: {original_size - unique_visitors} records\n")

    def example_2_financial_data(self):
        """Example 2: Financial Data Processing"""
        print("=== EXAMPLE 2: FINANCIAL DATA ===")
        print("Scenario: Stock prices with duplicate timestamps.")
        print("Need unique price points for technical analysis.\n")

        # Stock prices (sorted by timestamp, but some duplicates)
        stock_prices = [100, 100, 101, 101, 101, 102, 103, 103, 105]

        print(f"Raw price data: {stock_prices}")
        print("Problem: Duplicate prices skew moving averages!")

        unique_prices = self.remove_duplicates_inplace(stock_prices)

        print(f"Clean price data: {stock_prices[:unique_prices]}")
        print(f"Removed {len(stock_prices) - unique_prices} duplicate entries")
        print("Now can calculate accurate technical indicators!\n")

    def example_3_database_optimization(self):
        """Example 3: Database Result Optimization"""
        print("=== EXAMPLE 3: DATABASE OPTIMIZATION ===")
        print("Scenario: SQL query returned sorted results with duplicates.")
        print("Remove duplicates in-place to save memory.\n")

        # Simulated database query result (sorted customer IDs)
        customer_ids = [501, 501, 502, 502, 502, 503, 504, 504, 505, 506, 506]
        memory_before = len(customer_ids) * 4  # 4 bytes per int

        print(f"Query result: {customer_ids}")
        print(f"Memory usage: {memory_before} bytes")

        unique_customers = self.remove_duplicates_inplace(customer_ids)
        memory_after = unique_customers * 4

        print(f"After deduplication: {customer_ids[:unique_customers]}")
        print(f"Memory usage: {memory_after} bytes")
        print(f"Memory saved: {memory_before - memory_after} bytes ({(memory_before-memory_after)/memory_before*100:.1f}%)\n")

    def example_4_iot_sensor_data(self):
        """Example 4: IoT Sensor Data"""
        print("=== EXAMPLE 4: IoT SENSOR DATA ===")
        print("Scenario: Temperature sensor sends duplicate readings.")
        print("Remove duplicates to reduce storage and bandwidth.\n")

        # Temperature readings (sorted by timestamp)
        temperatures = [20, 20, 20, 21, 21, 22, 22, 22, 23, 23]

        print(f"Raw sensor data: {temperatures}")
        print("Problem: Storing every duplicate wastes space!")

        unique_readings = self.remove_duplicates_inplace(temperatures)

        print(f"Optimized data: {temperatures[:unique_readings]}")
        print(f"Data compression: {len(temperatures)} → {unique_readings} readings")
        print(f"Storage saved: {(len(temperatures) - unique_readings) / len(temperatures) * 100:.1f}%\n")

    def example_5_log_processing(self):
        """Example 5: Log File Processing"""
        print("=== EXAMPLE 5: LOG FILE PROCESSING ===")
        print("Scenario: Server logs with duplicate error codes (sorted).")
        print("Need unique error types for incident analysis.\n")

        # Error codes from logs (sorted chronologically)
        error_codes = [404, 404, 404, 500, 500, 502, 503, 503, 504]

        print(f"Error log: {error_codes}")
        print("Need: Unique error types for dashboard")

        unique_errors = self.remove_duplicates_inplace(error_codes)

        print(f"Unique error types: {error_codes[:unique_errors]}")
        print(f"Dashboard shows {unique_errors} different error types")
        print("Simplified incident response!\n")

    def performance_comparison(self):
        """Show why in-place is better than creating new arrays"""
        print("=== PERFORMANCE COMPARISON ===")
        print("Large dataset: 1 million sorted integers with duplicates\n")

        # Create large test data
        large_data = []
        for i in range(100000):
            large_data.extend([i] * 10)  # Each number appears 10 times

        print(f"Dataset size: {len(large_data):,} elements")
        print(f"Memory usage: ~{len(large_data) * 4 / 1024 / 1024:.1f} MB")

        # Method 1: In-place (our algorithm)
        data_copy1 = large_data.copy()
        start_time = time.time()
        unique_count = self.remove_duplicates_inplace(data_copy1)
        in_place_time = time.time() - start_time

        # Method 2: Using set (creates new data structure)
        start_time = time.time()
        set_time = time.time() - start_time

        print("\nResults:")
        print(f"In-place method: {in_place_time:.4f} seconds")
        print(f"Set method: {set_time:.4f} seconds")
        print(f"Unique elements: {unique_count:,}")
        print("Memory efficiency: In-place uses same array, set creates new one!")


def main():
    examples = RealWorldExamples()

    examples.example_1_user_analytics()
    examples.example_2_financial_data()
    examples.example_3_database_optimization()
    examples.example_4_iot_sensor_data()
    examples.example_5_log_processing()
    examples.performance_comparison()


if __name__ == "__main__":
    main()
