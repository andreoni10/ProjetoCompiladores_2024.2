# Generated from Expressoes.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressoesParser import ExpressoesParser
else:
    from ExpressoesParser import ExpressoesParser

# This class defines a complete listener for a parse tree produced by ExpressoesParser.
class ExpressoesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressoesParser#prog.
    def enterProg(self, ctx:ExpressoesParser.ProgContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#prog.
    def exitProg(self, ctx:ExpressoesParser.ProgContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#stmt.
    def enterStmt(self, ctx:ExpressoesParser.StmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#stmt.
    def exitStmt(self, ctx:ExpressoesParser.StmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#createStmt.
    def enterCreateStmt(self, ctx:ExpressoesParser.CreateStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#createStmt.
    def exitCreateStmt(self, ctx:ExpressoesParser.CreateStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#selectStmt.
    def enterSelectStmt(self, ctx:ExpressoesParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#selectStmt.
    def exitSelectStmt(self, ctx:ExpressoesParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#insertStmt.
    def enterInsertStmt(self, ctx:ExpressoesParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#insertStmt.
    def exitInsertStmt(self, ctx:ExpressoesParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#updateStmt.
    def enterUpdateStmt(self, ctx:ExpressoesParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#updateStmt.
    def exitUpdateStmt(self, ctx:ExpressoesParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#deleteItemStmt.
    def enterDeleteItemStmt(self, ctx:ExpressoesParser.DeleteItemStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#deleteItemStmt.
    def exitDeleteItemStmt(self, ctx:ExpressoesParser.DeleteItemStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#deleteTableStmt.
    def enterDeleteTableStmt(self, ctx:ExpressoesParser.DeleteTableStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#deleteTableStmt.
    def exitDeleteTableStmt(self, ctx:ExpressoesParser.DeleteTableStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#clearStmt.
    def enterClearStmt(self, ctx:ExpressoesParser.ClearStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#clearStmt.
    def exitClearStmt(self, ctx:ExpressoesParser.ClearStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#showStmt.
    def enterShowStmt(self, ctx:ExpressoesParser.ShowStmtContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#showStmt.
    def exitShowStmt(self, ctx:ExpressoesParser.ShowStmtContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#columns.
    def enterColumns(self, ctx:ExpressoesParser.ColumnsContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#columns.
    def exitColumns(self, ctx:ExpressoesParser.ColumnsContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#values.
    def enterValues(self, ctx:ExpressoesParser.ValuesContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#values.
    def exitValues(self, ctx:ExpressoesParser.ValuesContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#assignments.
    def enterAssignments(self, ctx:ExpressoesParser.AssignmentsContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#assignments.
    def exitAssignments(self, ctx:ExpressoesParser.AssignmentsContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#assignment.
    def enterAssignment(self, ctx:ExpressoesParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#assignment.
    def exitAssignment(self, ctx:ExpressoesParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#condition.
    def enterCondition(self, ctx:ExpressoesParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#condition.
    def exitCondition(self, ctx:ExpressoesParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#value.
    def enterValue(self, ctx:ExpressoesParser.ValueContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#value.
    def exitValue(self, ctx:ExpressoesParser.ValueContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#table.
    def enterTable(self, ctx:ExpressoesParser.TableContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#table.
    def exitTable(self, ctx:ExpressoesParser.TableContext):
        pass



del ExpressoesParser