(define (square x) (* x x))

(define (good_enough guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (sqrt_iter guess x)
  (if (good_enough guess x)
      guess
      (sqrt_iter (improve guess x)
                 x)))

(define (sqrt x)
  (sqrt_iter 1.0 x))

(display (sqrt 10))
