class Account {
    constructor(balance, accountType) {
        this.balance = 0
        this.accountType = null
    }

    createAccount() {
        this.balance = parseInt(prompt('Enter starting balance'))
        this.accountType = prompt('Enter account type')
    }

    deposit() {
        return this.balance + parseInt(prompt('Enter amount to deposit'))
    }

    withdraw() {
        return this.balance - parseInt(prompt('Enter amount to withdraw'))
    }

    showBalance() {
        console.log(this.accountType, this.balance)
    }
}

let account = new Account()
account.createAccount()
account.deposit()
account.withdraw()
account.showBalance()