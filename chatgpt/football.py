# Question 7: Football League Points Table and Goal Difference
# Difficulty: Advanced · Time: 60–90 minutes
# Build a league table for multiple football teams. Every pair of teams must play twice.
# Each match contains: Match ID, home team, away team, home goals and away goals.
# Requirements
# 1. Register unique, non-empty team names.
# 2. Validate goals as non-negative integers.
# 3. Prevent a team from playing itself and prevent any pair from playing more than twice.
# 4. Award 3 points for a win, 1 point each for a draw and 0 points for a loss. 
# 5. Track matches played, wins, draws, losses, goals scored and goals conceded.
# 6. Calculate goal difference using goals scored minus goals conceded.
# 7. Rank teams by points descending, goal difference descending, goals scored descending and team name ascending.
# 8. Do not update statistics when a match record is invalid.
# 9. Display the final table only after every pair has played twice.
# 10. Display the champion, the team with the most goals and the team with the fewest goals conceded.

n=int(input("noof teams:"))
if n<=0:
    raise Exception("invalid no.of teams")
tnames =[]
for i in range(n):
    tname=input("enter team name")
   
    if  not tname or tname in tnames:
        raise Exception("duplicted")
    tnames.append(tname)

teams={}

for tname in tnames:
    teams[tname]={
            "Match_played":0,"Wins":0,"Draws":0,"losses":0,"goals_for":0,"goals_against":0,"goals_difference":0,"total_points":0}


match_id=1  
for i in range(n):
    for j in range(i+1,n):
        while True:
            try:
                hteam,ateam=tnames[i],tnames[j]
                hgoals=int(input(f"{hteam} goals: "))
                agoals=int(input(f"{ateam} goals: "))

                # if not hgoals or not agoals:
                #     raise ValueError("empty not accepted")
                if hgoals<0 or agoals <0:
                    raise ValueError("invalid score")
                break

            except ValueError as e:
                print("invalid inputs ,enter numeric values")

        if hgoals>agoals:
            teams[hteam]["Wins"] += 1
            teams[hteam]["total_points"] += 3
            teams[hteam]["Match_played"] += 1
            teams[ateam]['Match_played']+=1
            teams[hteam]["goals_for"] += hgoals
            teams[ateam]['goals_for']+=agoals
            teams[hteam]["goals_against"] += agoals
            teams[ateam]['goals_against']+=hgoals
            teams[ateam]['losses']+=1
            teams[hteam]['goals_difference']=teams[hteam]['goals_for']-teams[hteam]['goals_against']
            teams[ateam]['goals_difference']=teams[ateam]['goals_for']-teams[ateam]['goals_against']

        elif agoals>hgoals:
            teams[ateam]['Wins']+=1
            teams[ateam]["total_points"]+=3
            teams[ateam]["Match_played"]+=1
            teams[hteam]['Match_played']+=1
            teams[ateam]['goals_for']+=agoals
            teams[hteam]['goals_for']+=hgoals
            teams[ateam]['goals_against']+=hgoals
            teams[hteam]['goals_against']+=agoals
            teams[hteam]['losses']+=1

            for team in [ateam,hteam]:
                teams[ateam]['goals_difference']=teams[ateam]['goals_for']-teams[ateam]['goals_against']
                teams[hteam]['goals_difference']=teams[hteam]['goals_for']-teams[hteam]['goals_against']

        elif agoals==hgoals:
            teams[ateam]['total_points']+=1
            teams[hteam]['total_points']+=1
            teams[hteam]["Match_played"]+=1
            teams[ateam]["Match_played"]+=1
            teams[ateam]['Draws']+=1
            teams[hteam]['Draws']+=1
            teams[ateam]['goals_for']+=agoals
            teams[hteam]['goals_for']+=hgoals
            teams[ateam]['goals_against']+=hgoals
            teams[hteam]['goals_against']+=agoals
            for team in [ateam,hteam]:
                teams[ateam]['goals_difference']=teams[ateam]['goals_for']-teams[ateam]['goals_against']
                teams[hteam]['goals_difference']=teams[hteam]['goals_for']-teams[hteam]['goals_against']
            print("matchId: ",match_id)
            match_id+=1

        print(f"{teams}")

    # 7. Rank teams by points descending, goal difference descending, goals scored descending and team name ascending.
ranked_teams = list(teams.keys())

for i in range(len(ranked_teams)):
    for j in range(len(ranked_teams) - 1):
        team1 = ranked_teams[j]
        team2 = ranked_teams[j + 1]
        # if team1<team2:
        #     ranked_teams[j],ranked_teams[j+1]=ranked_teams[j+1],ranked_teams[j]
        swap = False

        if teams[team1]["total_points"] < teams[team2]["total_points"]:
            swap = True

        elif teams[team1]["total_points"] == teams[team2]["total_points"]:

            if teams[team1]["goals_difference"] < teams[team2]["goals_difference"]:
                swap = True

            elif teams[team1]["goals_difference"] == teams[team2]["goals_difference"]:

                if teams[team1]["goals_for"] < teams[team2]["goals_for"]:
                    swap = True

                elif teams[team1]["goals_for"] == teams[team2]["goals_for"]:
                    if team1.lower() > team2.lower():
                        swap = True

        if swap:
            ranked_teams[j], ranked_teams[j + 1] = ranked_teams[j + 1], ranked_teams[j]


print("Football League Points Table")
# print("-" * 90)
# print(f"{'Team':<15}{'MP':<6}{'W':<6}{'D':<6}{'L':<6}{'GF':<6}{'GA':<6}{'GD':<6}{'Points':<8}")

for team in ranked_teams:
    stats = teams[team]
    print(
        f"{team:<15}"
        f"{stats['Match_played']:<6}"
        f"{stats['Wins']:<6}"
        f"{stats['Draws']:<6}"
        f"{stats['losses']:<6}"
        f"{stats['goals_for']:<6}"
        f"{stats['goals_against']:<6}"
        f"{stats['goals_difference']:<6}"
        f"{stats['total_points']:<8}"
    )





        





# def register_teams():
#     while True:
#         try:
#             n = int(input("Enter number of teams: "))
#             if n < 2:
#                 print("At least 2 teams are required.")
#                 continue
#             break
#         except ValueError:
#             print("Enter a valid integer.")

#     teams = {}

#     for i in range(n):
#         while True:
#             tname = input(f"Enter team {i + 1} name: ").strip()

#             if not tname:
#                 print("Team name cannot be empty.")
#             elif tname.lower() in [name.lower() for name in teams]:
#                 print("Team name already exists.")
#             else:
#                 teams[tname] = {
#                     "Match_played": 0,
#                     "Wins": 0,
#                     "Draws": 0,
#                     "Losses": 0,
#                     "goals_for": 0,
#                     "goals_against": 0,
#                     "goals_difference": 0,
#                     "total_points": 0
#                 }
#                 break

#     return teams


# def play_match(home, away, teams, match_id):
#     print(f"\nMatch {match_id}: {home} vs {away}")

#     while True:
#         try:
#             hgoal = int(input(f"Enter goals scored by {home}: "))
#             agoal = int(input(f"Enter goals scored by {away}: "))

#             if hgoal < 0 or agoal < 0:
#                 print("Goals cannot be negative.")
#                 continue

#             break
#         except ValueError:
#             print("Enter goals as valid integers.")

#     teams[home]["Match_played"] += 1
#     teams[away]["Match_played"] += 1

#     teams[home]["goals_for"] += hgoal
#     teams[home]["goals_against"] += agoal

#     teams[away]["goals_for"] += agoal
#     teams[away]["goals_against"] += hgoal

#     if hgoal > agoal:
#         teams[home]["Wins"] += 1
#         teams[home]["total_points"] += 3
#         teams[away]["Losses"] += 1

#     elif agoal > hgoal:
#         teams[away]["Wins"] += 1
#         teams[away]["total_points"] += 3
#         teams[home]["Losses"] += 1

#     else:
#         teams[home]["Draws"] += 1
#         teams[away]["Draws"] += 1
#         teams[home]["total_points"] += 1
#         teams[away]["total_points"] += 1

#     teams[home]["goals_difference"] = (
#         teams[home]["goals_for"] - teams[home]["goals_against"]
#     )
#     teams[away]["goals_difference"] = (
#         teams[away]["goals_for"] - teams[away]["goals_against"]
#     )

#     return match_id + 1


# def play_league(teams):
#     team_names = list(teams.keys())
#     match_id = 1

#     for i in range(len(team_names)):
#         for j in range(i + 1, len(team_names)):
#             home = team_names[i]
#             away = team_names[j]

#             match_id = play_match(home, away, teams, match_id)
#             match_id = play_match(away, home, teams, match_id)

#     return teams


# def sort_teams(teams):
#     team_names = list(teams.keys())
#     n = len(team_names)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             team1 = team_names[j]
#             team2 = team_names[j + 1]

#             swap = False

#             if teams[team1]["total_points"] < teams[team2]["total_points"]:
#                 swap = True

#             elif teams[team1]["total_points"] == teams[team2]["total_points"]:
#                 if teams[team1]["goals_difference"] < teams[team2]["goals_difference"]:
#                     swap = True

#                 elif teams[team1]["goals_difference"] == teams[team2]["goals_difference"]:
#                     if teams[team1]["goals_for"] < teams[team2]["goals_for"]:
#                         swap = True

#                     elif teams[team1]["goals_for"] == teams[team2]["goals_for"]:
#                         if team1.lower() > team2.lower():
#                             swap = True

#             if swap:
#                 team_names[j], team_names[j + 1] = team_names[j + 1], team_names[j]

#     return team_names


# def display_table(teams, team_names):
#     print("\nFOOTBALL LEAGUE POINTS TABLE")
#     print("-" * 100)
#     print(
#         f"{'Team':<15}{'MP':>5}{'W':>5}{'D':>5}{'L':>5}"
#         f"{'GF':>7}{'GA':>7}{'GD':>7}{'Points':>9}"
#     )
#     print("-" * 100)

#     for name in team_names:
#         t = teams[name]
#         print(
#             f"{name:<15}{t['Match_played']:>5}{t['Wins']:>5}"
#             f"{t['Draws']:>5}{t['Losses']:>5}"
#             f"{t['goals_for']:>7}{t['goals_against']:>7}"
#             f"{t['goals_difference']:>7}{t['total_points']:>9}"
#         )

#     print("-" * 100)

#     print(f"Champion: {team_names[0]}")

#     max_goals = max(t["goals_for"] for t in teams.values())
#     top_scorers = [
#         name for name, t in teams.items()
#         if t["goals_for"] == max_goals
#     ]

#     min_conceded = min(t["goals_against"] for t in teams.values())
#     best_defence = [
#         name for name, t in teams.items()
#         if t["goals_against"] == min_conceded
#     ]

#     print(f"Most goals scored: {', '.join(top_scorers)} ({max_goals})")
#     print(f"Fewest goals conceded: {', '.join(best_defence)} ({min_conceded})")


# teams = register_teams()
# teams = play_league(teams)
# team_names = sort_teams(teams)
# display_table(teams, team_names)
