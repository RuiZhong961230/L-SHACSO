# import packages
import os
from cec17_functions import cec17_test_func
import numpy as np
from copy import deepcopy


DimSize = 100
PopSizeMax = 400
PopSizeMin = 4
PopSize = PopSizeMax
LB = [-100] * DimSize
UB = [100] * DimSize
TrialRuns = 30
MaxFEs = 1000 * DimSize

Pop = np.zeros((PopSize, DimSize))
Velocity = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)
curFEs = 0
FuncNum = 1
HistorySize = 5
mu_phi = np.array([0.1] * HistorySize)


def meanL(arr):
    numer = 0
    denom = 0
    for var in arr:
        numer += var ** 2
        denom += var
    return numer / denom


def fitness(X):
    global DimSize, FuncNum
    f = [0]
    cec17_test_func(X, f, DimSize, 1, FuncNum)
    return f[0]


# initialize the M randomly
def Initialization():
    global Pop, Velocity, FitPop, PopSize, PopSizeMax, mu_phi, HistorySize
    PopSize = PopSizeMax
    Pop = np.zeros((PopSize, DimSize))
    FitPop = np.zeros(PopSize)
    Velocity = np.zeros((PopSize, DimSize))
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = fitness(Pop[i])
    mu_phi = np.array([0.3] * HistorySize)


def Check(indi):
    global LB, UB
    for i in range(DimSize):
        range_width = UB[i] - LB[i]
        if indi[i] > UB[i]:
            n = int((indi[i] - UB[i]) / range_width)
            mirrorRange = (indi[i] - UB[i]) - (n * range_width)
            indi[i] = UB[i] - mirrorRange
        elif indi[i] < LB[i]:
            n = int((LB[i] - indi[i]) / range_width)
            mirrorRange = (LB[i] - indi[i]) - (n * range_width)
            indi[i] = LB[i] + mirrorRange
        else:
            pass
    return indi


def LSHACSO():
    global Pop, Velocity, FitPop, PopSize, curFEs, mu_phi

    sequence = list(range(PopSize))
    np.random.shuffle(sequence)
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)
    Xmean = np.mean(Pop, axis=0)
    Success_phi = []
    r1 = np.random.randint(HistorySize)
    for i in range(int(PopSize / 2)):
        idx1 = sequence[2 * i]
        idx2 = sequence[2 * i + 1]

        if FitPop[idx1] < FitPop[idx2]:
            Off[idx1] = deepcopy(Pop[idx1])
            FitOff[idx1] = FitPop[idx1]

            phi = np.clip(np.random.normal(mu_phi[r1], 0.1, DimSize), 0.001, 0.5)
            Velocity[idx2] = np.random.rand(DimSize) * Velocity[idx2] + np.random.rand(DimSize) * (Pop[idx1] - Pop[idx2]) + phi * (Xmean - Pop[idx2])
            Off[idx2] = Pop[idx2] + Velocity[idx2]
            Off[idx2] = Check(Off[idx2])
            FitOff[idx2] = fitness(Off[idx2])
            curFEs += 1
            if FitOff[idx2] < FitPop[idx2]:
                Success_phi.append(np.mean(phi))
        else:
            Off[idx2] = deepcopy(Pop[idx2])
            FitOff[idx2] = FitPop[idx2]

            phi = np.clip(np.random.normal(mu_phi[r1], 0.1, DimSize), 0.001, 0.5)
            Velocity[idx1] = np.random.rand(DimSize) * Velocity[idx1] + np.random.rand(DimSize) * (Pop[idx2] - Pop[idx1]) + phi * (Xmean - Pop[idx1])
            Off[idx1] = Pop[idx1] + Velocity[idx1]
            Off[idx1] = Check(Off[idx1])
            FitOff[idx1] = fitness(Off[idx1])
            curFEs += 1
            if FitOff[idx1] < FitPop[idx1]:
                Success_phi.append(np.mean(phi))

    PopSize = round(((PopSizeMin - PopSizeMax) / MaxFEs * curFEs + PopSizeMax))
    if PopSize % 2 == 1:
        PopSize += 1

    c = 0.1
    if len(Success_phi) > 0:
        mu_phi[r1] = (1-c) * mu_phi[r1] + c * meanL(Success_phi)

    PopSize = max(PopSize, PopSizeMin)
    sorted_idx = np.argsort(FitOff)
    Pop = deepcopy(Off[sorted_idx[0:PopSize]])
    FitPop = deepcopy(FitOff[sorted_idx[0:PopSize]])


def RunLSHACSO():
    global FitPop, curFEs, TrialRuns, DimSize
    All_Trial = []
    for i in range(TrialRuns):
        BestList = []
        curFEs = 0
        np.random.seed(1996 + 20 * i)
        Initialization()
        BestList.append(min(FitPop))
        while curFEs < MaxFEs:
            LSHACSO()
            BestList.append(min(FitPop))
        All_Trial.append(BestList)
    np.savetxt("./LSHACSO_Data/CEC2017/F" + str(FuncNum) + "_" + str(Dim) + "D.csv", All_Trial, delimiter=",")


def main(dim):
    global FuncNum, DimSize, MaxFEs, Pop, LB, UB
    DimSize = dim
    Pop = np.zeros((PopSize, dim))
    MaxFEs = dim * 1000
    LB = [-100] * dim
    UB = [100] * dim

    for i in range(1, 31):
        if i == 2:
            continue
        FuncNum = i
        RunLSHACSO()


if __name__ == "__main__":
    if os.path.exists('./LSHACSO_Data/CEC2017') == False:
        os.makedirs('./LSHACSO_Data/CEC2017')
    Dims = [30, 50]
    for Dim in Dims:
        main(Dim)