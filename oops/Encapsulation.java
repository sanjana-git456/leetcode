class BankAccount {
    private int balance;

    BankAccount() {
        this.balance = 0;
    }

    void deposit(int amount) {
        balance = balance + amount;
    }

    void withdraw(int amount) {
        if (balance > amount) {
            balance = balance - amount;
        } else {
            System.out.println("Insufficient funds");
        }
    }

    int getBalance() {
        return balance;
    }
}

public class Encapsulation {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount();
        acc.deposit(1000);
        acc.withdraw(500);
        System.out.println(acc.getBalance());
    }
}