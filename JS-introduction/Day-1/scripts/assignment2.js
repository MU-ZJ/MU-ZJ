class Account {
  constructor(firstName, lastName, middleName, accountType, balance, status) {
    this.firstName = null;
    this.lastName = null;
    this.middleName = null;
    this.accountType = null;
    this.balance = 0;
    this.status = "Closed";
    this.accounts = [];
    this.accountDetails = {};
  }

  openAccount() {
    this.firstName = prompt("First name");
    this.lastName = prompt("Last name");
    this.middleName = prompt("Middle name");
    this.accountType = prompt("Account type");
    this.balance = parseFloat(prompt("Enter initial balance"));
    if (this.balance >= 100) {
      this.accountDetails = {
        firstName: this.firstName,
        lastName: this.lastName,
        middleName: this.middleName,
        accountType: this.accountType,
        balance: this.balance,
        status: "Open",
      };
      this.accounts.push(this.accountDetails);
      this.menu();
    } else
      console.log("A deposit of $100 or more is required to open an account");
    this.menu();
  }

  menu() {
    this.freezeAccount();
    this.selection = prompt(
      "Press 1 to open an account \nPress 2 to view account \n Press 3 to close account \nPress q to quit"
    );
    if (this.selection == "1") {
      this.openAccount();
    } else if (this.selection == "2") {
      this.viewAccount();
    } else if (this.selection == "3") {
      this.closeAccount();
    } else if (this.selection == "q") {
      throw new Error("Exiting");
    }
  }

  viewAccount() {
    this.freezeAccount();
    console.log(this.accounts);
    this.accountSelection = prompt("Select an account, or enter q to quit");
    if (this.accountSelection == "q") {
      this.menu();
    } else this.selectedAccount = parseInt(this.accountSelection);
    this.options = prompt(
      "Press 1 to deposit \nPress 2 to withdraw \nPress 3 to transfer funds \nPress q to quit"
    );
    if (this.options == "q") {
      this.menu();
    } else if (this.options == "1") {
      this.depositAmount = parseInt(prompt("Enter amount to deposit"));
      this.accounts[this.selectedAccount - 1].balance =
        this.accounts[this.selectedAccount - 1].balance + this.depositAmount;
      console.log(this.accounts[this.selectedAccount - 1]);
      this.freezeAccount();
      this.viewAccount();
    } else if (
      this.options == "2" &&
      this.accounts[this.selectedAccount - 1].status != "Frozen"
    ) {
      this.withdrawAmount = parseInt(prompt("Enter amount to withdraw"));
      this.accounts[this.selectedAccount - 1].balance =
        this.accounts[this.selectedAccount - 1].balance - this.withdrawAmount;
      if (this.accounts[this.selectedAccount - 1].balance <= 0) {
        this.accounts[this.selectedAccount - 1].balance -= 35;
        console.log(this.accounts[this.selectedAccount - 1]);
        this.viewAccount();
      } else console.log(this.accounts[this.selectedAccount - 1]);
      this.viewAccount();
    } else if (
      this.options == "3" &&
      this.accounts[this.selectedAccount - 1].status != "Frozen"
    ) {
      this.targetAccount = parseInt(prompt("Enter target account"));
      this.transferAmount = parseInt(prompt("Enter amount to transfer"));
      this.accounts[this.targetAccount - 1].balance =
        this.accounts[this.targetAccount - 1].balance + this.transferAmount;
      this.accounts[this.selectedAccount - 1].balance =
        this.accounts[this.selectedAccount - 1].balance - this.transferAmount;
    } else console.log("Invalid Input, or account is frozen");
    this.viewAccount();
  }

  closeAccount() {
    this.closureSelection = prompt(
      "Enter an account to close, or press q to quit"
    );
    if (this.closureSelection == "q") {
      this.menu();
    } else this.deleteSelection = parseInt(this.closureSelection - 1);
    this.accounts.splice(this.deleteSelection, this.deleteSelection);
    this.menu();
  }

  freezeAccount() {
    for (let item of this.accounts) {
      if (item["balance"] <= 0) {
        item["status"] = "Frozen";
      } else if (item["balance"] >= 0) {
        item["status"] = "Open";
      } else return;
    }
  }
}

let account = new Account();

account.menu();
