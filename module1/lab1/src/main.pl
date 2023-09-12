%---  База знаний (набор предикатов, факты)

%-  линия Аудиторе
parent("Dominico Auditore", "Renato Auditore").
parent("Renato Auditore", "Giovanni's father Auditore").
parent("Giovanni's father Auditore", "Giovanni Auditore da Firenze").
parent("Giovanni Auditore da Firenze", "Ezio Auditore da Firenze").
parent("Maria de'Mozzi da Firenze", "Ezio Auditore da Firenze").
parent("Ezio Auditore da Firenze", "Flavia Auditore").
parent("Sofia Sartor", "Flavia Auditore").
parent("Flavia Auditore", "William's Father Miles").

%-  линия Кенуэй
parent("Linette Hopkins", "Edward Kenway").
parent("Bernard Kenway", "Edward Kenway").
parent("Edward Kenway", "Haytham E. Kenway").
parent("Tessa Stephenson-Oakley", "Haytham E. Kenway").
parent("Haytham E. Kenway", "Ratonhnhaké:ton Connor Kenway").
parent("Kanieht:io", "Ratonhnhaké:ton Connor Kenway").
parent("Ratonhnhaké:ton Connor Kenway", "William's Mother Miles").

%-  линии Аудиторе + Кенуэй
parent("William's Father Miles", "William Miles").
parent("William's Mother Miles", "William Miles").

%-  линия Альтаира
parent("Umar Ibn-La'Ahad", "Altaïr Ibn-La'Ahad").
parent("Maud", "Altaïr Ibn-La'Ahad").
parent("Altaïr Ibn-La'Ahad", "Sef Ibn-La'Ahad").
parent("Maria Thorpe", "Sef Ibn-La'Ahad").
parent("Sef Ibn-La'Ahad", "Sef's Daughter (1) Ibn-La'Ahad").
parent("Sef's wife (Ibn-La'Ahad)", "Sef's Daughter (1) Ibn-La'Ahad").
parent("Sef's Daughter (1) Ibn-La'Ahad", "Mother of Desmond Miles").

%-  линии Аудиторе + Кенуэй + Альтаира
parent("William Miles", "Subject 17 Desmond Miles").
parent("Mother of Desmond Miles", "Subject 17 Desmond Miles").

%-  мужчины
man("Dominico Auditore").
man("Renato Auditore").
man("Giovanni's father Auditore").
man("Giovanni Auditore da Firenze").
man("Ezio Auditore da Firenze").
man("William's Father Miles").
man("William Miles").
man("Subject 17 Desmond Miles").
man("Bernard Kenway").
man("Edward Kenway").
man("Haytham E. Kenway").
man("Ratonhnhaké:ton Connor Kenway").
man("Umar Ibn-La'Ahad").
man("Altaïr Ibn-La'Ahad").
man("Sef Ibn-La'Ahad").


%-  девушки
woman("Maria de'Mozzi da Firenze").
woman("Sofia Sartor").
woman("Flavia Auditore").
woman("Linette Hopkins").
woman("Tessa Stephenson-Oakley").
woman("Kanieht:io").
woman("William's Mother Miles").
woman("Maud").
woman("Maria Thorpe").
woman("Sef's wife (Ibn-La'Ahad)").
woman("Sef's Daughter (1) Ibn-La'Ahad").
woman("Mother of Desmond Miles").

%-  навык
mage("Dominico Auditore").
pirate("Bernard Kenway").
assassin("Umar Ibn-La'Ahad").

%-  супруги
spouse("Giovanni Auditore da Firenze", "Maria de'Mozzi da Firenze").
spouse("Ezio Auditore da Firenze", "Sofia Sartor").
spouse("Linette Hopkins", "Bernard Kenway").
spouse("Edward Kenway", "Tessa Stephenson-Oakley").
spouse("Haytham E. Kenway", "Kanieht:io").
spouse("William's Mother Miles", "William's Father Miles").
spouse("Mother of Desmond Miles", "William Miles").
spouse("Umar Ibn-La'Ahad", "Maud").
spouse("Maria Thorpe", "Altaïr Ibn-La'Ahad").
spouse("Sef Ibn-La'Ahad", "Sef's wife (Ibn-La'Ahad)").

%---  правила

spouse(X, Y)        :- spouse(Y, X), X \= Y.

son(X, Y)           :- parent(Y, X), !, man(X).
daughter(X, Y)      :- parent(Y, X), !, woman(X).
mom(X, Y)           :- parent(X, Y), woman(X).
dad(X, Y)           :- parent(X, Y), man(X).
grandfather(X, Y)   :- parent(Z, Y), parent(X, Z), man(X).
grandmother(X, Y)   :- parent(Z, Y), parent(X, Z), woman(X).

isMage(X)           :- mage(X); parent(Y, X), isMage(Y).
isPirate(X)         :- pirate(X); parent(Y, X), isPirate(Y).
isAssassin(X)       :- assassin(X); parent(Y, X), isAssassin(Y).
