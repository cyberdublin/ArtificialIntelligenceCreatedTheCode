#!/bin/bash

# Initialize score
score=0

# Function to display instructions
display_instructions() {
    clear
    echo "Welcome to the Cybersecurity Skills Game!"
    echo "Let's test your knowledge and skills in cybersecurity."
    echo ""
    echo "Instructions:"
    echo "1. You will be presented with various scenarios related to cybersecurity."
    echo "2. Use your knowledge and skills to solve the challenges and earn points."
    echo "3. Each correct answer will earn you points, while incorrect answers will deduct points."
    echo "4. You can use 'hint' for a hint for the current challenge (costs points)."
    echo "5. You can use 'skip' to skip the current challenge (costs points)."
    echo "6. Your goal is to earn as many points as possible."
    echo "7. Have fun and happy learning!"
    echo ""
    echo "Press Enter to start the game."
    read -r
}

# Function to display challenge and prompt for user input
display_challenge() {
    clear
    echo "Your Score: $score"
    echo ""
    echo "Challenge: $1"
    echo "Enter your answer:"
    read -r user_input
}

# Function to check if the user input matches the expected answer
check_answer() {
    expected_answer=$1
    if [[ "$user_input" == "$expected_answer" ]]; then
        echo "Correct! You earned $2 points."
        ((score+= $2))
        sleep 2
        return 0
    else
        echo "Incorrect. Try again or use 'hint' for a hint."
        sleep 2
        return 1
    fi
}

# Function to provide a hint for the current challenge
provide_hint() {
    echo "Hint: $1"
    ((score-= $2))
    sleep 2
}

# Function to skip the current challenge
skip_challenge() {
    echo "Challenge skipped. You lost $1 points."
    ((score-= $1))
    sleep 2
}

# Main game loop
display_instructions

# Challenge 1: Identify phishing email
display_challenge "Identify whether the following email is a phishing attempt:\n
From: security@bank.com\n
Subject: Urgent: Account Verification Required!\n
Dear Customer,\n
Your account has been compromised. Please click on the following link to verify your account details:\n
http://www.fakebank.com/verify-account\n
Thank you,\n
Bank Security Team"
while true; do
    display_challenge "Identify whether the following email is a phishing attempt:\n
From: security@bank.com\n
Subject: Urgent: Account Verification Required!\n
Dear Customer,\n
Your account has been compromised. Please click on the following link to verify your account details:\n
http://www.fakebank.com/verify-account\n
Thank you,\n
Bank Security Team"
    check_answer "No, it's a phishing attempt." 20 && break
done

# Challenge 2: Secure SSH configuration
display_challenge "You've just set up a new SSH server. What is the best practice for securing SSH access?"
while true; do
    display_challenge "You've just set up a new SSH server. What is the best practice for securing SSH access?"
    check_answer "Disable root login and use SSH keys for authentication." 30 && break
done

# Challenge 3: Identify SQL injection vulnerability
display_challenge "Identify whether the following code is vulnerable to SQL injection:\n
$query = \"SELECT * FROM users WHERE username = '$_POST[username]' AND password = '$_POST[password]'\";"
while true; do
    display_challenge "Identify whether the following code is vulnerable to SQL injection:\n
$query = \"SELECT * FROM users WHERE username = '$_POST[username]' AND password = '$_POST[password]'\";"
    check_answer "Yes, it's vulnerable to SQL injection." 40 && break
done

# Challenge 4: Implement firewall rule
display_challenge "You need to block incoming traffic on port 22 (SSH) using iptables. Write the command to add the firewall rule."
while true; do
    display_challenge "You need to block incoming traffic on port 22 (SSH) using iptables. Write the command to add the firewall rule."
    check_answer "iptables -A INPUT -p tcp --dport 22 -j DROP" 30 && break
done

# Challenge 5: Identify malware behavior
display_challenge "Identify the following behavior as indicative of malware infection or not: CPU usage spikes to 100% unexpectedly."
while true; do
    display_challenge "Identify the following behavior as indicative of malware infection or not: CPU usage spikes to 100% unexpectedly."
    check_answer "Yes, it could be a sign of malware infection." 20 && break
done

# End of game
clear
echo "Congratulations! You've completed all challenges successfully."
echo "Your final score is: $score"
echo "Well done!"
