class ApplicationState:
    instance=None
    
    def __init__(self):
        self.isLoggedIn=False
        
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance=ApplicationState()
            return ApplicationState.instance
        
appState1= ApplicationState.getAppState()
print(appState1.isLoggedIn)  #False

appState2= ApplicationState.getAppState()
appState1.isLoggedIn=True

print(appState1.isLoggedIn) #false
print(appState2.isLoggedIn) #true
        