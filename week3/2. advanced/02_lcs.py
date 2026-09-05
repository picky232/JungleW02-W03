"""
[동적 계획법 - 최장 공통 부분수열 (Longest Common Subsequence, LCS)]

▣ 문제 배경
- 두 문자열에서 동시에 등장하면서 "원래 순서를 유지" 하는 가장 긴 부분수열의 길이를
  구하는 표준 DP 문제입니다. (DNA 정렬, diff 알고리즘 등 응용 많음)
- 본 지문과 테스트 케이스는 본 학습 자료를 위해 자체적으로 작성되었습니다.

▣ 작은 예시
  s1 = "ABCBDAB"
  s2 = "BDCABA"

  공통 부분수열 후보: "B", "BCB", "BDAB", "BCAB", ...
  가장 긴 공통 부분수열의 길이: 4   (예: "BDAB" 또는 "BCAB")

▣ 구현할 함수
lcs_length(s1: str, s2: str) -> int
  - 두 문자열의 가장 긴 공통 부분수열의 길이를 정수로 반환합니다.
  - 어느 한쪽이라도 빈 문자열이면 0 을 반환합니다.

▣ 제약
- 0 <= len(s1), len(s2) <= 500 정도면 충분합니다 (O(m*n) 2차원 DP).

▣ 힌트 (2차원 DP)
- dp[i][j] := s1[0:i] 와 s2[0:j] 의 LCS 길이 (1-based 로 보면 편함)
- 점화식:
    if s1[i-1] == s2[j-1]:   dp[i][j] = dp[i-1][j-1] + 1
    else:                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- 초기 조건: dp[0][*] = dp[*][0] = 0
- 최종 답은 dp[len(s1)][len(s2)] 입니다.
"""


def lcs_length(s1: str, s2: str) -> int:
    """
    s1, s2 의 가장 긴 공통 부분수열의 길이를 반환.
    어느 한쪽이라도 비어 있으면 0 을 반환합니다.
    """
    # TODO: 빈 문자열 처리
    if s1 == "" or s2 == "":
        return 0
    # TODO: (len(s1)+1) x (len(s2)+1) 크기의 2차원 dp 배열을 0 으로 초기화
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    print(dp)
    # TODO: 이중 반복문으로 점화식에 따라 dp 채우기
    for i in range(1,len(s1)+1):
      for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    # TODO: dp[len(s1)][len(s2)] 반환
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    print("[테스트 1] 한쪽이 빈 문자열")
    print(f'  s1="", s2="abc" -> LCS 길이={lcs_length("", "abc")}')
    print()

    print("[테스트 2] 두 문자열이 동일")
    print(f'  s1="abc", s2="abc" -> LCS 길이={lcs_length("abc", "abc")}')
    print()

    print("[테스트 3] 공통 원소가 전혀 없음")
    print(f'  s1="abc", s2="xyz" -> LCS 길이={lcs_length("abc", "xyz")}')
    print()

    print("[테스트 4] 표준 예시 1")
    print(f'  s1="abcde", s2="ace" -> LCS 길이={lcs_length("abcde", "ace")}')
    print()

    print("[테스트 5] 표준 예시 2")
    print(f'  s1="AGGTAB", s2="GXTXAYB" -> LCS 길이={lcs_length("AGGTAB", "GXTXAYB")}')
    print()

    print("[테스트 6] 두 LCS 후보가 길이가 같은 경우")
    print(f'  s1="ABCBDAB", s2="BDCABA" -> LCS 길이={lcs_length("ABCBDAB", "BDCABA")}')
