def reverseWords( s: str) -> str:
        return " ".join(reversed(s.split()))
    

print(reverseWords("The sky is blue"))