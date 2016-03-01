import Rust
import ItemManager
import ItemContainer
import PlayerInventory

class PowerStruggle:
    def __init__(self):
        self.Title = "PowerStruggle"
        self.Author = "Hoober"
        self.Version = V(0, 0, 1)
        self.HasConfig = True

    def OnServerInitialized(self):
        command.AddChatCommand('scores', self.Plugin, 'scores')
        command.AddConsoleCommand("server.scores", self.Plugin, "server_scores")
        print "server init"
        print self.Plugin.Title
        # item = ItemManager.CreateByItemID(-770311783)


    def LoadDefaultConfig(self):
        self.Config["authLevel"] = 1
        self.Config["moep"] = (1, 0, 1)
        self.Config["narf"] = { "entry1" : "oink", "entry2" : "blubb" }

    def server_scores(self, arg):
        self.Config["authLevel"] = 2
        # self.SaveConfig()
        dataObj = data.GetData("PowerStruggle")
        dataObj["score"] = 100
        data.SaveData("PowerStruggle")
        print "Score: {0}".format(dataObj["score"])

    def scores(self,player,cmd,args):
        # dataObj = data.GetData("PowerStruggle")
        # dataObj["scores"] = {"Hoober": 100, "Bob": 20}
        # data.SaveData("PowerStruggle")

        # print dataObj.keys()
        # print "Score: {0}".format(dataObj["score"])
        # print "player.displayName=" + player.displayName
        # print "player.userID=" +str(player.userID)
        # print "cmd=" +cmd
        # print "number of arguments="+str(len(args))
        # print str(args)

        for p in player.activePlayerList:
            for i in p.inventory.containerMain.itemList:
                print i
                print dir(i)
                break
                # print dir(i)

        # for user, score in dataObj["scores"].iteritems():
        #     rust.SendChatMessage(player, "{}: {}".format(user, score), None, "76561198235146288")

    # def OnPlayerLoot(self, inventory, target):
    #     print "OnPlayerLoot works!"
    #     if hasattr(target, "inventory"):
    #         print "inventory: {}".format(target.inventory)
    def OnEntityTakeDamage(self, entity, info):
        # print "OnEntityTakeDamage works!"
        if hasattr(entity, "inventory"):
            # print "inventory: {}".format(entity.inventory)
            # print entity.inventory.itemList
            # print dir(entity.inventory.itemList)
            item = ItemManager.CreateByItemID(93832698)
            # print(type(entity.inventory))
            # print dir(item)
            if type(entity.inventory) == ItemContainer:
                item.MoveToContainer(entity.inventory, -1, False);
            # elif type(entity.inventory) == PlayerInventory:
            #     entity.inventory.GiveItem(ItemManager.CreateByName("blood"), 1);

            # #     item.MoveToContainer(entity.inventory, -1, False);
            # entity.inventory.itemList.Add(item)
            # print entity.inventory.itemList

    # def OnEntityDeath(self, entity, info):
    #     print "OnEntityDeath works!"
    #     if hasattr(entity, "inventory"):
    #         print "inventory: {}".format(entity.inventory)
    #         print entity.inventory.itemList
    #         # print dir(entity.inventory.itemList)
    #         item = ItemManager.CreateByItemID(-770311783)
    #         entity.inventory.itemList.Add(item)
    #         print entity.inventory.itemList
            # entity.inventory.itemList
            # item = ItemManager.CreateByItemID(-770311783);
            # print item
            # print dir(entity.inventory)


    def OnEntitySpawned(self, entity):
        if hasattr(entity, "inventory"):
            # print "inventory: {}".format(entity.inventory)
            # print entity.inventory.itemList
            # print dir(entity.inventory.itemList)
            item = ItemManager.CreateByItemID(2021568998)
            item.MoveToContainer(entity.inventory, -1, False);
            print "Adding battery to {} - {}".format(entity.GetType(), entity.gameObject)\