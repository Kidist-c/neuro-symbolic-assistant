;; =============================
;; Family Rules
;; =============================

;; Child Rule: infer child from parent
(: child_rule
   (-> (has_parent $parent $child)
       (has_child $child $parent))
)

;; Sibling Rule: infer siblings from shared parent
(: sibling_rule
   (-> (has_parent $p $x)
       (-> (has_parent $p $y)
           (-> (not (= $x $y))
               (has_sibling $x $y)
           )
       )
   )
)

;; Grandparent Rule
(: grandparent_rule
   (-> (has_parent $x $y)
       (-> (has_parent $y $z)
           (has_grandparent $x $z)
       )
   )
)

;; Cousin Rule: children of siblings are cousins
(: cousin_rule
   (-> (has_sibling $p1 $p2)
       (-> (has_parent $p1 $c1)
           (-> (has_parent $p2 $c2)
               (has_cousin $c1 $c2)
           )
       )
   )
)

;; Spouse Rule: married relationship is bidirectional
(: spouse_rule
   (-> (has_married $x $y)
       (has_spouse $y $x))
)

;; =============================
;; Employment Rules
;; =============================

;; Unemployed inference: if not employed, considered unemployed
(: unemployed_rule
   (-> (not (has_employed $x))
       (has_unemployed $x))
)

;; =============================
;; Personality & Social Status Rules
;; =============================

;; Extrovert rule: if married, may influence social connections (example inference)
(: social_influence_rule
   (-> (has_married $x $y)
       (-> (has_personality_extrovert $x)
           (has_social_network_expanded $y)
       )
   )
)

;; Age group rule: define adult or minor
(: adult_rule
   (-> (has_age $x ?age)
       (-> (> ?age 18)
           (has_age_group_adult $x)
       )
   )
)

(: minor_rule
   (-> (has_age $x ?age)
       (-> (<= ?age 18)
           (has_age_group_minor $x)
       )
   )
)

;; Education level inference: higher education implies employed potential
(: education_employment_rule
   (-> (has_education_college $x)
       (has_employment_potential $x))
)

(: education_employment_rule2
   (-> (has_education_university $x)
       (has_employment_potential $x))
)

;; =============================
;; Location & Hobbies (optional reasoning)
;; =============================

;; Shared city implies potential social connection
(: city_connection_rule
   (-> (has_city $x $city)
       (-> (has_city $y $city)
           (has_possible_connection $x $y)
       )
   )
)

;; Shared hobbies imply potential social connection
(: hobby_connection_rule
   (-> (has_hobby $x $hobby)
       (-> (has_hobby $y $hobby)
           (has_hobby_connection $x $y)
       )
   )
)