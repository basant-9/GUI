import PyQt5.QtWidgets as qtw
import market 

class MainWindow (qtw.QMainWindow ,market.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        
        self.price = 0.0 
        
        self.counts = {
            'oweis': 0,
            'sokary': 0,
            'Apples': 0,
            'Bananas': 0,
            'Guavas': 0
        }
        self.prices = {
            'oweis': 7.0,
            'sokary': 4.5,
            'Apples': 2.4,
            'Bananas': 6.0,
            'Guavas': 4.5 
        } 

        self.oweis.clicked.connect(lambda: self.update('oweis'))
        self.sokary.clicked.connect(lambda: self.update('sokary'))
        self.apples.clicked.connect(lambda: self.update('Apples'))
        self.bananas.clicked.connect(lambda: self.update('Bananas '))
        self.guavas.clicked.connect(lambda: self.update('Guavas')) 
    
    def update(self , fruit):
        self.counts [fruit] += 1
        self.price += self.prices[fruit]
        self.update_ui() 

    def update_ui(self):
        self.oweis.setText(f"Oweis: {self.counts['oweis']}")
        self.sokary.setText(f"Sokary: {self.counts['sokary']}")
        self.apples.setText(f"Apples: {self.counts['Apples']}")
        self.bananas.setText(f"Bananas: {self.counts['Bananas']}")
        self.guavas.setText(f"Guavas: {self.counts['Guavas']}")
        self.label.setText(f"Total Cost: {self.price:} EGP")

app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec() 