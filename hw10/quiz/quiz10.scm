(define (how-many-dots s)
  (cond
   ((null? s) 0)
   ((number? s) 0)
   ((and (pair? s) (number? (car s)) (null? (cdr s))) 0) 
   ((and (pair? s) (number? (car s)) (number? (cdr s))) 1) 
   ((and (pair? s) (number? (car s)) (pair? (cdr s))) (how-many-dots (cdr s)))
   ((and (pair? s) (pair? (car s)) (pair? (cdr s))) 
                            (+ (how-many-dots (car s)) (how-many-dots (cdr s))))
   ((and (pair? s) (pair? (car s)) (null? (cdr s))) (how-many-dots (car s)))
   ((and (pair? s) (pair? (car s)) (number? (cdr s))) (+ (how-many-dots (car s)) 1))
   )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7)))))))
; expect 0