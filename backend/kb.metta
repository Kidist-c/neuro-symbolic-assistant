;; Define cast functions between Nat and Number

(= (fromNumber $n) (if (<= $n 0) Z (S (fromNumber (- $n 1)))))

;; Knowledge base
!(bind! &kb (new-space))
                     
!(add-reduct &kb (superpose ((get-atoms &temp1))))
!(add-reduct &kb (superpose ((get-atoms &temp2))))

;; Base case
(= (backward-chain $kb $_ (: $prf $ccln)) (match $kb (: $prf $ccln) (: $prf $ccln)))

;; Recursive step
(= (backward-chain $kb (S $k) (: ($prfabs $prfarg) $ccln))
   (let* (((: $prfabs (-> $prms $ccln)) (backward-chain $kb $k (: $prfabs (-> $prms $ccln))))
          ((: $prfarg $prms) (backward-chain $kb $k (: $prfarg $prms))))
     (: ($prfabs $prfarg) $ccln)))

;; Forward DTL Curried
(: forward-chain (-> $a                            ; Knowledge base space
           Nat                           ; Maximum depth
           $b                            ; Source
           $b))                          ; Conclusion

;; Base case
(= (forward-chain $kb $_ (: $prf $prms)) (: $prf $prms))

;; Recursive step
(= (forward-chain $kb (S $k) (: $prfarg $prms))
   (let (: $prfabs (-> $prms $ccln)) (backward-chain $kb $k (: $prfabs (-> $prms $ccln)))
     (forward-chain $kb $k (: ($prfabs $prfarg) $ccln))))
(= (forward-chain $kb (S $k) (: $prfabs (-> $prms $ccln)))
    (let (: $prfarg $prms) (backward-chain $kb $k (: $prfarg $prms))
     (forward-chain $kb $k (: ($prfabs $prfarg) $ccln))))


!(forward-chain &kb (fromNumber 2) (: FACT1 (has_parent John Mary)))