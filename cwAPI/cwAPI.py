import requests 
import json
class cwAPI():
    def __init__(self):
        self.headers = {'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json', 'Accept': 'application/json', 'Connection': 'keep-alive', 'DNT': '1'}
        self.ca=None
        self.cert=None
        
    class Wallets():
        def list(self):
            r = requests.get(self.port+"/v2/wallets", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

        def utxoStatistics(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/statistics/utxos", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data  

        def utxo(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/utxo", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data      

        def get(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data             
            
        def delete(self,walletId):
            r = requests.delete(self.port+"/v2/wallets/" + walletId , verify=self.ca, headers=self.headers, cert=self.cert)
            if r.ok:
                return {"OK"}
            json_data = json.loads( r.text)

            return json_data      

        def create(self,name,mnemonic_sentence,passphrase,mnemonic_second_factor=None,address_pool_gap=20):
            data={"name":name,"mnemonic_sentence":mnemonic_sentence,"passphrase":passphrase,"address_pool_gap":address_pool_gap}
            if mnemonic_second_factor!= None:
                data["mnemonic_second_factor"]= mnemonic_second_factor
            r = requests.post(self.port+"/v2/wallets/"  , data=json.dumps(data), verify=self.ca, headers=self.headers, cert=self.cert)

            json_data = json.loads( r.text)

            return json_data   

        def update(self,walletId,name):
            data={"name":name}
            r = requests.put(self.port+"/v2/wallets/" + walletId ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            
            json_data = json.loads( r.text)
            return json_data

        def updatePassphrase(self,walletId,old_passphrase,new_passphrase):
            data={"old_passphrase":old_passphrase,"new_passphrase":new_passphrase}
            r = requests.put(self.port+"/v2/wallets/" + walletId + "/passphrase" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            if r.ok:
                return {"OK"}
            json_data = json.loads( r.text)
            return json_data       

    class Assets():
        def list(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/assets", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

        def mint(self,walletId,mint_burn,passphrase,metadata=None,time_to_live=None):
            data={"walletId":walletId,"mint_burn":mint_burn,"passphrase":passphrase}
            if metadata!=None:
                data["metadata"]=metadata
            if time_to_live!=None:
                data["time_to_live"] = time_to_live

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/assets", data=json.dumps(data), verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

        def get(self,walletId,policyId,assetName=None):
            if assetName==None:
                r = requests.get(self.port+"/v2/wallets/" + walletId + "/assets/" + policyId , verify=self.ca, headers=self.headers, cert=self.cert)
            else:
                r = requests.get(self.port+"/v2/wallets/" + walletId + "/assets/" + policyId+ "/" + assetName , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

    class Addresses():
        def list(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/addresses", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data
        
        def inspect(self,addressId):
            r = requests.get(self.port+"/v2/addresses/"+ addressId, verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

        def Construct(self,payment,stake,validation):
            data={"payment":payment,"stake":stake,"validation":validation}
            r = requests.post(self.port+"/v2/addresses", verify=self.ca, data=json.dumps(data), headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

    class Transactions():
        def paymentFees(self,walletId,payments,withdrawal="self",metadata=None,time_to_live=None):
            data={"payments":payments,"withdrawal":withdrawal}
            if metadata!=None:
                data["metadata"]=metadata
            if time_to_live!=None:
                data["time_to_live"]=time_to_live  

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/payment-fees" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data         

        def create(self,walletId,passphrase,payments,withdrawal="self",metadata=None,time_to_live=None):
            data={"passphrase":passphrase,"payments":payments,"withdrawal":withdrawal}
            if metadata!=None:
                data["metadata"]=metadata
            if time_to_live!=None:
                data["time_to_live"]=time_to_live  

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data   

        def list(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/transactions" , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data   

        def get(self,walletId,transactionId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/transactions/" + transactionId , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def forget(self,walletId,transactionId):
            r = requests.delete(self.port+"/v2/wallets/" + walletId + "/transactions/" + transactionId , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

## TODO Test when implemented
    class TransactionsNew():   
        def construct(self,walletId,payments,withdrawal="self",metadata=None,time_to_live=None):
            data={"payments":payments,"withdrawal":withdrawal}
            if metadata!=None:
                data["metadata"]=metadata
            if time_to_live!=None:
                data["time_to_live"]=time_to_live  

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-construct" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def sign(self,walletId,passphrase,transaction):
            data={"passphrase":passphrase,"transaction":transaction}
            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-sign" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def decode(self,walletId,transaction):
            data={"transaction":transaction}
            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-decode" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def submit(self,walletId,transaction):    
            data={"transaction":transaction}
            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-decode" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def balance(self,walletId,transaction,inputs=None,redeemers=None):
            data={"transaction":transaction}
            if inputs!=None:
                data["inputs"] = inputs
            if redeemers!=None:
                data["redeemers"]=redeemers    
            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-balance" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

    class Migrations():
        def plan(self,walletId,addresses):
            data={"addresses":addresses}

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/transactions-construct" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

        def migrate(self,walletId,passphrase,addresses):
            data={"addresses":addresses,"passphrase":passphrase}
            
            r = requests.post(self.port+"/v2/wallets/" + walletId + "/migrations" ,data=json.dumps(data) , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

    class StakePools():
        def listStakeKeys(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/stake-keys"  , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

        def list(self,stake):
            r = requests.get(self.port+"/v2/stake-pools?stake="+ stake  , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

        def viewMaintananceActions(self):
            r = requests.get(self.port+"/v2/stake-pools/maintenance-actions"  , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

        def triggerMaintananceActions(self,maintenance_action):
            data={"maintenance_action":maintenance_action}
            r = requests.post(self.port+"/v2/stake-pools/maintenance-actions"  , data=json.dumps(data) ,verify=self.ca, headers=self.headers, cert=self.cert)
            if r.ok:
                return {"OK"}
            json_data = json.loads( r.text)
            return json_data     

        def estimateFee(self,walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/delegation-fees" , verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  

        def quit(self,walletId,passphrase):
            data={"passphrase":passphrase}
            r = requests.delete(self.port+"/v2/stake-pools/*/wallets/" + walletId , data=json.dumps(data), verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data  
        def join(self,stakePoolId,walletId,passphrase):
            data={"passphrase":passphrase}
            r = requests.put(self.port+"/v2/stake-pools/" + stakePoolId + "/wallets/" + walletId , data=json.dumps(data), verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 
            
    class Keys():
        def createAccountPublickKey(self,walletId,index,passphrase,format,purpose=None):
            data={"passphrase":passphrase,"format":format}
            if purpose!=None:
                data["purpose"]=purpose

            r = requests.post(self.port+"/v2/wallets/" + walletId + "/keys/" + index , data=json.dumps(data), verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 
        
        def getAccountPublicKey(self, walletId):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/keys",  verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

        def getPublicKey(self, walletId, role, index):
            r = requests.get(self.port+"/v2/wallets/" + walletId + "/keys/" + role + "/" + index,  verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)
            return json_data 

    class Network():
        def information(self):
            r = requests.get(self.port+"/v2/network/information", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data
        
        def clock(self):
            r = requests.get(self.port+"/v2/network/clock", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data

        def parameters(self):
            r = requests.get(self.port+"/v2/network/parameters", verify=self.ca, headers=self.headers, cert=self.cert)
            json_data = json.loads( r.text)

            return json_data
        