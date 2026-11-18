# proof:

I assume that sum_nested returns the sum of the integers in list nested if nested has maximum depth k.

Let nested by an arbitrary list composed of integers and nested lists of depth k.

---

Claim: P(nested) is "if nested is a recursively defined nested list of integers, then sum_nested(nested) is the sum of all the integers in nested."

We will use structural induction to prove this claim. We will perform induction on the depth (k) of the list

We will use structural induction to prove this claim.

Base case (k=0): nested is a list of depth 0. It contains only integers

Then, sum_nested returns total, and total is the sum of all the items in nested. So sum_nested(nested) returns the sum of all the integers in nested.

Inductive case: We assume that sum_nested() returns the sum of the integers in a nested list of depth k. A nested list of depth k contains integers or nested lists of depth k - 1.

Now, let nested be an arbitrary nested list of depth k + 1.
It is composed of integers and nested lists of depth k.

Then, sum_nested(nested) = v1 + v2 + .. vm where vi is either an integer or sum_nested(vi).

Case 1: vi is an integer
vi is added to the sum.

Case 2: vi is a nested list
sum_nested(vi) is added to the sum. vi is a nested list of depth k, so by the inductive hypothesis, it returns the sum of the integers in vi.

As a result, we always add the sum of the integers in vi, so sum_nested(nested) is the sum of all the integers in nested.

By the principle of induction, since the case for a flat list works and we have shown that an arbitrarily nested list of depth k+1 holds if a list of depth k holds, then sum_nested returns the sum of the integers in any arbitrary nested list.
