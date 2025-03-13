class Payment:
    @staticmethod
    def process_payment(amount, method="cash"):
        return f"Payment of {amount} processed via {method}"