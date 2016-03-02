import Rust
import UnityEngine
import ItemManager
import ItemContainer
import StorageContainer
import PlayerInventory
import BasePlayer

class PowerStruggle:
    def __init__(self):
        self.Title = "PowerStruggle"
        self.Author = "Hoober"
        self.Version = V(0, 0, 1)
        self.HasConfig = True

    def OnServerInitialized(self):
        command.AddChatCommand('scores', self.Plugin, 'chat_scores')
        command.AddConsoleCommand("ps.scores", self.Plugin, "console_scores")
        for item in ItemManager.itemList:
            if item.name == self.Config["currency_res"]:
                item.stackable = self.Config["currency_stack"]

    def LoadDefaultConfig(self):
        self.Config["currency_item"] = "battery.small"
        self.Config["currency_res"] = "battery_small.item"
        self.Config["currency_stack"] = 1000

    def calc_scores(self):
        scores = {}

        for item in UnityEngine.Resources.FindObjectsOfTypeAll(StorageContainer):
            if hasattr(item, "inventory") and type(item.inventory) == ItemContainer:
                if not item.OwnerID == 0:
                    for i in item.inventory.itemList:
                        if i.info.name == self.Config["currency_res"]:
                            if not item.OwnerID in scores:
                                scores[item.OwnerID] = 0
                            scores[item.OwnerID] += i.amount

        # for p in BasePlayer.activePlayerList:
        #     for i in p.inventory.containerMain.itemList:
        #         if i.info.name == "{}.item".format(self.Config["currency_res"]):
        #             # print "{} (x{})".format(i.info.name, i.amount)
        #             if not p.steamId in scores:
        #                 scores.p.steamId = 0
        #             scores[p.steamId] += i.amount

        return scores


    def chat_scores(self,player,cmd,args):
        dataObj = data.GetData("PowerStruggle")

        scores = self.calc_scores()

        for user, score in self.calc_scores().iteritems():
            rust.SendChatMessage(player, "{}: {}".format(dataObj["name_cache"][user], score), None, "76561198235146288")

        if not scores:
            rust.SendChatMessage(player, "No players have any {}".format(self.Config["currency_item"]), None, "76561198235146288")

    def console_scores(self, arg):
        dataObj = data.GetData("PowerStruggle")
        for user, score in self.calc_scores().iteritems():
            print("{}: {}".format(dataObj["name_cache"][user], score))

    # Hooks

    def OnPlayerInit(self, player):
        dataObj = data.GetData("PowerStruggle")
        if not "name_cache" in dataObj:
            dataObj["name_cache"] = {}
        dataObj["name_cache"][player.userID] = player.displayName
        dataObj["id_cache"][player.displayName] = player.userID
        print "{}: {}".format(player.displayName, player.userID)
        data.SaveData("PowerStruggle")

    def OnEntitySpawned(self, entity):
        if hasattr(entity, "inventory") and type(entity.inventory) == ItemContainer:
            item = ItemManager.CreateByName(self.Config["currency_item"])
            item.MoveToContainer(entity.inventory, -1, False);

            prefab_name = entity.ToString().split("/")[-1].split(".prefab")[0]
            print "Adding {} to {} ({})".format(self.Config["currency_item"], prefab_name, entity.GetType())
