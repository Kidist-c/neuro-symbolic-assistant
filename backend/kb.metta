;; ---------- CREATE KNOWLEDGE BASE ----------

!(bind! &kb (new-space))

;; ---------- LOAD FACTS ----------
!(add-reduct &kb
    (superpose (
        (Parent Chandler Pam)
        (Parent Chandler Adem)
        (Parent Chandler Jane)

        (Parent Monica John)
        (Parent Monica Pam)
        (Parent Monica Adem)
        (Parent Monica Jane)

        (Parent John Bob)

        (Parent Pam Tim)
        (Parent Pam Kim)

        (Parent Adam Eve)

        (Parent Jane Joe)

        (Male Chandler)
        (Male John)
        (Male Bob)
        (Male Joe)
        (Male Tim)
        (Male Adam)

        (Female Pam)
        (Female Monica)
        (Female Kim)
        (Female Eve)
        (Female Jane)
    ))
)

;; ---------- LOAD RULES ----------
!(add-reduct &kb
    (superpose (
        child-rule
        sibling-rule
        grandparent-rule
        greatgrandparent-rule
        grandfather-rule
        grandmother-rule
        uncle-rule
        aunt-rule
        cousin-rule
    ))
)