from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Knowledge that Character might be Knight or Knave but not both
def KnightOrKnave(X,Y):
    return And(Or(X , Y), Not(And(X,Y)))

# Knowledge that Character statement might be true or false
def True_or_False(Char , Statement):
    knight = f"{Char}Knight"
    knave = f"{Char}Knave"

    Knight = globals().get(knight)
    Knave = globals().get(knave)

    return And(
    Implication(Knight , Statement),
    Implication(Knave , Not(Statement))
    )

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    KnightOrKnave(AKnight,AKnave),
    True_or_False("A" , And(AKnight,AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    KnightOrKnave(AKnight,AKnave),
    KnightOrKnave(BKnight,BKnave),

    True_or_False("A", And(AKnave,BKnave))
)

# Puzzle 2
# A says "We are the same kind."~
# B says "We are of different kinds."
knowledge2 = And(
    KnightOrKnave(AKnight,AKnave),
    KnightOrKnave(BKnight,BKnave),

    True_or_False("A" , Or(And(AKnight,BKnight) , And(AKnave, BKnave))),
    True_or_False("B" , Or(And(AKnight,BKnave) , And(AKnave, BKnight)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    KnightOrKnave(AKnight,AKnave),
    KnightOrKnave(BKnight,BKnave),
    KnightOrKnave(CKnight,CKnave),

    True_or_False("C" , AKnight),
    True_or_False("B" , CKnave),
    True_or_False("B" , True_or_False("A" , AKnave)),
    True_or_False("A" , Or(AKnight,AKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
