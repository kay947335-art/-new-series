import random

try:
    # --- YOUR WORD LIST ---
    words = ["python", "variable", "coding", "software", "rat"]

    def unscramble():
        print("--- Python Unscrambler ---")
        user_input = input("Enter the scrambled letters: ").lower()
        
        # Unscrambling logic
        matches = [w for w in words if sorted(w) == sorted(user_input)]
        
        if matches:
            print(f"Match found: {matches}")
        else:
            print("No matches found in the list.")

    # Run the function
    unscramble()

except Exception as e:
    # This part catches errors and stops the window from closing!
    print(f"\n!! SCRIPT CRASHED !!\nError details: {e}")

# This is the "Anchor" that keeps the window open
input("\n\nPress ENTER to close this window...")