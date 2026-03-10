;; child rule
(: child-rule
   (-> (Parent $y $x)
      (child $x $y))
)

;; sibling rule
(: sibling-rule
  (-> (Parent $p $x)
       (-> (Parent $p $y)
           (-> (not (= $x $y))
               (sibling $x $y)
           )
       )
   )
)

;; grandparent rule
(: grandparent-rule
   (-> (Parent $x $y)
       (-> (Parent $y $z)
           (grandparent $x $z)
       )
   )
)
;;
great grandparent rule
(: greatgrandparent-rule
  (-> (Parent $x $y)
    (-> (grandparent $y $z)
      (greatgrantparent $x $z)
      )
    )
)

;; grandfather rule
( : grandfather-rule 
  (-> (grandparent $x $y)
    (-> (Male $x)
      (grandfather $x $y)
      )
    )
)
;; grandmother rule
( : grandmother-rule 
  (-> (grandparent $x $y)
    (-> (Female $x)
      (grandmother $x $y)
      )
    )
)
;; uncle rule
(: uncle-rule 
  (-> (sibling $x $y)
    (-> (Parent $x $z)
      (-> (Male $y)
        (uncle $y $z)
       )
    )
)
)
;;aunt rule
(: aunt-rule 
  (->(sibling $x $y)
    (-> (Parent $x $z)
      (-> (Female $y)
        (aunt $y $z)
        )
      )
    )
)

;; cousin rule
(: cousin-rule 
  (-> (Parent $p1 $y)
    (-> (Parent $p2 $x)
      (->(sibling $p1 $p2)
        (cousin $y $x)
        )
    )
))