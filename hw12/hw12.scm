(define (find s predicate)
  (cond
   ((null? s) #f)
   ((predicate (car s)) (car s))
   (else (find (cdr-stream s) predicate))
   )
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
  (define (cycle-tracker so-far cur)
   (cond
    ((null? cur) #f)
    ((contains so-far cur) #t)
    (else (cycle-tracker (cons cur so-far) (cdr-stream cur)))
    )
  )
  (cycle-tracker nil s)
)
   

(define (contains lst s)
  (cond
   ((null? lst) #f)
   ((eq? s (car lst)) #t)
   (else (contains (cdr lst) s))
  )
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
