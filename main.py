###game start 3:
import requests
import json
import time
import requests
import datetime
import pprint

current_milli_time = lambda: int(round(time.time() * 1000))

def EpochTimeWithSeconds(seconds=0):
   return int(round(time.mktime((datetime.datetime.fromtimestamp(time.time()) + datetime.timedelta(seconds=seconds)).timetuple()) *1000))

print 'Ininitializing configuration'
md5 = "335ffa0f6ba6acb4db81b33dec254c09"
equipedcharacter = ""


session = "djE6YWhOemZuZHBiblJsY20xMWRHVXRNVFV4TURBeGNsRUxFZ1pRYkdGNVpYSWlHV1YyWlhKM2FXNW5Mek13TURrM01URTJNalUzTmpZd05qUU1DeElOVUd4aGVXVnlVMlZ6YzJsdmJpSVpaWFpsY25kcGJtY3ZNekF3T1RjeE1UWXlOVGMyTmpBMk5Bdy84ZjY1ZDAyNC1kMzA0LTRiNDQtYjExMS0yYTU0NDNhYmQ5MDM="
weekid = 0
sidekickleft = ""
sidekickright = ""
clanid = ""

githash = "2d820a525" #i haven't seen this effect the behaviour when it's changed


#userid Wouter
userid = "3009711625766064"

#this game data only works with the character that gets double the money
gamedata = {"runs":1000,"score":180,"xpearned":100,"coinsearned":380,"waittime":4,"energygained":0}

bossdata = {"damageToBeDone":2000000,"waittime":5}


headers = {
    'x-wintermute-session': session,
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://apps-141184676316522.apps.fbsbx.com/instant-bundle/1174389249249108/2402152366521208/index.html?version=861&gcgs=1&source=fbinstant-141184676316522&IsMobileWeb=0',
    'Origin': 'https://apps-141184676316522.apps.fbsbx.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/json;charset=UTF-8',
}

def GamestartRun(gamedata):

   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:" + md5,
            "ledgerVersion":"37.4.0",
            "gitHash":"a0f3b735a",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"everwing"
         },
         "userData":{
            "contextID":"default",
            "userID":userid
         },
         "storageData":{
            "contextID":"default",
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"gameStart",
            "params":{

            },
            "simulateTime":EpochTimeWithSeconds()
         }
      },
      "returnRecord":False,
      "returnState":True
   }
   sendRequest(data)


   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:" + md5,
            "ledgerVersion":"37.4.0",
            "gitHash":githash,
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"everwing"
         },
         "userData":{
            "contextID":"default",
            "userID":userid
         },
         "storageData":{
            "contextID":"default",
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"gameComplete",
            "params":{
               "score":gamedata["score"],
               "xpEarned":gamedata["xpearned"],
               "coinsEarned":gamedata["coinsearned"],
               "energyEarned":gamedata["energygained"],
               "eggTypeFound":"",
               "sidekick1Key":sidekickleft,
               "sidekick2Key":sidekickright,
               "qa":False
            },
            "otherLedgerStorageDatas":{
               "clanPersonal":{
                  "schemaName":"clanPersonal",
                  "storageUserID":userid,
                  "storageContextID":"clan_2261025580693541"
               },
               "clan":{
                  "schemaName":"clan",
                  "storageUserID":"default",
                  "storageContextID":"clan_2261025580693541"
               }
            },
            "simulateTime":EpochTimeWithSeconds(gamedata["waittime"] * 4)
         }
      },
      "returnRecord":False,
      "returnState":True
   }

   time.sleep(gamedata["waittime"] / 2)
   sendRequest(data)


def raidRun(bossdata):

   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:7d16d9afb3a3a31c21b06d7830a94922",
            "ledgerVersion":"37.4.0",
            "gitHash":"a0f3b735a",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"everwing"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"default",
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"checkInToClan",
            "params":{
               "mapID":"aTaleOfFireAndIce",
               "name":"Cracker",
               "photo":"https://platform-lookaside.fbsbx.com/platform/instantgames/profile_pic.jpg?igpid=3009711625766064&height=256&width=256&ext=1572372253&hash=AeQowhGQu40DSYSn",
               "playerLevel":2,
               "characterID":"standard",
               "characterLevel":6,
               "leftSidekickID":"FC02",
               "leftSidekickLevel":2,
               "rightSidekickID":"",
               "rightSidekickLevel":0
            },
            "otherLedgerStorageDatas":{
               "clan":{
                  "schemaName":"clan",
                  "storageUserID":"default",
                  "storageContextID":"clan_" + clanid
               },
               "clanPersonal":{
                  "schemaName":"clanPersonal",
                  "storageUserID":userid,
                  "storageContextID":"clan_" + clanid
               }
            },
            "simulateTime":EpochTimeWithSeconds(0)
         }
      },
      "returnRecord":False,
      "returnState":True
   }


   responseObject = sendRequest(data)
   actionIndex = responseObject['state']['multiWriteStates'][0]['actionIndex']
   actionIndexUpdate = responseObject['state']['multiWriteStates'][1]['actionIndex']
   bosses = responseObject['state']['multiWriteStates'][1]['instances']
   currentBoss = bosses[-1]
   nodeId = currentBoss['stats']['nodeID']

   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:335ffa0f6ba6acb4db81b33dec254c09",
            "ledgerVersion":"37.4.0",
            "gitHash":"dfbb85677",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"clan"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"clan_" + clanid,
            "userID":'default'
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"updateBoss",
            "simulateTime":EpochTimeWithSeconds(1)
         },
         "personalSchemaManagerData":{
            "name":"clanPersonal"
         },
         "expectedActionIndex":actionIndexUpdate
      },
      "returnRecord":False,
      "returnState":True
   }


   responseObject = sendRequest(data)['state']

   boss = responseObject['instances'][-1]['stats']
   hpLeft = boss['health'] - boss['damage']
   percentageleft = round(float(hpLeft - bossdata['damageToBeDone']) / float(boss['health']) *100,2)



   print "   Raid start"

   # Raid start
   data = {

      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:8e3dd38bc50327af7fdc362cd6984614",
            "ledgerVersion":"37.4.0",
            "gitHash":"a0f3b735a",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"clanPersonal"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"clan_" + clanid,
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"raidStart",
            "params":{
            },
            "otherLedgerStorageDatas":{
               "clan":{
                  "schemaName":"clan",
                  "storageUserID":"default",
                  "storageContextID":"clan_" + clanid
               }
            },
            "simulateTime":EpochTimeWithSeconds(1)
         },
         "expectedActionIndex":actionIndex
      },
      "returnRecord":False,
      "returnState":True
   }

   sendRequest(data)


   # Raid complete:
   time.sleep(bossdata["waittime"])

   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:8e3dd38bc50327af7fdc362cd6984614",
            "ledgerVersion":"37.4.0",
            "gitHash":"a0f3b735a",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"clanPersonal"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"clan_" + clanid,
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"raidComplete",
            "params":{
               "damage":bossdata['damageToBeDone'],
               "mapID":"aTaleOfFireAndIce",
               "weekID":weekid,
               "nodeID":nodeId
            },
            "simulateTime":EpochTimeWithSeconds(15)
         },
         "expectedActionIndex":actionIndex + 1
      },
      "returnRecord":False,
      "returnState":True
   }

   sendRequest(data)

   print "   starting one arcade for energy"
   GamestartRun({"runs":1,"score":100,"xpearned":20,"coinsearned":100,"waittime":4,"energygained":1})



   if hpLeft < bossdata['damageToBeDone']:
      print 'boss is dead, up to the next one!'

   else:
      print '   HP left: ' + str(hpLeft - bossdata['damageToBeDone']) + ',  percentage left: ' + str(percentageleft) + '%'


def sendRequest(data,continueOnError=False):
   dataJson = json.dumps(data)
   response = requests.post('https://wintermute-151001.appspot.com/game/run_action', headers=headers, data=dataJson)
   if(response.status_code != 200):
       print 'something went wrong with request:'
       print data
       print 'received status code: ' + str(response.status_code)
       print 'received error:'
       print response.content
       if(continueOnError == False):
         quit()
       else:
          return False
   else:
      return json.loads(response.content)



def claimrewards(nodeId):
   timestamp = EpochTimeWithSeconds()
   # timestamp = 1570394581000
   #attempt to modify timestamp for cash rewards, failed
   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:3aff6a3496e3bd50e7717745e0d9ab80",
            "ledgerVersion":"37.4.0",
            "gitHash":"dfbb85677",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"everwing"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"default",
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"claimClanLoot",
            "params":{
               "nodeID":nodeId
            },
            "simulateTime":timestamp
         }
      },
      "returnRecord":False,
      "returnState":True
   }

   reward = sendRequest(data,True)
   print 'reward:'
   if(reward):
      rewardData = reward['state']['actionResult']['chest']
      print '   received item:' + str(rewardData['rewardType']) + ', count: ' + str(rewardData['rewardCount']) + ', reward Value: ' + str(rewardData['rewardValue'])
      print '   timestamp: ' + str(timestamp)




def initEverwing():
    print "running initializing method to retrieve your data"
    global weekid
    global sidekickleft
    global sidekickright
    global clanid

    #max all characters boosts
    #set all chest max levels for all bosses
    #retrieve info for left/right kick

    data = {
       "clientData":{
          "ledgerData":{
             "schemaHash":"md5:1db20a4f8b3c8f327cce8826a3d9b673",
             "ledgerVersion":"37.4.0",
             "gitHash":"215e464de",
             "gitBranch":"master"
          },
          "appID":"everwing",
          "schemaManagerData":{
             "name":"everwing"
          },
          "userData":{
             "contextID":"default",
             "userID":userid
          },
          "storageData":{
             "contextID":"default",
             "userID":userid
          },
          "action":{
             "type":"RUN_FUNCTION",
             "functionName":"updateLastLoginDate",
             "params":{

             },
             "simulateTime":EpochTimeWithSeconds()
          }
       },
       "returnRecord":False,
       "returnState":True
    }

    response = sendRequest(data,True)
    print json.dumps(response)

    responseData = response["state"]["instances"]


    weekid = responseData[760]["stats"]["weekID"]
    clanid = responseData[0]["stats"]["clanID"]
    sidekickleft = responseData[361]["key"]
    sidekickright = responseData[346]["key"]

    print "results of init variables, weekid, clanid, sidekickleft, sidekickright"
    print weekid
    print clanid
    print sidekickleft
    print sidekickright

def setClanLootReward(nodeID):

   data = {
      "clientData":{
         "ledgerData":{
            "schemaHash":"md5:7d16d9afb3a3a31c21b06d7830a94922",
            "ledgerVersion":"37.4.0",
            "gitHash":"a0f3b735a",
            "gitBranch":"master"
         },
         "appID":"everwing",
         "schemaManagerData":{
            "name":"everwing"
         },
         "userData":{
            "contextID":clanid,
            "userID":userid
         },
         "storageData":{
            "contextID":"default",
            "userID":userid
         },
         "action":{
            "type":"RUN_FUNCTION",
            "functionName":"setClanLootReward",
            "params":{
               "nodeID":nodeID,
               "treasureLevel":20,
               "damageNormalized":0.966383,
               "hadBestRun":True,
               "wasFirstToMaxReward":True
            },
            "otherLedgerStorageDatas":{
               "clanPersonal":{
                  "schemaName":"clanPersonal",
                  "storageUserID":userid,
                  "storageContextID":"clan_" + clanid
               }
            },
            "simulateTime":EpochTimeWithSeconds()
         }
      },
      "returnRecord":False,
      "returnState":True
   }
   sendRequest(data,True)
   print "set the reward of boss level " + str(nodeID+1)

   time.sleep(2)



#claims daily cash reward + gems + fb login reward
def claimDailyRewards():
   return 'a'

def boostAllCharacters():
   characters = ['lucia','magnet','trixie','lyra','arcana','jade','lenore','coin','sophia','fiona','standard','neve']
   for character in characters:
      for i in range(5):
         data = {
            "clientData":{
               "ledgerData":{
                  "schemaHash":"md5:9b25e1955913ee30273d9371e6b5b077",
                  "ledgerVersion":"37.4.0",
                  "gitHash":"a0f3b735a",
                  "gitBranch":"master"
               },
               "appID":"everwing",
               "schemaManagerData":{
                  "name":"everwing"
               },
               "userData":{
                  "contextID":"default",
                  "userID":userid
               },
               "storageData":{
                  "contextID":"default",
                  "userID":userid
               },
               "action":{
                  "type":"RUN_FUNCTION",
                  "functionName":"claimPowerBoost",
                  "params":{
                     "characterID":character
                  },
                  "simulateTime":EpochTimeWithSeconds()
               }
            },
            "returnRecord":False,
            "returnState":True
         }
         sendRequest(data,True)
         print 'boosted ' + character + ' amount of boosters: ' + str(i+1)

         time.sleep(2)

### getting a session:
def getSessionID():


   cookie = "YqDl12iyKFJUxQWcg8fTzTouRqDB4NWLpqswOJ_NYY8.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTU3MTU2NDA1MiwicGxheWVyX2lkIjoiMzAwOTcxMTYyNTc2NjA2NCIsInJlcXVlc3RfcGF5bG9hZCI6IkxPR0lOX1JFUVVFU1QifQ"

   headers = {
       'Accept': 'application/json, text/plain, */*',
       'Referer': 'https://apps-141184676316522.apps.fbsbx.com/instant-bundle/1174389249249108/2558543447541259/index.html?version=866&gcgs=1&source=fbinstant-141184676316522&IsMobileWeb=0',
       'Origin': 'https://apps-141184676316522.apps.fbsbx.com',
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
       'Sec-Fetch-Mode': 'cors',
       'Content-Type': 'application/json;charset=UTF-8',
   }

   data = {
      "signedPayload":cookie,
      "appID":"everwing",
      "clientData":{
         "ledgerVersion":"37.4.0",
         "gitBranch":"master",
         "gitHash":"dfbb85677"
      },
      "userID":"3009711625766064"
   }
   dataJson = json.dumps(data)
   response = requests.post('https://wintermute-151001.appspot.com/v2/game/session', headers=headers, data=dataJson)


   print response
   print response.content

def claimAndSetAllRewards(levelstart,levelend):
   for nodeID in range(levelstart,levelend):
      setClanLootReward(nodeID)
      for a in range(5):
         print 'attempt to claim reward for node #' + str(nodeID) + ', chest number: ' + str(a)
         claimrewards(nodeID)
         time.sleep(2)



def buyNewCharacters(amount):
   for i in range(amount):
      timestamp = EpochTimeWithSeconds()

      #arcana character
      # timestamp = 1570393665000

      data = {
         "clientData":{
            "ledgerData":{
               "schemaHash":"md5:3aff6a3496e3bd50e7717745e0d9ab80",
               "ledgerVersion":"37.4.0",
               "gitHash":"dfbb85677",
               "gitBranch":"master"
            },
            "appID":"everwing",
            "schemaManagerData":{
               "name":"everwing"
            },
            "userData":{
               "contextID":clanid,
               "userID":userid
            },
            "storageData":{
               "contextID":"default",
               "userID":userid
            },
            "action":{
               "type":"RUN_FUNCTION",
               "functionName":"purchaseStarTokens",
               "params":{
                  "gachaID":"starTokenCommonGacha",
                  "priceID":"regular"
               },
               "simulateTime":timestamp
            }
         },
         "returnRecord":False,
         "returnState":True
      }

      result = sendRequest(data)
      print "Bought 11 new characters, attempt " + str(i)
      print result['state']['actionResult']
      print 'timestampe: ' + str(timestamp)
      time.sleep(2)

# getSessionID()

initEverwing()


#codeblock for boss runs
for i in range(1000):
   print "Starting boss raid #" + str(i)
   raidRun(bossdata)
   time.sleep(2)

#codeblock for normal runs
for i in range(1000):
   GamestartRun(gamedata)
   print 'finished run #' + str(i+1) + ' total money collected: ' + str((i+1)*gamedata['coinsearned'])

quit()


