
class TeamModel:
    teamName = ""
    teamNickname = ""
    teamAbbrv = ""
    teamComplexID = ""
    teamSimpleID = -1
    teamCurProjRank = -1
    teamDraftProjRank = -1
    teamPlayoffSeed = -1
    teamPointsFor = -1
    teamPointsAgainst =  -1
    teamFinalRank = -1
    teamAwayRecord = ["-1:W", "-1:L", "-1:T"]
    teamHomeRecord = ["-1:W", "-1:L", "-1:T"]
    teamDivRecord = ["-1:W", "-1:L", "-1:T"]
    teamOverallRecord = ["-1:W", "-1:L", "-1:T"]
    teamTotalTransactions = -1
    teamTotalDrops = -1
    teamTotalTrades = -1
    teamWaiverRank = -1

def __init__(self, teamName, teamNickname, teamAbbrv, teamComplexID, teamSimpleID, teamCurProjRank,
             teamDraftProjRank, teamPlayoffSeed, teamPointsFor, teamPointsAgainst, teamFinalRank, teamAwayRecord, teamHomeRecord, teamDivRecord, teamOverallRecord,
             teamTotalTransactions, teamTotalDrops, teamTotalTrades, teamWaiverRank):
    self.teamName = teamName
    self.teamNickname = teamNickname
    self.teamAbbrv = teamAbbrv
    self.teamComplexID = teamComplexID
    self.teamSimpleID = teamSimpleID
    self.teamCurProjRank = teamCurProjRank
    self.teamDraftProjRank = teamDraftProjRank
    self.teamPlayoffSeed = teamPlayoffSeed
    self.teamPointsFor = teamPointsFor
    self.teamPointsAgainst = teamPointsAgainst
    self.teamFinalRank = teamFinalRank
    self.teamAwayRecord = teamAwayRecord
    self.teamHomeRecord = teamHomeRecord
    self.teamDivRecord = teamDivRecord
    self.teamOverallRecord = teamOverallRecord
    self.teamTotalTransactions = teamTotalTransactions
    self.teamTotalDrops = teamTotalDrops
    self.teamTotalTrades = teamTotalTrades
    self.teamWaiverRank = teamWaiverRank