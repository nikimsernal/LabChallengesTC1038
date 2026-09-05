def compute_PPV(sens, spec, inci):
    ppv = (inci * sens) / ((inci * sens) + ((1 - inci) * (1 - spec)))
    return ppv

def main():
    sensitivity = float(input())
    specificity = float(input())
    incidence = float(input())

    print(compute_PPV(sensitivity, specificity, incidence))

main()
