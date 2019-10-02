import requests

def gatherRawData(league_id, year):
      # url - Cookies are used to view private leagues
      url = "http://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/555232?view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mSettings&view=mTeam&view=modular&view=mNav"

      r = requests.get(url, cookies={"swid": "{C2CDCDF5-70DB-44AE-BCC8-6E56D7BF5386}",
                                     "espn_s2": "AEAcCx48E1uDuGYKbROmriamC%2BSvzArjxBNZ8E%2Bb5Te4%2BFmE1heHdpOE4%2FhAdfljb3Z9GRsscZAYRqqP4OwRmKJgxzeeikIJOaUQBvRhY6AWmFhZmS3TXixk51fslzj56kpPPO39INCXyBmmHz6sGXksQ2hWCNpukhL6ltUkf3MoaogrKKn3uJog1mvsn%2BsX3M0vNe0KTqigdrjlPKn%2F5wY38PWne3VieU8LNhu6S1BUdkppCbuRAUqhjDM%2FCV%2FRXgXB05eVLILDr6FZlRJUgPPn"})
      d = r.json()
      print(d)
      return d