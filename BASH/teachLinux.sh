#!/bin/bash

# Welcome message
echo "Welcome to the Linux Command-Line Game!"
echo "Let's test your skills in navigating the Linux command line."

# Function to display instructions
display_instructions() {
    echo "Instructions:"
    echo "1. You will be given a task to perform using the command line."
    echo "2. Use the appropriate Linux commands to complete the task."
    echo "3. Enter your command and press Enter to execute it."
    echo "4. If your command is correct, you will proceed to the next task."
    echo "5. If your command is incorrect, you will be given another chance."
    echo ""
}

# Function to display task and prompt for user input
display_task() {
    echo "Task: $1"
    echo "Enter your command:"
    read user_input
}

# Function to check if the user input matches the expected command
check_command() {
    expected_command=$1
    if [[ "$user_input" == "$expected_command" ]]; then
        echo "Correct!"
        return 0
    else
        echo "Incorrect. Try again."
        return 1
    fi
}

# Main game loop
display_instructions

# Task 1: Navigate to the home directory
display_task "Navigate to your home directory"
while true; do
    display_task "Navigate to your home directory"
    check_command "cd ~" && break
done

# Task 2: List files in the current directory
display_task "List files in the current directory"
while true; do
    display_task "List files in the current directory"
    check_command "ls" && break
done

# Task 3: Create a new directory named "game"
display_task "Create a new directory named 'game'"
while true; do
    display_task "Create a new directory named 'game'"
    check_command "mkdir game" && break
done

# Task 4: Navigate into the "game" directory
display_task "Navigate into the 'game' directory"
while true; do
    display_task "Navigate into the 'game' directory"
    check_command "cd game" && break
done

# Task 5: Create a new file named "instructions.txt"
display_task "Create a new file named 'instructions.txt'"
while true; do
    display_task "Create a new file named 'instructions.txt'"
    check_command "touch instructions.txt" && break
done

# End of game
echo "Congratulations! You've completed all tasks successfully."
echo "You're now a master of the Linux command line!"
