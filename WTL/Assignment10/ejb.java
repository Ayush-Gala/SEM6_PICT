package Assignment10;

@Entity
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long transactionId;
    private long accountId;
    private String transactionType;
    private double amount;
    // constructors, getters, and setters
}

@Stateless
public class TransactionManagerBean implements
        TransactionManagerRemote {
    @PersistenceContext(unitName = "bank")
    private EntityManager entityManager;

    public void deposit(long accountId, double amount) {
        Account account = entityManager.find(Account.class, accountId);
        double newBalance = account.getBalance() + amount;
        account.setBalance(newBalance);
        entityManager.persist(account);

        Transaction transaction = new Transaction(accountId, "deposit", amount);
        entityManager.persist(transaction);
    }

    public void withdraw(long accountId, double amount) throws InsufficientFundsException {
        Account account = entityManager.find(Account.class, accountId);
        double newBalance = account.getBalance() - amount;

        if (newBalance < 0) {
            throw new InsufficientFundsException();
        }

        account.setBalance(newBalance);
        entityManager.persist(account);

        Transaction transaction = new Transaction(accountId, "withdraw", amount);
        entityManager.persist(transaction);
    }

    public List<Transaction> getTransactionHistory(long accountId) {
        TypedQuery<Transaction> query = entityManager.createQuery(
                "SELECT t FROM Transaction t WHERE t.accountId = :accountId", Transaction.class);
        query.setParameter("accountId", accountId);
        return query.getResultList();
    }
}

public class TransactionServlet extends HttpServlet {
    @EJB
    private TransactionManagerRemote transactionManager;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        long accountId = Long.parseLong(request.getParameter("accountId"));
        List<Transaction> transactions = transactionManager.getTransactionHistory(accountId);
        request.setAttribute("transactions", transactions);
        request.getRequestDispatcher("transaction_history.jsp").forward(request, response);
    }

protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
{
    long accountId = Long.parseLong(request.getParameter("accountId"));
    double amount = Double.parseDouble(request.getParameter("amount"));

    String action = request.getParameter("action");
    String message = "";

    if (action.equals("deposit")) {
        transactionManager.deposit(accountId, amount); message = "Deposit successful";
    }
    else if (action.equals("withdraw")) {
        boolean success = transactionManager.withdraw(accountId, amount);
            if (success) { message = "Withdrawal successful";
            } else {
                message = "Insufficient funds";
            }
    }

    request.setAttribute("message", message);
    doGet(request, response);
    }
}