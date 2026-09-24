import sys


def analyze_scores():
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    raw_data = sys.argv[1:]
    valid_scores = []

    for item in raw_data:
        try:
            score = int(item)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{item}'")

    if not valid_scores:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    count = len(valid_scores)
    total = sum(valid_scores)
    avg = total / count
    high = max(valid_scores)
    low = min(valid_scores)
    score_range = high - low

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {avg:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    analyze_scores()
