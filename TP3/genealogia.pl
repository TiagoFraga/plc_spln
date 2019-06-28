%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% SIST. REPR. CONHECIMENTO E RACIOCINIO - MiEI/3

%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% Invariantes

%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% SICStus PROLOG: Declaracoes iniciais

cleanup_db :-
      retractall(filho(_)).
cleanup_db :-
      retractall(pai(_)).
cleanup_db :-
      retractall(neto(_)).
cleanup_db :-
      retractall(avo(_)).

:- set_prolog_flag( discontiguous_warnings,off ).
:- set_prolog_flag( single_var_warnings,off ).


%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% SICStus PROLOG: definicoes iniciais

go :-
    call_cleanup(go_with_clean_db, cleanup_db).

:- op( 900,xfy,'::' ).
:- dynamic filho/1.
:- dynamic pai/1.
:- dynamic neto/1.
:- dynamic avo/1.


%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% Extensao do predicado filho: Filho,Pai -> {V,F,D}

filho( joao,jose ).
filho( jose,manuel ).
filho( carlos,jose ).

% Invariante Estrutural:  nao permitir a insercao de conhecimento
%                         repetido

+filho( F,P ) :: (solucoes( (F,P),(filho( F,P )),S ),
                  comprimento( S,N ), 
				  N == 1
                  ).
+pai( P,F ) :: (solucoes( ( P,F ),(pai( P,F )), S),
				comprimento( S,N ),
				N == 1
				). 

+neto( N,A ) :: (solucoes( ( N,A ),(neto( N,A )), S),
				comprimento( S,N ),
				N == 1
				).

+avo( A,N ) :: (solucoes( ( A,N ),(avo( A,N )),S),
				comprimento( S,N ),
				N == 1
				).

% Invariante Referencial: nao admitir mais do que 2 progenitores
%                         para um mesmo individuo

+filho( F,P ) :: ( solucoes( (Ps) , (filho( F,PS)),S),
					comprimento( S,N),
					N =<2 ).

%--------------------------------- - - - - - - - - - -  -  -  -  -   -
% Extensão do predicado que permite a evolucao do conhecimento


insercao(T) :-
			assert(T).
insercao(T) :-
			retract(T), !,fail.

solucoes( X,Y,Z ) :- findall( X,Y,Z ).

comprimento([], L) :-
	L is 0.
comprimento([H|T], L) :-
	comprimento(T, R),
	L is 1+R.

testar([]).
testar([I|L]) :- I,testar(L).

evolucao(F) :- 
			solucoes(I, +F :: I,Li) ,  
			insercao(F),
			testar(Li).

