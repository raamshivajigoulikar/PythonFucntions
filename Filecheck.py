def chkvars(chkData, chkVarNames, chkDataType):
    """
    :param chkData: The name of the dataset that contains the variable to be checked
    :param chkVarNames: A space delimited list of variables to check for specified dataset
    :param chkDataType: The expected data type, N for numeric and C for char
    :return:
    """
    chkvars = None
    hasVar = 0
    dsid = chkData
    varnum = None
    varCnt = None
    chkVarName = None
    vartype = None
    chektype = eval(chkDataType)[0].upper()
    chki = None

    # Double check to ensure the data type value is captured correctly

    chektype = upper(str(chkDataType, 1,1))
if dsid:
    #Determine the count of variables supplied to the macro
    varCnt = len(chkVarNames)
    for chki in varCnt:
        curChkName = chkVarNames[chki]
        varnum = bool(curChkName in dsid)
        if varnum:
            vartype = vartpe(dsid, varnum)
            #confirm that vartype resolves to true
            if (vartype==chektype) or (X==chektype):
                print("NOte: The variable" + curChkName + "was found in the dataset" + chkData)
                hasVar = 0
            else:
                print("WARNING: The variable" + curChkName + "was not found in the dataset" + chkData)
                hasVar = 1
                finish_chkErr(hasVar)
        else:
            print("WARNING: The variable" + curChkName + "was not found int he dataset" + chkData)
            hasVar = 1
            finish_chkErr(hasVar)
            #Close the dataset
def finish_chkErr(hasVar):
    #Set the return value chkVars to the value of hasVar
    chkvars = hasVar
    #Check the value of the chkVars and set the error_flag to YES if the variable was not found
    if chkvars[0] == 0:
        print("NOTE:" + (chki-1) + "total varialbes were found successfully in the target dataset" + chkData)
    else:
        print("WARNING: At least one variable was not found and execution has passed back to the calling program")
    #return the value of chkVars as if the chkVars was a function
    return chkvars

