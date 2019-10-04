from FantasyFootballDjango.TeamModel import *
import requests

# dictionary of names in league -> key is displayName, value is id
nameDetails = {}
overallWinLoss = {}

def gatherRawData(league_id, year):
      # url - Cookies are used to view private leagues
      url = "http://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/555232?view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mSettings&view=mTeam&view=modular&view=mNav"

      r = requests.get(url, cookies={"swid": "{C2CDCDF5-70DB-44AE-BCC8-6E56D7BF5386}",
                                     "espn_s2": "AEAcCx48E1uDuGYKbROmriamC%2BSvzArjxBNZ8E%2Bb5Te4%2BFmE1heHdpOE4%2FhAdfljb3Z9GRsscZAYRqqP4OwRmKJgxzeeikIJOaUQBvRhY6AWmFhZmS3TXixk51fslzj56kpPPO39INCXyBmmHz6sGXksQ2hWCNpukhL6ltUkf3MoaogrKKn3uJog1mvsn%2BsX3M0vNe0KTqigdrjlPKn%2F5wY38PWne3VieU8LNhu6S1BUdkppCbuRAUqhjDM%2FCV%2FRXgXB05eVLILDr6FZlRJUgPPn"})
      d = r.json()
      listUsers = analyzeData(d)
      return listUsers

def analyzeData(data):
      listUsers = []
      for x in data.get("teams"):
            curTeam = TeamModel()
            curTeam.teamNickname = x.get("nickname")
            curTeam.teamAbbrv = x.get("abbrev")
            curTeam.teamComplexID = x.get("primaryOwner")
            curTeam.teamSimpleID = x.get("id")
            curTeam.teamCurProjRank = x.get("currentProjectedRank")
            curTeam.teamDraftProjRank = x.get("draftDayProjectedRank")
            curTeam.teamPlayoffSeed = x.get("playoffSeed")
            curTeam.teamPointsFor = x.get("record").get("overall").get("pointsFor")
            curTeam.teamPointsAgainst = x.get("record").get("overall").get("pointsAgainst")
            curTeam.teamAwayRecord = [x.get("record").get("away").get("wins"), x.get("record").get("away").get("losses"), x.get("record").get("away").get("ties")]
            curTeam.teamHomeRecord = [x.get("record").get("home").get("wins"), x.get("record").get("home").get("losses"), x.get("record").get("home").get("ties")]
            curTeam.teamDivRecord = [x.get("record").get("division").get("wins"), x.get("record").get("division").get("losses"), x.get("record").get("division").get("ties")]
            curTeam.teamOverallRecord = [x.get("record").get("overall").get("wins"), x.get("record").get("overall").get("losses"), x.get("record").get("overall").get("ties")]
            curTeam.teamTotalTransactions = x.get("transactionCounter").get("acquisitions")
            curTeam.teamTotalDrops = x.get("transactionCounter").get("drops")
            curTeam.teamTotalTrades = x.get("transactionCounter").get("trades")
            curTeam.teamWaiverRank = x.get("waiverRank")
            listUsers.append(curTeam)
      return listUsers