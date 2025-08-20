

class Bankaccount1 {
    private String accountNumber;
    private String accountName;
    private double balance;

    public Bankaccount1(String accountNumber, String accountName) {
        this.accountNumber = accountNumber;
        this.accountName = accountName;
        this.balance = 0.0; // Initial balance is set to zero
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAccountName() {
        return accountName;
    }

    public double getbalance() {
        return balance;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            balance = balance + amount;
            return true;
        } else {
            return false;
        }
    }

    public boolean withdraw(double amount) {
        if (amount > balance) {
            return false; // insufficient funds
        } else {
            balance = balance - amount;
            return true;
        }
    }
}

class SavingsAccount extends Bankaccount1 {
    private double interestRate;

    public SavingsAccount(String accountNumber, String accountName, double interestRate) {
        super(accountNumber, accountName);
        this.interestRate = interestRate;
    }

    public double addInterest() {
        double interest = getbalance() * interestRate / 100;
        deposit(interest);
        return interest;
    }
}

public class Bankaccount {
    public static void main(String[] args) {
        Bankaccount1 bank = new Bankaccount1("123", "John Doe");
        bank.deposit(1000);
        System.out.println("Account Number: " + bank.getAccountNumber());
        System.out.println("Account Name: " + bank.getAccountName());
        System.out.println("Balance: " + bank.getbalance());

        bank.withdraw(500);
        System.out.println("Balance after withdrawal: " + bank.getbalance());

        bank.deposit(200);
        System.out.println("Balance after deposit: " + bank.getbalance());

        SavingsAccount savings = new SavingsAccount("456", "Jane Doe", 5.0);
        savings.deposit(1000);
        System.out.println("Savings Account Number: " + savings.getAccountNumber());
        System.out.println("Savings Account Name: " + savings.getAccountName());
        System.out.println("Savings Balance: " + savings.getbalance());

        double interest = savings.addInterest();
        System.out.println("Interest added: " + interest);
        System.out.println("Savings Balance after interest: " + savings.getbalance());
    }
}
